---
layout: base
title: 'name'
shortdef: 'specific name'
---

## <a class="span" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Scope

Span annotations that mark the specific names of people, systems, datasets, languages, countries, etc. are marked with the <a class="flag" nolink>name</a> flag. Specifically, a <a class="flag" nolink>name</a> flag can be assigned to annotations of the following, and only the following, types: <a class="span" nolink>person</a>, <a class="span" nolink>plan</a>, <a class="span" nolink>data-item</a>, <a class="span" nolink>language</a>, <a class="span" nolink>location</a>, <a class="span" nolink>organization</a>, <a class="span" nolink>artifact</a>.


### Examples

* <q>Markov</q>

  <div class="ann-annotation">
  Markov
  T1 PERSON 0 6 Markov
  A1 Name T1
  </div>

* <q>AdaBoost</q>

  <div class="ann-annotation">
  AdaBoost
  T1 PLAN 0 8 AdaBoost
  A1 Name T1
  </div>

* <q>Penn Treebank</q>

  <div class="ann-annotation">
  Penn Treebank
  T1 DATA-ITEM 0 13 Penn Treebank
  A1 Name T1
  </div>

* <q>Japanese</q>

  <div class="ann-annotation">
  Japanese
  T1 LANGUAGE 0 8 Japanese
  A1 Name T1
  </div>

* <q>USA</q>

  <div class="ann-annotation">
  USA
  T1 LOCATION 0 3 USA
  A1 Name T1
  </div>

* <q>DARPA</q>

  <div class="ann-annotation">
  DARPA
  T1 ORGANIZATION 0 5 DARPA
  A1 Name T1
  </div>

* <q>MacBook</q>

  <div class="ann-annotation">
  MacBook
  T1 ARTIFACT 0 7 MacBook
  A1 Name T1
  </div>

