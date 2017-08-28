---
layout: base
title: 'quality'
shortdef: 'properties of other entities'
---

## <a class="span" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Scope

References to properties that are carried by (inhere in) specific
other entities are annotated as <a class="span" nolink>quality</a>,
excluding potentially absent but realizable entities (functions,
roles, and dispositions).  Includes references to qualities in general
(as universals, without reference to any entity carrying the quality)
such as <q>color</q>.


### Syntactic constraints

Nominal mentions (see Span annotation: [Nominal mention annotation](../span-annotation.html#nominal-mention-annotation) plus adjectival and adverbial
references to qualities.


### Examples

* <q>novel [approach]</q>

  <div class="ann-annotation">
  novel approach
  T1 QUALITY 0 5 novel
  T2 PLAN 6 14 approach
  </div>

* <q>large [dataset]</q>

  <div class="ann-annotation">
  large dataset
  T1 QUALITY 0 5 large
  T2 DATA-ITEM 6 13 dataset
  </div>

* <q>efficient [implementation]</q>

  <div class="ann-annotation">
  efficient implementation
  T1 QUALITY 0 9 efficient
  T2 PLAN 10 24 implementation
  </div>

* <q>[system is] good</q>

  <div class="ann-annotation">
  system is good
  T1 PLAN 0 6 system
  T2 QUALITY 10 14 good
  </div>

* <q>[method is] better</q>

  <div class="ann-annotation">
  method is better
  T1 PLAN 0 6 method
  T2 QUALITY 10 16 better
  </div>

* <q>[method executes] well</q>

  <div class="ann-annotation">
  method executes well
  T1 PLAN 0 6 method
  T2 PROCESS 7 15 executes
  T3 QUALITY 16 20 well
  </div>

* <q>most efficient [implementation]</q>: <a class="span" nolink>quality</a>(<q>most efficient</q>) (see below)

  <div class="ann-annotation">
  most efficient implementation
  T1 QUALITY 0 14 most efficient
  T2 PLAN 15 29 implementation
  </div>

* <q>new efficient [implementation]</q>: <a class="span" nolink>quality</a>(<q>new</q>) <a class="span" nolink>quality</a>(<q>efficient</q>) (see below)

  <div class="ann-annotation">
  new efficient implementation
  T1 QUALITY 0 3 new
  T2 QUALITY 4 13 efficient
  T3 PLAN 14 28 implementation
  </div>



### Further details

When multiple words are used to express a single quality (e.g. in
comparative and superlative expressions such as <q>more efficient</q>
or <q>most efficient</q>), a single <a class="span" nolink>quality</a>
annotation is used to mark the whole expression. By contrast, multiple
independent qualities are marked separately even when appearing
consecutively (e.g. <q>new efficient</q>).


### References

The semantic scope of <a class="span" nolink>quality</a> annotations
includes that of `quality`_BFO (see Ontological basis: [Top-level organization](../ontological-basis.html#top-level-organization). By contrast to
`quality`_BFO, the scope of <a class="span" nolink>quality</a>
annotations includes properties of processes.

