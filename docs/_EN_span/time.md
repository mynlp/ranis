---
layout: base
title: 'time'
shortdef: 'any part of time'
---

## <a class="span" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Scope

References to both instants and time intervals (including open ones)
as well as discontinuous (scattered) regions of time are all annotated
as <a class="span" nolink>time</a>. References to all of time are
annotated similarly. Statements referencing time are annotated
regardless of their (im)precision, and both absolute and relative
references to time are annotated.


### Syntactic constraints

None. References to time are annotated without regard for the parts of
speech or other syntactic aspects of the marked text. In particular,
prepositions relating to the boundaries of regions of time such as
<q>before</q> are included in <a class="span" nolink>time</a>
annotations.


### Examples

* <q>today</q>

  <div class="ann-annotation">
  Today's Internet industry
  T1 TIME 0 5 Today
  T2 ORGANIZATION 8 25 Internet industry
  </div>

* <q>recently</q>

  <div class="ann-annotation">
  a software recently developed
  T1 PLAN 2 10 software
  T2 TIME 11 19 recently
  T3 PROCESS 20 29 developed 
  </div>

* <q>2014</q>

  <div class="ann-annotation">
  published in 2014
  T1 PROCESS 0 9 published
  T2 TIME 13 17 2014
  </div>

* <q>before 2014</q>

  <div class="ann-annotation">
  babies born before 2014
  T1 PERSON 0 6 babies
  T2 PROCESS 7 11 born
  T3 TIME 12 23 before 2014
  </div>

* <q>every summer</q>

  <div class="ann-annotation">
  visit Europe every summer
  T1 PROCESS 0 5 visit
  T2 LOCATION 6 12 Europe
  T3 TIME 13 25 every summer
  </div>

* <q>until recently</q>

  <div class="ann-annotation">
  updated until recently
  T1 PROCESS 0 7 updated
  T2 TIME 8 22 until recently
  </div>

* <q>always</q>

  <div class="ann-annotation">
  discourse coherence has always been used
  T1 DATA-ITEM 0 19 discourse coherence
  T2 TIME 24 30 always
  T3 PROCESS 36 40 used 
  </div>

* <q>before</q>

  <div class="ann-annotation">
  confirm before submitting
  T1 PROCESS 0 7 confirm
  T2 TIME 8 14 before
  T3 PROCESS 15 25 submitting
  </div>



### References

The semantic scope of <a class="span" nolink>time</a> annotations
matches that of <a class="onto">temporal region<sub>BFO</sub></a> (see
Ontological basis: [Top-level organization](../ontological-basis.html#top-level-organization)). Contrast <a class="span">process</a>.
