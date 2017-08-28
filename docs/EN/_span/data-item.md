---
layout: base
title: 'data-item'
shortdef: 'static information entities'
---

## <a class="span" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Scope

References to data, datasets, documents, their parts, collections,
universals, and similar information entities that can not be realized
as processes (cf. <a class="span">plan</a>) are annotated as <a
class="span" nolink>data-item</a>.


### Syntactic constraints

Names and nominal mentions (see Span annotation: [Name mention annotation](../span-annotation.html#name-mention-annotation) and [Nominal mention annotation](../span-annotation.html#nominal-mention-annotation))


### Examples

* <q>data</q>

  <div class="ann-annotation">
  analyse data from web
  T1 PROCESS 0 7 analyse
  T2 DATA-ITEM 8 12 data
  T3 DATA-ITEM 18 21 web
  </div>

* <q>word</q>

  <div class="ann-annotation">
  meaning of a word
  T1 DATA-ITEM 0 7 mining
  T2 DATA-ITEM 13 17 word
  </div>

* <q>result</q>

  <div class="ann-annotation">
  the results of a project
  T1 DATA-ITEM 4 11 results
  T2 PLAN 17 24 project
  </div>

* <q>information</q>

  <div class="ann-annotation">
  retrieve information from speech data
  T1 PROCESS 0 8 retrieve
  T2 DATA-ITEM 9 20 information
  T3 DATA-ITEM 26 37 speech data
  </div>

* <q>training corpus</q>

  <div class="ann-annotation">
  different training corpus
  T1 QUALITY 0 9 different
  T2 DATA-ITEM 10 25 training corpus
  </div>

* <q>parse tree</q>

  <div class="ann-annotation">
  a parse tree is decomposed into meta-structure
  T1 DATA-ITEM 2 12 parse tree
  T2 PROCESS 16 26 decomposed
  T3 DATA-ITEM 32 46 meta-structure
  </div>

* <q>graph</q>

  <div class="ann-annotation">
  draw a graph
  T1 PROCESS 0 4 draw
  T2 DATA-ITEM 7 12 graph
  </div>



### References

The semantic scope of <a class="span" nolink>data-item</a> includes
those of <a class="onto">data item<sub>IAO</sub></a> and <a
class="onto">textual entity<sub>IAO</sub></a>. (see Ontological basis: [Information entities](../ontological-basis.html#information-entities)). See
also <a class="onto">information content entity<sub>IAO</sub></a>;
contrast <a class="span">plan</a> / <a class="onto">directive
information entity<sub>IAO</sub></a>.  Contrast <a
class="span">quality</a>, see [Specific annotation guidelines](../specific-guidelines.html#data-item-vs-quality).
