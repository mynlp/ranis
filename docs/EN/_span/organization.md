---
layout: base
title: 'organization'
shortdef: 'group established for purpose'
---

## <a class="span" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Scope

References to any established groups of people organized for an
explicit purpose, whether governmental, commercial, educational, or
other, are annotated as <a class="span" nolink>organization</a>
regardless of specificity, including references to collectives and
universals of organizations such as <q>industry</q>.


### Syntactic constraints

Names and nominal mentions (see Span annotation: [Name mention annotation](../span-annotation.html#name-mention-annotation) and [Nominal mention annotation](../span-annotation.html#nominal-mention-annotation))


### Examples

* <q>Apple</q>

  <div class="ann-annotation">
  Mac OS X developed by Apple
  T1 PLAN 0 8 Mac OS X
  T2 PROCESS 9 18 developed
  T3 ORGANIZATION 22 27 Apple
  </div>

* <q>DARPA</q>

  <div class="ann-annotation">
  DARPA-TDT evaluation metrics
  T1 ORGANIZATION 0 5 DARPA
  T2 PLAN 6 9 TDT
  T3 PLAN 0 28 DARPA-TDT evaluation metrics
  </div>

* <q>Charles University</q>

  <div class="ann-annotation">
  Charles University (CUNI)
  T1 ORGANIZATION 0 18 Charles University
  T2 ORGANIZATION 20 24 CUNI
  </div>

* <q>Internet companies</q>

  <div class="ann-annotation">
  today's internet companies
  T1 TIME 0 5 today
  T2 ORGANIZATION 8 26 internet companies
  </div>

* <q>advertizers</q>

  <div class="ann-annotation">
  queries shared between the advertisers
  T1 DATA-ITEM 0 7 queries
  T2 PROCESS 8 14 shared
  T3 ORGANIZATION 26 38 advertisers 
  </div>

* <q>industry</q>

  <div class="ann-annotation">
  released for industry
  T1 PROCESS 0 8 released
  T2 ORGANIZATION 12 21 industry
  </div>

* <q>eBay</q>

  <div class="ann-annotation">
  empirical analysis of eBay
  T1 PLAN-OR-PROCESS 0 18 empirical analysis
  T2 ORGANIZATION 22 26 eBay
  </div>



### Further details

<a class="span" nolink>organization</a> is preferred over <a
class="span">person</a> whenever applicable, but only applies to
references of groups of people where a specific organization is
explicit. For example, reference to a <q>teachers' union</q> is
annotated as <a class="span" nolink>organization</a>, but general
reference to <q>teachers</q> is annotated as <a
class="span">person</a>.


### References

The semantic scope of <a class="span" nolink>organization</a> includes
that of ORG(anization) in "classical" named entity recognition tasks
as a subset. Contrast <a class="span">person</a>.
