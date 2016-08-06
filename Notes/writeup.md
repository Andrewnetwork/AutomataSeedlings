<center>
    <h1>The Theory of Automata Seedlings</h1>
    <h3><i>How you are created is what you are.</i></h3>
</center>
<hr/>

The general problem of one-shot learning: Given a set of reference structures S, and a new list of structures NS, match
each new structure in NS to a corresponding reference structure in S based on their <i>inherent similarity</i>.

```python
for e in NS:
    for s in S:
        #Find the largest ( e sim s )
```

The reason one-shot learning interests me is due to the notion of finding similarity based on inherent structure --
which I feel is closer to how humans perform pattern recognition than current methods like Neural Nets. We can be given
an arbitrary reference alphabet and perform one-shot learning without extensive training over several thousand variants.


