---
layout: base
title: 'in-out'
shortdef: 'both input and output of process or plan'
---

## <a class="relation" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Definition

B is both the input and output of <a class="span" nolink>process</a> or <a class="span" nolink>plan</a> A. A is not limited
to concrete processes and programs, but includes also abstract methods
and actions.


### Examples

<div class="ann-annotation">
log an error message
T1 PROCESS 0 3 log
T2 DATA-ITEM 6 20 error message
R1 IN-OUT Arg1:T1 Arg2:T2
</div>

<div class="ann-annotation">
select the best parameters
T1 PROCESS 0 6 select
T2 QUALITY 11 15 best
T3 DATA-ITEM 16 26 parameters
R1 ATTRIBUTE Arg1:T3 Arg2:T2
R2 IN-OUT Arg1:T1 Arg2:T3
</div>


### Argument types

Arg1: <a class="span" nolink>process</a> or <a class="span" nolink>plan</a>

Arg2: <a class="span" nolink>data-item</a> or <a class="span" nolink>plan</a> or <a class="span" nolink>plan-or-process</a> or <a class="span" nolink>quality</a>


### Direction

From <a class="span" nolink>process</a> or <a class="span" nolink>plan</a> to its <a class="span" nolink>input/output</a>.


### Further details

* The direction of this relation is reversed from that in the Japanese
  annotation.


### References