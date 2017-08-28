---
layout: base
title: 'condition'
shortdef: 'constraint or restriction'
---

## <a class="relation" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Definition

Experimental condition, scope of applicability (time, place, etc.) or
similar, B modifies A.


### Examples

* Domain constraint

  <div class="ann-annotation">
  popularity is increasing in NLP
  T1 QUALITY 0 10 popularity
  T2 PROCESS 14 24 increasing
  T3 DOMAIN 28 31 NLP
  R1 IN-OUT Arg1:T2 Arg2:T1
  R2 CONDITION Arg1:T2 Arg2:T3
  </div>

* Location constraint

  <div class="ann-annotation">
  information system in public area
  T1 PLAN 0 18 information system
  T2 LOCATION 22 33 public area
  R1 CONDITION Arg1:T1 Arg2:T2
  </div>

* Time constraint

  <div class="ann-annotation">
  experiments before 2004
  T1 PROCESS 0 11 experiments
  T2 TIME 12 23 before 2004
  R1 CONDITION Arg1:T1 Arg2:T2
  </div>

* Other constraints

  * TODO

  <div class="ann-annotation" tabs="yes">
  TODO
  </div>

  * <a class="relation" nolink>condition</a> for <a class="span" nolink>quality</a>

  <div class="ann-annotation">
  the algorithm is efficient to run
  T1 PLAN 4 13 algorithm
  T2 QUALITY 16 26 efficient
  T3 PROCESS 30 33 run
  R1 ATTRIBUTE Arg1:T1 Arg2:T2
  R2 CONDITION Arg1:T2 Arg2:T3
  </div>

6. "possibility of" or "risk of"

* TODO

  <div class="ann-annotation" tabs="yes">
  TODO
  </div>

### Argument types

Arg1: <a class="span" nolink>process</a> or <a class="span" nolink>plan</a> or <a class="span" nolink>quality</a> or <a class="span" nolink>quantity</a> or <a class="span" nolink>data-item</a>

Arg2: any entity


### Direction

From constrained entity to constraint.


### Further details

* The direction of this relation is reversed from that in the Japanese annotation.


### References