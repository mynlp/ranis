---
layout: base
title: 'apply-to'
shortdef: 'purpose, intentional result'
---

## <a class="relation" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Definition

A is a process, method, technique, program, tool, or similar, which
has process or plan B as its purpose, including cases where B occurs
as an intentional result of A. Conversely, seen from the perspective
of B, process or plan A can be seen as an instrument for realizing
B. (<a class="relation" nolink>apply-to</a> can thus be thought of as a composite INSTRUMENT-PURPOSE
relation.)


### Examples

* Relation between a process or plan and its purpose.

  <div class="ann-annotation">
  extend by imitation
  T1 PROCESS 0 6 extend
  T2 PROCESS 10 19 imitation
  R1 APPLY-TO Arg1:T2 Arg2:T1
  </div>

* Relation between a process or plan and its intentional result.

  <div class="ann-annotation">
  progress by imitation learning
  T1 PROCESS 0 8 progress
  T2 PROCESS 12 30 imitation learning
  R1 APPLY-TO Arg1:T2 Arg2:T1
  </div>


* Relation between a program (PLAN) and its function.

  <div class="ann-annotation">
  a system to support users
  T1 PLAN 2 8 system
  T2 PROCESS 12 19 support
  T3 PERSON 20 25 users
  R1 APPLY-TO Arg1:T1 Arg2:T2
  </div>



### Argument types

Arg1: <a class="span" nolink>process</a> or <a class="span" nolink>plan</a> or <a class="span" nolink>artifact</a>

Arg2: <a class="span" nolink>process</a> or <a class="span" nolink>plan</a> or <a class="span" nolink>artifact</a>


### Direction

From applied <a class="span" nolink>process</a> or <a class="span" nolink>plan</a> to the <a class="span" nolink>process</a> or <a class="span" nolink>plan</a> applied to.


### Further details

Note: <q>method used in system</q>: method−<a class="relation" nolink>apply-to</a>→system, but <q>data used in system</q>: system−<a class="relation" nolink>input</a>→data


### References

Contrast <a class="relation">result</a> (intentional
vs. non-intentional), <a class="relation">input</a>.
See also Section 8.5.
