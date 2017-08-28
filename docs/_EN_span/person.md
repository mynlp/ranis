---
layout: base
title: 'person'
shortdef: 'human individuals and groups'
---

## <a class="span" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Scope

References to human individuals, groups, and humanity as a whole are
annotated as <a class="span" nolink>person</a> regardless of
specificity.


### Syntactic constraints

Names and nominal mentions (see Span annotation: [Name mention annotation](../span-annotation.html#name-mention-annotation) and [Nominal mention annotation](../span-annotation.html#nominal-mention-annotation)) plus pronominal
references.


### Examples

* <q>Markov</q>

  <div class="ann-annotation">
  hidden Markov model
  T1 PLAN 0 19 hidden Markov model
  T2 PERSON 7 14 
  </div>

* <q>Eugene Charniak</q>

  <div class="ann-annotation">
  statistically-based methods developed by Eugene Charniak
  T1 PLAN 0 27 statistically-based methods
  T2 PROCESS 28 37 developed
  T3 PERSON 40 56 Eugene Charniak
  </div>

* <q>Bayesian</q>

  <div class="ann-annotation">
  Bayesian methods
  T1 PERSON 0 8 Bayesian
  T2 PLAN 0 16 methods
  </div>

* <q>engineers</q>

  <div class="ann-annotation">
  engineers apply techniques
  T1 PERSON 0 9 engineers
  T2 PROCESS 10 15 apply
  T3 PLAN 16 26 techniques
  </div>

* <q>humans</q>

  <div class="ann-annotation">
  linguistic information from humans
  T1 DATA-ITEM 0 22 linguistic information
  T2 PERSON 27 34 humans
  </div>

* <q>users</q>

  <div class="ann-annotation">
  information about the location of users
  T1 DATA-ITEM 0 11 information
  T2 LOCATION 21 30 location
  T3 PERSON 34 39 users 
  </div>

* <q>they</q>

  <div class="ann-annotation">
  they use the computers
  T1 PERSON 0 4 they
  T2 PROCESS 5 8 use
  T3 ARTIFACT 13 22 computers 
  </div>



### Further details

<a class="span" nolink>person</a> annotation is exhaustive and
mentions are annotated also when nested in annotations of other
types. For example, although the entire span <q>Brown, Della Pietra
and Mercer (1993)</q> is annotated as <a
class="span" nolink>external-reference</a>, each of the embedded mentions
<q>Brown</q>, <q>Della Pietra</q> and <q>Mercer</q> is annotated as <a
class="span" nolink>person</a>.


### References

See also <a class="span">intelligent-agent</a>, Contrast <a
class="span">organization</a>.
