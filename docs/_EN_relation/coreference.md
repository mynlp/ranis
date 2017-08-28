---
layout: base
title: 'coreference'
shortdef: 'coreferential mentions'
---

## <a class="relation" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Definition

Relation between two expressions referring to same entity. The <a class="relation" nolink>coreference</a> relation is used to annotate a limited subset of coreferential expressions where the reference to a previous expression is explicit (e.g. <q>it</q>, <q>this method</q>).

### Examples

<div class="ann-annotation">
</div>

### Argument types

Arg1: <a class="relation">reference</a> or referencing phrase (see Section 5.18)

Arg2: any


### Direction

From latter mention to former (see below).

### Further details

<a class="relation">coreference</a> relations are always annotated from the latter to the closest earlier referencing expression so that they form a reference chain. However, this structure should be understood only as an artifact of the applied annotation primitive: the underlying coreference relation is understood to be symmetric and transitive, so that any two annotations directly or indirectly connected by <a class="relation">coreference</a> annotations are taken to stand in the relation of coreference. The references connected by <a class="relation">coreference</a> annotation chains thus conceptually form equivalence classes defined by the referenced entities.