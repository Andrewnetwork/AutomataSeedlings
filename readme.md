<center>
    <h1>The Theory of Automata Seedlings</h1>
    <h3><i>How you are created is what you are.</i></h3>
</center>
<hr/>
<h2>Problem Definition</h2>

The general problem of <b>one-shot learning</b>:

Given a set of reference structures S, and a new list of structures NS, match
each new structure in NS to a corresponding reference structure in S based on their inherent similarity.

```python
for e in NS:
    for s in S:
        #Find the largest ( e sim s )
```

One-shot learning interests me due to the notion of finding similarity based on inherent structure --
which I feel is closer to how humans perform pattern recognition than current methods like Neural Nets. We can be given
an arbitrary reference alphabet and perform one-shot learning without extensive training over several thousand variants.


<h2>Motivation</h2>
<p>
The problem that concerns me is <b>one-shot learning</b>.
To be given a single reference and apply pattern recognition to new examples and have the ability to report some measure
of sameness. Humans do this particularly well. If I was to provide you a reference card of an unfamiliar alphabet and
show you a series of hand written variants of that alphabet, chances are you'd be able to match a high percentage of
this test set with the reference alphabet -- perhaps misclassifying a few exotic variations. The current state-of-the-art
for visual pattern recognition are convolutional neural nets. The problem with convolutional neural nets, and with
neural networks to begin with, is that they require massive amounts of labeled data to train on and resources to do so.

</p>

<h3>The Importance of One-Shot Learning</h3>
<p>
The ability to find similarity between structures inheirent in their nature bears unprecidented power for computer applications.



Similarity is the foundation of structure and order. For numbers, we can define similarity... sim(a,b) = | a - b |.

The only reason why we can order a list such as <b><i>A</i></b> = [10,3,8,1,7] is because we have a definition of similarity,
which produces structure.
</p>

<h3>Configuration Setup</h3>
<p>I reccomend you install virtualenv, then when you activate your new environment, pip install my requirements, which is a complete data science setup. It is not a minimum requirements list, in that there are many packages included that are not required to run the programs herein.</p>
<code>pip install -r requirements.txt</code>

<h1>WORK IN PROGRESS</h1>