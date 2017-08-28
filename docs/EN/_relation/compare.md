---
layout: base
title: 'compare'
shortdef: 'comparison between entities'
---

## <a class="relation" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Definition

Relation between quality and entity that does not hold that quality
but is contrasted with one that does in text.


### Examples

<div class="ann-annotation">
A is better than B
T1 -  0 1 A
T2 QUALITY 5 11 better
T3 -  17 18 B
R1 ATTRIBUTE Arg1:T1 Arg2:T2
R2 COMPARE Arg1:T3 Arg2:T2
</div>


### Argument types

Arg1: any entity

Arg2: QUALITY or QUANTITY or TIME


### Direction

From contrasted entity to quality.


### Further details


### References