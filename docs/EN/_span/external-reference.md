---
layout: base
title: 'external-reference'
shortdef: 'literature references'
---

## <a class="span" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Scope

Any statement or span of text that is in context understood to be a
reference to publications other than the document it appears in is
annotated as <a class="span" nolink>external-reference</a>, including
references to collections of publications, subsets of the literature,
and the literature as a whole.


### Syntactic constraints

None. <a class="span" nolink>external-reference</a> annotations may
consist of only non-alphabetic symbols and numbers, contain
coordinations, etc. (see Examples below)


### Examples

* <q>literature</q>

  <div class="ann-annotation">
  results reported in the literature
  T1 DATA-ITEM 0 7 results
  T2 PROCESS 8 16 reported
  T3 EXTERNAL-REFERENCE 24 34 literature
  </div>

* <q>prior studies</q>

  <div class="ann-annotation">
  prior studies address
  T1 EXTERNAL-REFERENCE 0 13 prior studies
  T2 PROCESS 14 21 address
  </div>

* <q>previous work</q>

  <div class="ann-annotation">
  models proposed in the previous work
  T1 PLAN 0 6 models
  T2 PROCESS 7 15 proposed
  T3 EXTERNAL-REFERENCE 23 36 previous work
  </div>

* <q>game theory literature</q>

  <div class="ann-annotation">
  commitments in game theory literature
  T1 PLAN 0 11 commitments
  T2 EXTERNAL-REFERENCE 15 37 game theory literature
  </div>

* <q>Brown, Della Pietra and Mercer (1993)</q>

  <div class="ann-annotation">
  Brown, Della Pietra and Mercer (1993)
  T1 PERSON 0 5 Brown
  T2 PERSON 7 19 Della Pietra
  T3 PERSON 24 30 Mercer
  T4 TIME 32 36 1993
  T5 EXTERNAL-REFERENCE 0 37 Brown, Della Pietra and Mercer (1993)
  </div>

* <q>[26, 27]</q>

  <div class="ann-annotation">
  leveled commitment contract [26,27]
  T1 PLAN 0 27 leveled commitment contract
  T2 EXTERNAL-REFERENCE 29 34 26,27
  </div>

* <q>(1)</q>

  <div class="ann-annotation">
  cf. (1) and others
  T1 EXTERNAL-REFERENCE 4 7 (1)
  </div>

