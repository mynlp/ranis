---
layout: base
title: 'component-object'
shortdef: 'component part-of object'
---

## <a class="relation" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Definition

Relation between a functional part of a larger object and that
object. 

Note that "object" is here not limited to physical objects.  (To avoid
this potential source of confusion between OBJECT as understood in
e.g. BFO [1] and the "object" in the label it may be desirable to
rename the label, e.g. to COMPONENT-WHOLE following [6].)

### Examples

<div class="ann-annotation">
sensors of robot system
T1 ARTIFACT 0 7 sensors
T2 ARTIFACT 10 23 robot system
R1 COMPONENT-OBJECT Arg1:T2 Arg2:T1
</div>

<div class="ann-annotation">
queries with relevant morphemes
T1 DATA-ITEM 0 7 queries
T2 QUALITY 12 21 relevant
T3 DATA-ITEM 22 31 morphemes
R1 ATTRIBUTE Arg1:T3 Arg2:T2
R2 COMPONENT-OBJECT Arg1:T3 Arg2:T1
</div>

<div class="ann-annotation">
subtasks in the query estimation task
T1 PLAN 0 8 subtasks
T2 PLAN 16 37 query estimation task
R1 COMPONENT-OBJECT Arg1:T2 Arg2:T1 
</div>

### Argument types

Arg1: <a class="span" nolink>artifact</a> or <a class="span" nolink>data-item</a> or <a class="span" nolink>process</a> or <a class="span" nolink>plan</a> or <a class="span" nolink>intelligent-agent</a> or <a class="span" nolink>organization</a>

Arg2: <q>same type as Arg1</q>


### Direction

From member to collection

### Further details

<a class="relation" nolink>member-collection</a> is understood to be distinguished from the related part-of relation <a class="relation">component-object</a> in that it is <q>non-functional</q>: the parts of a collection are not “in a specific spatial/temporal position with respect to each other which supports their functional role with respect to the whole.” [9].

### References

Contrast <a class="relation">component-object</a>, see also Section 8.4.