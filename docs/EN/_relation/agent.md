---
layout: base
title: 'agent'
shortdef: 'participant intentionally performing an action'
---

## <a class="relation" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Definition

B is person or similar intelligent agent intentionally initiating
process or plan A. Note that references to the author(s) of the
manuscript are out of scope (see [Internal and external](../annotation-scope.html#internal-and-external)).


### Examples

<div class="ann-annotation">
user runs the program
T1 PERSON 0 4 user
T2 PROCESS 5 9 runs
R1 AGENT Arg1:T2 Arg2:T1
</div>


### Argument types

Arg1: <a class="span" nolink>process</a> or <a class="span" nolink>plan</a>

Arg2: <a class="span" nolink>person</a> or <a class="span" nolink>prganization</a> or <a class="span" nolink>intelligent-agent</a>


### Direction

From process or plan to agent.


### Further details

* Important note: <a class="relation" nolink>agent</a> is not a general-purpose (proto-)agent role
  marker but is used considerably more restrictively, with preference
  given to other relation types, as specified in the following.

* When applicable, <a class="relation" nolink>input</a>, <a class="relation" nolink>output</a>, <a class="relation" nolink>in-out</a>, or <a class="relation" nolink>apply-to</a> are used instead
  of <a class="relation" nolink>agent</a>.

* AGENT is only used for intentional actions of the agent.

* Note: the label <a class="relation" nolink>agent</a> is not applied in the Japanese annotation,
  which uses the label <a class="relation" nolink>perform</a> instead. The direction of this relation
  is reversed from that of the corresponding <a class="relation" nolink>perform</a> relation in the
  Japanese annotation.


### References