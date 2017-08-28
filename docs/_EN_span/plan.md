---
layout: base
title: 'plan'
shortdef: 'information that can be realized as a process'
---

## <a class="span" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Scope

References to methods, algorithms, experimental designs, data format
specifications, programming languages, software, informal sequences of
instructions, and similar information entities that can be realized as
processes are annotated as <a class="span" nolink>plan</a>, including
collections and universals of such entities.


### Syntactic constraints

Names and nominal mentions (see Span annotation: [Name mention annotation](../span-annotation.html#name-mention-annotation) and [Nominal mention annotation](../span-annotation.html#nominal-mention-annotation))


### Examples

* <q>system</q>

  <div class="ann-annotation">
  implementation of the system
  T1 PLAN 0 14 implementation
  T2 PLAN 22 28 system 
  </div>

* <q>algorithm</q>

  <div class="ann-annotation">
  the algorithm makes lexical chains
  T1 PLAN 4 13 algorithm
  T2 PROCESS 14 19 makes
  T3 DATA-ITEM 20 34 lexical chains
  </div>

* <q>voting rules</q>

  <div class="ann-annotation">
  match for all voting rules
  T1 PROCESS 0 5 match
  T2 QUANTITY 10 13 all
  T3 PLAN 14 26 voting rules
  </div>

* <q>clustering algorithm</q>

  <div class="ann-annotation">
  clustering algorithm was applied
  T1 PLAN 0 20 clustering algorithm
  T2 PROCESS 25 32 applied
  </div>

* <q>multimedia system</q>

  <div class="ann-annotation">
  evaluate on a multimedia system
  T1 PROCESS 0 8 evaluate
  T2 PLAN 13 31 multimedia system
  </div>

* <q>Bayesian games</q>

  <div class="ann-annotation">
  the domain is modeled as Bayesian games
  T1 DOMAIN 4 10 domain
  T2 PROCESS 14 21 modeled
  T3 PLAN 24 39 Bayesian games
  </div>

* <q>CR framework</q>

  <div class="ann-annotation">
  parameter settings within the CR framework
  T1 DATA-ITEM 0 18 parameter settings
  T2 PLAN 30 42 CR framework
  </div>

* <q>classification method</q>

  <div class="ann-annotation">
  performance of the classification method
  T1 QUALITY 0 11 performance
  T2 PLAN 19 40 classification method
  </div>

* <q>formal model</q>

  <div class="ann-annotation">
  extend a formal model
  T1 PROCESS 0 6 extend
  T2 PLAN 8 21 formal model
  </div>



### Further details

In text, there is often ambiguity between methods (and similar)
conceived of in the abstract, described in natural language, presented
in (pseudo)code on paper, implemented in a programming language in a
computer, compiled into machine code, etc. <a class="span"
nolink>plan</a> annotation does not require this ambiguity to be
resolved: statements such as <q>[our] method</q> are annotated as <a
class="span" nolink>plan</a> regardless of which of the above they
refer to.

Note: mentions of metrics (e.g. <q>TFIDF</q>) are annotated as <a
class="span" nolink>plan</a> when understood as referring to methods
for calculating a value, and as <a class="span">data-item</a> when
understood as referring to those values themselves (see Specific annotation guidelines: [DATA-ITEM vs. PLAN](../specific-guidelines.html#data-item-vs-plan)).


### References

The semantic scope of <a class="span" nolink>plan</a> annotation
matches that of <a class="onto">directive information
entity<sub>IAO</sub></a>: "An information content entity whose
concretizations indicate to their bearer how to realize them in a
process." [2] (see Ontological basis: [Information entities](../ontological-basis.html#information-entities)). Contrast <a class="span">process</a>
and <a class="span">data-item</a>, consider <a
class="span">plan-or-process</a> for ambiguous cases.
