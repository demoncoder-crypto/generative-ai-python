
# google.generativeai.protos.TaskType

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/generative_service.py#L57-L93">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Type of task for which the embedding will be used.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>google.generativeai.protos.TaskType(
    *args, **kwds
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Values</h2></th></tr>

<tr>
<td>

`TASK_TYPE_UNSPECIFIED`<a id="TASK_TYPE_UNSPECIFIED"></a>

</td>
<td>

`0`

Unset value, which will default to one of the
other enum values.

</td>
</tr><tr>
<td>

`RETRIEVAL_QUERY`<a id="RETRIEVAL_QUERY"></a>

</td>
<td>

`1`

Specifies the given text is a query in a
search/retrieval setting.

</td>
</tr><tr>
<td>

`RETRIEVAL_DOCUMENT`<a id="RETRIEVAL_DOCUMENT"></a>

</td>
<td>

`2`

Specifies the given text is a document from
the corpus being searched.

</td>
</tr><tr>
<td>

`SEMANTIC_SIMILARITY`<a id="SEMANTIC_SIMILARITY"></a>

</td>
<td>

`3`

Specifies the given text will be used for
STS.

</td>
</tr><tr>
<td>

`CLASSIFICATION`<a id="CLASSIFICATION"></a>

</td>
<td>

`4`

Specifies that the given text will be
classified.

</td>
</tr><tr>
<td>

`CLUSTERING`<a id="CLUSTERING"></a>

</td>
<td>

`5`

Specifies that the embeddings will be used
for clustering.

</td>
</tr><tr>
<td>

`QUESTION_ANSWERING`<a id="QUESTION_ANSWERING"></a>

</td>
<td>

`6`

Specifies that the given text will be used
for question answering.

</td>
</tr><tr>
<td>

`FACT_VERIFICATION`<a id="FACT_VERIFICATION"></a>

</td>
<td>

`7`

Specifies that the given text will be used
for fact verification.

</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>

`denominator`<a id="denominator"></a>

</td>
<td>

the denominator of a rational number in lowest terms

</td>
</tr><tr>
<td>

`imag`<a id="imag"></a>

</td>
<td>

the imaginary part of a complex number

</td>
</tr><tr>
<td>

`numerator`<a id="numerator"></a>

</td>
<td>

the numerator of a rational number in lowest terms

</td>
</tr><tr>
<td>

`real`<a id="real"></a>

</td>
<td>

the real part of a complex number

</td>
</tr>
</table>



## Methods

<h3 id="as_integer_ratio"><code>as_integer_ratio</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>as_integer_ratio()
</code></pre>

Return a pair of integers, whose ratio is equal to the original int.

The ratio is in lowest terms and has a positive denominator.

```
>>> (10).as_integer_ratio()
(10, 1)
>>> (-10).as_integer_ratio()
(-10, 1)
>>> (0).as_integer_ratio()
(0, 1)
```

<h3 id="bit_count"><code>bit_count</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>bit_count()
</code></pre>

Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

```
>>> bin(13)
'0b1101'
>>> (13).bit_count()
3
```

<h3 id="bit_length"><code>bit_length</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>bit_length()
</code></pre>

Number of bits necessary to represent self in binary.

```
>>> bin(37)
'0b100101'
>>> (37).bit_length()
6
```

<h3 id="conjugate"><code>conjugate</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>conjugate()
</code></pre>

Returns self, the complex conjugate of any int.


<h3 id="from_bytes"><code>from_bytes</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>from_bytes(
    byteorder=&#x27;big&#x27;, *, signed=False
)
</code></pre>

Return the integer represented by the given array of bytes.

bytes
  Holds the array of bytes to convert.  The argument must either
  support the buffer protocol or be an iterable object producing bytes.
  Bytes and bytearray are examples of built-in objects that support the
  buffer protocol.
byteorder
  The byte order used to represent the integer.  If byteorder is 'big',
  the most significant byte is at the beginning of the byte array.  If
  byteorder is 'little', the most significant byte is at the end of the
  byte array.  To request the native byte order of the host system, use
  `sys.byteorder' as the byte order value.  Default is to use 'big'.
signed
  Indicates whether two's complement is used to represent the integer.

<h3 id="is_integer"><code>is_integer</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>is_integer()
</code></pre>

Returns True. Exists for duck type compatibility with float.is_integer.


<h3 id="to_bytes"><code>to_bytes</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>to_bytes(
    length=1, byteorder=&#x27;big&#x27;, *, signed=False
)
</code></pre>

Return an array of bytes representing an integer.

length
  Length of bytes object to use.  An OverflowError is raised if the
  integer is not representable with the given number of bytes.  Default
  is length 1.
byteorder
  The byte order used to represent the integer.  If byteorder is 'big',
  the most significant byte is at the beginning of the byte array.  If
  byteorder is 'little', the most significant byte is at the end of the
  byte array.  To request the native byte order of the host system, use
  `sys.byteorder' as the byte order value.  Default is to use 'big'.
signed
  Determines whether two's complement is used to represent the integer.
  If signed is False and a negative integer is given, an OverflowError
  is raised.

<h3 id="__abs__"><code>__abs__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__abs__()
</code></pre>

abs(self)


<h3 id="__add__"><code>__add__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__add__(
    value, /
)
</code></pre>

Return self+value.


<h3 id="__and__"><code>__and__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__and__(
    value, /
)
</code></pre>

Return self&value.


<h3 id="__bool__"><code>__bool__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__bool__()
</code></pre>

True if self else False


<h3 id="__eq__"><code>__eq__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__eq__(
    other
)
</code></pre>

Return self==value.


<h3 id="__floordiv__"><code>__floordiv__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__floordiv__(
    value, /
)
</code></pre>

Return self//value.


<h3 id="__ge__"><code>__ge__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__ge__(
    other
)
</code></pre>

Return self>=value.


<h3 id="__gt__"><code>__gt__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__gt__(
    other
)
</code></pre>

Return self>value.


<h3 id="__invert__"><code>__invert__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__invert__()
</code></pre>

~self


<h3 id="__le__"><code>__le__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__le__(
    other
)
</code></pre>

Return self<=value.


<h3 id="__lshift__"><code>__lshift__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__lshift__(
    value, /
)
</code></pre>

Return self<<value.


<h3 id="__lt__"><code>__lt__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__lt__(
    other
)
</code></pre>

Return self<value.


<h3 id="__mod__"><code>__mod__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__mod__(
    value, /
)
</code></pre>

Return self%value.


<h3 id="__mul__"><code>__mul__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__mul__(
    value, /
)
</code></pre>

Return self*value.


<h3 id="__ne__"><code>__ne__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__ne__(
    other
)
</code></pre>

Return self!=value.


<h3 id="__neg__"><code>__neg__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__neg__()
</code></pre>

-self


<h3 id="__or__"><code>__or__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__or__(
    value, /
)
</code></pre>

Return self|value.


<h3 id="__pos__"><code>__pos__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__pos__()
</code></pre>

+self


<h3 id="__pow__"><code>__pow__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__pow__(
    value, mod, /
)
</code></pre>

Return pow(self, value, mod).


<h3 id="__radd__"><code>__radd__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__radd__(
    value, /
)
</code></pre>

Return value+self.


<h3 id="__rand__"><code>__rand__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rand__(
    value, /
)
</code></pre>

Return value&self.


<h3 id="__rfloordiv__"><code>__rfloordiv__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rfloordiv__(
    value, /
)
</code></pre>

Return value//self.


<h3 id="__rlshift__"><code>__rlshift__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rlshift__(
    value, /
)
</code></pre>

Return value<<self.


<h3 id="__rmod__"><code>__rmod__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rmod__(
    value, /
)
</code></pre>

Return value%self.


<h3 id="__rmul__"><code>__rmul__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rmul__(
    value, /
)
</code></pre>

Return value*self.


<h3 id="__ror__"><code>__ror__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__ror__(
    value, /
)
</code></pre>

Return value|self.


<h3 id="__rpow__"><code>__rpow__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rpow__(
    value, mod, /
)
</code></pre>

Return pow(value, self, mod).


<h3 id="__rrshift__"><code>__rrshift__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rrshift__(
    value, /
)
</code></pre>

Return value>>self.


<h3 id="__rshift__"><code>__rshift__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rshift__(
    value, /
)
</code></pre>

Return self>>value.


<h3 id="__rsub__"><code>__rsub__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rsub__(
    value, /
)
</code></pre>

Return value-self.


<h3 id="__rtruediv__"><code>__rtruediv__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rtruediv__(
    value, /
)
</code></pre>

Return value/self.


<h3 id="__rxor__"><code>__rxor__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rxor__(
    value, /
)
</code></pre>

Return value^self.


<h3 id="__sub__"><code>__sub__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__sub__(
    value, /
)
</code></pre>

Return self-value.


<h3 id="__truediv__"><code>__truediv__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__truediv__(
    value, /
)
</code></pre>

Return self/value.


<h3 id="__xor__"><code>__xor__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__xor__(
    value, /
)
</code></pre>

Return self^value.






<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Class Variables</h2></th></tr>

<tr>
<td>

CLASSIFICATION<a id="CLASSIFICATION"></a>

</td>
<td>

`<TaskType.CLASSIFICATION: 4>`

</td>
</tr><tr>
<td>

CLUSTERING<a id="CLUSTERING"></a>

</td>
<td>

`<TaskType.CLUSTERING: 5>`

</td>
</tr><tr>
<td>

FACT_VERIFICATION<a id="FACT_VERIFICATION"></a>

</td>
<td>

`<TaskType.FACT_VERIFICATION: 7>`

</td>
</tr><tr>
<td>

QUESTION_ANSWERING<a id="QUESTION_ANSWERING"></a>

</td>
<td>

`<TaskType.QUESTION_ANSWERING: 6>`

</td>
</tr><tr>
<td>

RETRIEVAL_DOCUMENT<a id="RETRIEVAL_DOCUMENT"></a>

</td>
<td>

`<TaskType.RETRIEVAL_DOCUMENT: 2>`

</td>
</tr><tr>
<td>

RETRIEVAL_QUERY<a id="RETRIEVAL_QUERY"></a>

</td>
<td>

`<TaskType.RETRIEVAL_QUERY: 1>`

</td>
</tr><tr>
<td>

SEMANTIC_SIMILARITY<a id="SEMANTIC_SIMILARITY"></a>

</td>
<td>

`<TaskType.SEMANTIC_SIMILARITY: 3>`

</td>
</tr><tr>
<td>

TASK_TYPE_UNSPECIFIED<a id="TASK_TYPE_UNSPECIFIED"></a>

</td>
<td>

`<TaskType.TASK_TYPE_UNSPECIFIED: 0>`

</td>
</tr>
</table>

