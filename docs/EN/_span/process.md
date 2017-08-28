---
layout: base
title: 'process'
shortdef: 'things that happen'
---

## <a class="span" nolink>{{ page.title }}</a>: {{ page.shortdef }}

### Scope

Anything that has temporal parts / that happens that is not part of
time (<a class="span">time</a>), regardless of whether past, present,
future, hypothetical, counterfactual, etc. In addition to any single
process as whole, applies also to arbitrary parts and aggregates of
processes as well as to processual universals.

(contrast <a class="onto">process<sub>BFO</sub></a>: A processual entity that is
a maximally connected spatiotemporal whole and has bona fide
beginnings and endings corresponding to real discontinuities.)


### Syntactic constraints

Verbal and derived (e.g. nominalized) expressions. Spans normally
exclude determiners, prepositions etc. as per the standard guidelines
for nominals ([Nominal mention annotation](../span-annotation.html#nominal-mention-annotation)) but include prepositions and particles
for phrasal verbs (e.g. <q>deal with</q>).

### Examples

* <q>use</q>

  <div class="ann-annotation">
  The methods uses semantic similarity
  T1 PLAN 4 11 methods
  T2 PROCESS 12 16 uses
  T3 DATA_ITEM 17 36 semantic similarity
  </div>

* <q>move</q>

  <div class="ann-annotation">
  by moving to a graph perspective
  T1 PROCESS 3 9 moving
  T2 PLAN 15 32 graph perspective 
  </div>

* <q>implement</q>

  <div class="ann-annotation">
  We implemented a type inference algorithm
  T1 PROCESS 3 14 implemented
  T2 PLAN 16 41 type inference algorithm 
  </div>

* <q>evaluate</q>

  <div class="ann-annotation">
  Relevance features evaluate a sentence
  T1 PLAN 0 18 Relevance features
  T2 PROCESS 19 27 evaluate
  T3 DATA_ITEM 29 38 sentence 
  </div>

* <q>evaluation</q>

  <div class="ann-annotation">
  implementation and evaluation of a search and rescue system
  T1 PROCESS 0 14 implementation
  T2 PROCESS 18 29 evaluation
  T3 PLAN 35 59 search and rescue system
  </div>

* <q>predict</q>

  <div class="ann-annotation">
  a discriminative model for predicting the likelifood of a response
  T1 PLAN 2 22 discriminative model
  T2 PROCESS 26 37 predicting
  T3 DATA_ITEM 41 52 likelifood
  T4 DATA_ITEM 57 66 response
  </div>

* <q>develop</q>

  <div class="ann-annotation">
  We develop a graphical representation
  T1 PROCESS 3 10 develop
  T2 PLAN 12 37 graphical representation
  </div>

* <q>adapt</q>:

  <div class="ann-annotation">
  Adapting Asynchronous Messaging Middleware to ad-hoc Networking
  T1 PROCESS 0 8 Adapting
  T2 PLAN 9 42 Asynchronous Messaging Middleware
  T3 PLAN_OR_PROCESS 46 63 ad-hoc Networking
  </div>

### References

The semantic scope of <a class="span" nolink>process</a> annotation
matches that of <a class="onto">processual entity<sub>BFO</sub></a>:
"An occurrent that exists in time by occurring or happening, has
temporal parts and always involves and depends on some
entity. Examples: the life of an organism, the process of meiosis, the
course of a disease, the flight of a bird" [1] (see Ontological basis: [Top-level organization](../ontological-basis.html#top-level-organization)). Contrast <a class="span">plan</a>, <a class="span">time</a>,
consider <a class="span">plan-or-process</a> for ambiguous cases.
