---
layout: base
title: 'result'
shortdef: 'non-intentional outcome or logical conclusion'
---

## <a class="relation" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Definition

A is process or plan that affects B, but the effect is not intentional
(case 1). Alternatively, B is logical conclusion from evidence A (case
2).


### Examples

* As a result of A, B occurred (causative) (case 1)

  <div class="ann-annotation">
  as jekyll 2.3.0 is installed, examples are visualized
  T1 PLAN 3 15 jekyll 2.3.0
  T2 PROCESS 18 28 installed
  T3 DATA-ITEM 30 38 examples
  T4 PROCESS 42 53 visualized
  R1 OUTPUT Arg1:T2 Arg2:T1
  R2 IN-OUT Arg1:T4 Arg2:T3
  R3 RESULT Arg1:T2 Arg2:T4
  </div>

* When process or plan A was (intentionally) performed, an unintended
result B occurred (side-effect) (case 1)

  <div class="ann-annotation">
  after upgrading the system, an error observed
  T1 PROCESS 6 15 upgrading
  T2 PLAN 20 26 system
  T3 PLAN-OR-PROCESS 31 36 error
  T4 PROCESS 37 45 observed
  R1 IN-OUT Arg1:T1 Arg2:T2
  R2 OUTPUT Arg1:T4 Arg2:T3
  R3 RESULT Arg1:T1 Arg2:T3
  </div>

* As a conclusion of/based on evidence A, B holds (logical
conclusion) (case 2)

  <div class="ann-annotation">
  since the system has been upgraded, the command changed
  T1 PLAN 10 16 system
  T2 PROCESS 26 34 upgraded
  T3 PLAN 40 47 command
  T4 PROCESS 48 55 changed
  R1 IN-OUT Arg1:T2 Arg2:T1
  R2 IN-OUT Arg1:T4 Arg2:T3
  R3 RESULT Arg1:T2 Arg2:T4
  </div>


### Argument types

Arg1: <a class="span" nolink>process</a> or <a class="span" nolink>plan</a> (case 1); or any (case 2)

Arg2: <a class="span" nolink>process</a> or <a class="span" nolink>plan</a> (case 1); or any (case 2)


### Direction

From cause to result.


### Further details

* The case where an evaluation result B was observed as a result of
<a class="span" nolink>process</a> or <a class="span" nolink>plan</a> A was also annotated as <a class="relation" nolink>result</a> in the Japanese
relation annotation effort. Here, this relation is annotated using <a
class="relation">output</a>.

* The non-intentional outcome (case 1) and logical conclusion (case 2)
subtypes of <a class="relation" nolink>result</a> are semantically distinct and can additionally be
largely differentiated in the annotated data on the basis of whether
or not the annotation involves a trigger expression. The separation of
these two cases into two types may be considered in future work.


### References

Contrast <a class="relation">apply-to</a> (intentional
vs. non-intentional).
