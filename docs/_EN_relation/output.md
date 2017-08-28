---
layout: base
title: 'output'
shortdef: 'output of process or plan'
---

## <a class="relation" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Definition

B is an output of <a class="span" nolink>process</a> or <a class="span" nolink>plan</a> A. A is not limited to concrete
processes and programs, but includes also abstract methods and
actions.


### Examples


<div class="ann-annotation">
information is provided
T1 DATA-ITEM 0 11 information
T2 PROCESS 15 23 provided
R1 OUTPUT Arg1:T2 Arg2:T1
</div>

<div class="ann-annotation">
spelling is extracted from text
T1 DATA-ITEM 0 8 spelling
T2 PROCESS 11 21 expected
T3 DATA-ITEM 27 31 text
R1 OUTPUT Arg1:T2 Arg2:T1
R2 INPUT Arg1:T2 Arg2:T3
</div>


### Argument types

Arg1: <a class="span" nolink>process</a> or <a class="span" nolink>plan</a>

Arg2: <a class="span" nolink>data-item</a> or <a class="span" nolink>plan</a> or <a class="span" nolink>plan-or-process</a> or <a class="span" nolink>quality</a> or <a class="span" nolink>quantity</a>


### Direction

From <a class="span" nolink>process</a> or <a class="span" nolink>plan</a> to its output.


### Further details

* The case <a class="relation" nolink>output</a> Arg2 <a class="span" nolink>quantity</a> applies to expressions relating to
  evaluation (e.g. <q>evaluation showed 90% accuracy</q>), where the
  relation between the evaluation process and its result is typed
  <a class="relation" nolink>output</a>.

* The direction of this relation is reversed from that in the Japanese
  annotation.


### References