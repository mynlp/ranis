---
layout: base
title: 'plan-or-process'
shortdef: 'plan or process (ambiguous)'
---

## <a class="span" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Scope

Any mention that is, in context, ambiguous between the <a
class="span">process</a> and <a class="span">plan</a> types is
annotated as <a class="span" nolink>plan-or-process</a>. No other
mention is annotated as <a class="span" nolink>plan-or-process</a>.


### Syntactic constraints

Following <a class="span">process</a> and <a class="span">plan</a>
constraints.


### Examples

* <q>learning</q>

  <div class="ann-annotation">
  leaning the sublexical relationships
  T1 PLAN-OR-PROCESS 0 7 learning
  T2 DATA-ITEM 12 36 sublexical relationships 
  </div>

* <q>experiments</q>

  <div class="ann-annotation">
  the experiments evaluate the performance
  T1 PLAN-OR-PROCESS 4 15 experiments
  T2 PROCESS 16 24 evaluate
  T3 DATA-ITEM 29 40 performance 
  </div>

* <q>error analysis</q>

  <div class="ann-annotation">
  error analysis of a transition-based parser
  T1 PLAN-OR-PROCESS 0 14 error analysis
  T2 PLAN 20 43 transition-based parser
  </div>

* <q>contextual advertizing</q>

  <div class="ann-annotation">
  a semantic approach to contextual advertising
  T1 PLAN 2 19 semantic approach
  T2 PLAN-OR-PROCESS 23 45 contextual advertising
  </div>

* <q>discourse clustering</q>

  <div class="ann-annotation">
  discourse clustering with POS n-gram profiles
  T1 PLAN-OR-PROCESS 0 20 discourse clustering
  T2 DATA-ITEM 26 45 POS n-gram profiles
  </div>

* <q>coreference resolution</q>

  <div class="ann-annotation">
  method for coreference resolution
  T1 PLAN 0 6 method
  T2 PLAN-OR-PROCESS 10 33 coreference resolution
  </div>

* <q>approximate search</q>

  <div class="ann-annotation">
  fast approximate search
  T1 QUALITY 0 4 fast
  T2 PLAN-OR-PROCESS 5 23 approximate search
  </div>

* <q>automatic tagging</q>

  <div class="ann-annotation">
  automatic tagging on speech data
  T1 PLAN-OR-PROCESS 0 17 automatic tagging
  T2 DATA-ITEM 21 32 speech data
  </div>



### References

See Ontological basis: [Ambiguous types](../ontological-basis.html#ambiguous-types) for more information on ambiguous types. Contrast <a
class="span">process</a>, <a class="span">plan</a>.
