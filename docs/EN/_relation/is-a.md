---
layout: base
title: 'is-a'
shortdef: 'instance of class'
---

## <a class="relation" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Definition

Relation between instance of class (universal) and that class

### Examples

* <q>documents (e.g. pictures)</q>

  <div class="ann-annotation">
  documents (e.g. pictures)
  T1 DATA-ITEM 0 9 documents
  T2 DATA-ITEM 16 24 pictures
  R1 IS-A Arg1:T2 Arg2:T1
  </div>

* <q>languages, including English</q>

  <div class="ann-annotation">
  languages, including English
  T1 LANGUAGE 0 9 languages
  T2 LANGUAGE 20 28 English
  R1 IS-A Arg1:T2 Arg2:T1
  </div>

* <q>AdaRank, a boosting algorithm</q>

  <div class="ann-annotation">
  AdaRank, a boosting algorithm
  T1 PLAN 0 7 AdaRank
  T2 PLAN 11 29 boosting algorithm
  R1 IS-A Arg1:T1 Arg2:T2
  </div>

* <q>linguistic entities such as words</q>

  <div class="ann-annotation">
  linguistic entities such as words
  T1 DATA-ITEM 0 19 linguistic entities
  T2 DATA-ITEM 28 33 words
  R1 IS-A Arg1:T2 Arg2:T1
  </div>

* <q>information such as co-occurrence statistics</q>

  <div class="ann-annotation">
  information such as co-occurrence statistics
  T1 DATA-ITEM 0 11 information
  T2 DATA-ITEM 20 44 co-occurrence statistics
  R1 IS-A Arg1:T2 Arg2:T1
  </div>

### Argument types

Arg1: any entity

Arg2: <q>same type as Arg1</q>


### Direction

From instance to class
