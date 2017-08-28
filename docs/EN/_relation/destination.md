---
layout: base
title: 'destination'
shortdef: 'end point'
---

## <a class="relation" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Definition

End point or destination of an action; in the case of addition or
assignment (etc.), used to capture the thing added to
("destination of addition").


### Examples

* end point of action, e.g. movement

  <div class="ann-annotation">
  go from Otemachi to Jinbocho
  T1 PROCESS 0 2 go
  T2 LOCATION 7 16 Otemachi
  T3 LOCATION 20 28 Jinbocho
  R1 ORIGIN Arg1:T1 Arg2:T2
  R2 DESTINATION Arg1:T1 Arg2:T3
  </div>


* thing added, assigned, etc. to

  <div class="ann-annotation">
  probability is assigned to nodes
  T1 DATA-ITEM 0 11 probability
  T2 PROCESS 14 23 assigned
  T3 DATA-ITEM 27 32 nodes
  R1 IN-OUT Arg1:T1 Arg2:T2
  R2 DESTINATION Arg1:T2 Arg2:T3
  </div>



### Argument types

Arg1: <a class="span" nolink>process</a> or <a class="span" nolink>plan</a>

Arg2: <a class="span" nolink>data-item</a> or <a class="span" nolink>plan</a> or <a class="span" nolink>plan-or-process</a> or <a class="span" nolink>location</a>


### Direction

From <a class="span" nolink>process</a> or <a class="span" nolink>plan</a> to its argument.


### Further details

* The direction of this relation is reversed from that in the Japanese
  annotation.


### References