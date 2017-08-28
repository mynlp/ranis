---
layout: base
title: 'input'
shortdef: 'input of process or plan'
---

## <a class="relation" nolink>{{ page.title }}</a>: {{ page.shortdef }}

### Definition

B is an input of process or plan A. A is not limited to concrete
processes and programs, but includes also abstract methods and
actions.

### Examples

<div class="ann-annotation">
extraction from document
T1 PROCESS 0 10 extraction
T2 DATA-ITEM 16 24 document
R1 INPUT Arg1:T1 Arg2:T2
</div>

### Argument types

Arg1: <a class="span" nolink>process</a> or <a class="span" nolink>plan</a>

Arg2: <a class="span" nolink>DATA-ITEM</a> or <a class="span" nolink>plan</a> or <a class="span" nolink>plan-or-process</a> or <a class="span" nolink>quality</a>

### Direction

From process or plan to its input.

### Further details

* Don’t confuse with the literal expression "input" (e.g. "input data
  of the system")

* The direction of this relation is reversed from that in the Japanese
  annotation.
