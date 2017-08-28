---
layout: base
title: 'attribute'
shortdef: 'property, feature'
---

## <a class="relation" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Definition

A is dependent on B (TODO: check def, direction)


### Examples

* A has property B

  <div class="ann-annotation">
  performance of system
  T1 QUALITY 0 11 performance
  T2 PLAN 15 21 system
  R1 ATTRIBUTE Arg1:T2 Arg2:T1
  </div>

  <div class="ann-annotation">
  function of program
  T1 PLAN 0 8 function
  T2 PLAN 12 19 program
  R1 ATTRIBUTE Arg1:T2 Arg2:T1
  </div>

* A has feature B

  <div class="ann-annotation">
  private installation
  T1 QUALITY 0 7 private
  T2 PLAN-OR-PROCESS 8 20 installation
  R1 ATTRIBUTE Arg1:T2 Arg2:T1
  </div>

* PROCESS or PLAN A behaves in manner B

  <div class="ann-annotation">
  process exhaustively
  T1 PROCESS 0 7 process
  T2 QUALITY 8 20 exhaustively
  R1 ATTRIBUTE Arg1:T1 Arg2:T2
  </div>

* MODALITY of PROCESS or PLAN (or similar)

  <div class="ann-annotation">
  can be performed
  T1 MODALITY 0 3 can
  T2 PROCESS 7 16 performed
  R1 ATTRIBUTE Arg1:T2 Arg2:T1
  </div>


### Argument types

Arg1: any entity

Arg2: <a class="span" nolink>quality</a> or <a class="span" nolink>quantity</a> or <a class="span" nolink>data-item</a> or <a class="span" nolink>plan</a> or <a class="span" nolink>plan-or-process</a> or <a class="span" nolink>language</a> or <a class="span" nolink>time</a> or <a class="span" nolink>domain</a> or <a class="span" nolink>location</a>


### Direction

From entity to dependent attribute, property or feature.


### Further details

* When applicable, <a class="relation" nolink>is-a</a>, <a class="relation" nolink>member-collection</a> and <a class="relation" nolink>component-object</a> are
  used instead of <a class="span" nolink>attribute</a>

* When applicable, <a class="relation" nolink>attribute</a> is used instead of <a class="relation" nolink>condition</a>.

* The direction of this relation is reversed from that in the Japanese
  annotation.

* In the Japanese annotation, the relation <a class="relation" nolink>evaluate</a> is used to relate
  <a class="span" nolink>modality</a> (see [MODALITY](../span/modality.html)) annotations to the process or plan
  annotations that they modify.

* In the Japanese annotation, the relation EVALUATE is used to relate
  properties that represent value judgments to entities. Here, the
  <a class="relation" nolink>attribute</a> relation is used for this purpose and the <a class="span" nolink>judgment</a> flag to   differentiate these cases (see Flag annotation: [JUDGMENT](../flag/judgment.html))

* In the Japanese annotation, the relation <a class="relation" nolink>equivalence</a> is used to
  relate attributes with their values. Here, the <a class="relation" nolink>attribute</a> relation is
  used for this purpose.


### References