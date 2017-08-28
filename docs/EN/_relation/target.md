---
layout: base
title: 'target'
shortdef: 'target of action'
---

## <a class="relation" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Definition

Relation between method, process or action and entity whose state is
temporarily or reversibly affected by it.


### Examples

<div class="ann-annotation">
accelerate a car
T1 PROCESS 0 10 accelerate
T2 ARTIFACT 13 16 car
R1 TARGET Arg1:T1 Arg2:T2 
</div>

<div class="ann-annotation">
the car accelerates
T1 ARTIFACT 4 7 car
T2 PROCESS 8 19 accelerates
R1 TARGET Arg1:T2 Arg2:T1
</div>


### Argument types

Arg1: <a class="span" nolink>process</a> or <a class="span" nolink>plan</a>

Arg2: any entity


### Direction

From <a class="span" nolink>process</a> or <a class="span" nolink>plan</a> to its target.


### Further details

* Only reversible changes in state are annotated using
  <a class="relation" nolink>target</a>. Permanent and transformative changes in state or properties
  are annotated using <a class="relation" nolink>input</a>, <a class="relation" nolink>output</a> or <a class="relation" nolink>in-out</a>.

* The direction of this relation is reversed from that in the Japanese
  annotation.


### References