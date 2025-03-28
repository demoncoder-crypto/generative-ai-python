import google.generativeai as genai
import collections
import random
import math
from google.generativeai.types import GenerationConfig, GenerateContentResponse


def _normalize_probs(prob_map):
    total_prob = sum(prob_map.values())
    if total_prob == 0:
        num_tokens = len(prob_map)
        if num_tokens == 0:
            return {}
        equal_prob = 1.0 / num_tokens
        return {token: equal_prob for token in prob_map}

    return {token: prob / total_prob for token, prob in prob_map.items()}


def generate_content_min_p_approx(
    model: genai.GenerativeModel,
    prompt: str,
    max_new_tokens: int = 50,
    p_base: float = 0.1,
    temperature: float = 1.0,
    num_samples: int = 100,
    fallback_to_most_frequent: bool = True
) -> str:

    if not (0.0 < p_base <= 1.0):
        raise ValueError("p_base must be between 0.0 (exclusive) and 1.0 (inclusive)")

    generated_sequence = prompt
    current_prompt = prompt

    print(f"Starting min_p approximation (p_base={p_base}, temp={temperature}, samples={num_samples})...")

    for i in range(max_new_tokens):
        print(f"  Step {i+1}/{max_new_tokens}: Generating candidates...")
        try:
            estimation_config = GenerationConfig(
                candidate_count=num_samples,
                max_output_tokens=1,
                temperature=temperature
            )

            response: GenerateContentResponse = model.generate_content(
                current_prompt,
                generation_config=estimation_config,
            )

            if not response.candidates:
                 print("  Warning: No candidates generated by the API. Stopping generation.")
                 break

            token_counts = collections.Counter()
            valid_candidates = 0
            for candidate in response.candidates:
                if candidate.content and candidate.content.parts:
                    try:
                         token_text = candidate.content.parts[0].text
                         if token_text:
                            token_counts[token_text] += 1
                            valid_candidates += 1
                    except (IndexError, AttributeError, KeyError):
                        print(f"  Warning: Skipping malformed candidate: {candidate}")
                        continue
                else:
                     print(f"  Warning: Skipping empty or blocked candidate: {candidate.finish_reason}, {candidate.safety_ratings}")


            if valid_candidates == 0:
                print("  Error: No valid tokens found among candidates. Stopping generation.")
                break

            estimated_probs = {token: count / valid_candidates for token, count in token_counts.items()}

            if not estimated_probs:
                 print("  Error: Estimated probabilities are empty. Stopping generation.")
                 break

            p_max = max(estimated_probs.values())
            p_threshold = p_base * p_max

            filtered_probs = {
                token: prob for token, prob in estimated_probs.items() if prob >= p_threshold
            }

            chosen_token = None
            if not filtered_probs:
                print("  Warning: Min_p filter resulted in empty set.")
                if fallback_to_most_frequent:
                    chosen_token = token_counts.most_common(1)[0][0]
                    print(f"    Falling back to most frequent token: '{chosen_token}'")
                else:
                    print("  Error: No tokens passed min_p filter and no fallback. Stopping.")
                    break
            else:
                normalized_filtered_probs = _normalize_probs(filtered_probs)

                tokens = list(normalized_filtered_probs.keys())
                probabilities = list(normalized_filtered_probs.values())
                chosen_token = random.choices(tokens, weights=probabilities, k=1)[0]

            if chosen_token is None:
                 print("  Error: Could not select a token. Stopping generation.")
                 break

            generated_sequence += chosen_token
            current_prompt += chosen_token

        except Exception as e:
            print(f"  Error during generation step {i+1}: {e}")
            break

    print("Finished min_p approximation.")
    return generated_sequence

if __name__ == "__main__":
    try:

        model = genai.GenerativeModel('gemini-1.5-flash-latest')

        initial_prompt = "Write a short story about a curious cat exploring a futuristic city."


        p_base_val = 0.1
        temp_val = 1.5
        samples_per_step = 100
        tokens_to_generate = 100


        generated_text = generate_content_min_p_approx(
            model,
            initial_prompt,
            max_new_tokens=tokens_to_generate,
            p_base=p_base_val,
            temperature=temp_val,
            num_samples=samples_per_step
        )

        print("\n--- Generated Text ---")
        print(generated_text)

    except Exception as e:
        print(f"An error occurred during example usage: {e}")
        print("Please ensure you have configured your API key and have access to the specified model.")