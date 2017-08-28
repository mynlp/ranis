---
layout: base
title: 'origin'
shortdef: 'starting point'
---

## <a class="relation" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Definition

Starting point or origin of an action; in the case of removal or
deletion (etc.), used to capture the thing deleted from ("origin of
deletion").


### Examples

* starting point of action, e.g. movement

  <div class="ann-annotation">
  go from Otemachi to Jinbocho
  T1 PROCESS 0 2 go
  T2 LOCATION 7 16 Otemachi
  T3 LOCATION 20 28 Jinbocho
  R1 ORIGIN Arg1:T1 Arg2:T2
  R2 DESTINATION Arg1:T1 Arg2:T3
  </div>

* thing removed, deleted, etc. from

  <div class="ann-annotation">
  items are deleted from the logfile
  T1 DATA-ITEM 0 5 items
  T2 PROCESS 10 17 deleted
  T3 DATA-ITEM 27 34 logfile
  R1 OUT Arg1:T2 Arg2:T1
  R2 ORIGIN Arg1:T2 Arg2:T3
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