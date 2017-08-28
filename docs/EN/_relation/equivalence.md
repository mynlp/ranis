---
layout: base
title: 'equivalence'
shortdef: 'synonymy'
---

## <a class="relation" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Definition

Relation between expressions and their locally defined synonyms.


### Examples 

* full form (acronym)

  <div class="ann-annotation">
  part-of-speech (POS)
  T1 DATA-ITEM 0 14 part-of-speech
  T2 DATA-ITEM 16 19 POS
  R1 EQUIVALENCE Arg1:T2 Arg2:T1
  </div>

* acronym (full form)

  <div class="ann-annotation">
  QA (question answering)
  T1 PLAN 0 2 QA
  T2 PLAN 4 23 question answering
  R1 EQUIVALENCE Arg1:T2 Arg2:T1
  </div>



### Argument types

Arg1: any entity

Arg2: *same type as Arg1*


### Direction

From latter mention to former.


### Further details

* In the Japanese annotation, the relation <a class="relation" nolink>equivalence</a> is used to
  relate coreferential expressions. Here, the <a class="relation" nolink>coreference</a> relation is
  used for this purpose.

* In the Japanese annotation, the relation <a class="relation" nolink>equivalence</a> is used to
  relate attributes with their values. Here, the <a class="relation" nolink>attribute</a> relation is
  used for this purpose.


### References