---
layout: base
title: 'Specific annotation guidelines'
---

# Specific annotation guidelines

This section collects detailed guidelines pertaining to distinctions and decision points found to be challenging during annotation. It is intended to be used primarily as a reference to consult to resolve particular issues rather than for reading through as a whole.

## <a class="span" nolink>data-item</a> vs. <a class="span" nolink>quality</a>

There is a systematic potential ambiguity for qualities that can be measured and represented as data. For example, while reference to the weight of a person is in general be annotated as <a class="span" nolink>quality</a> , the “weight” datum representing the result of measuring that quality is annotated as <a class="span" nolink>data-item</a>.

The decision between annotating <a class="span" nolink>data-item</a> or <a class="span" nolink>quality</a> is based on the context of each mention (rather than e.g. its surface form). In difficult cases permitting either reading, the type <a class="span" nolink>data-item</a> is preferred over the more generic <a class="span" nolink>quality</a>.

## <a class="span" nolink>data-item</a> vs. <a class="span" nolink>plan</a>

Mentions of metrics (e.g. <q>TFIDF</q>) are annotated as PLAN when understood as referring to methods for calculating a value, and as <a class="span" nolink>data-item</a> when understood as referring to those values themselves (see <a class="span">plan</a>).

## <a class="span" nolink>artifact</a> vs. <a class="span" nolink>plan</a>

References to systems explicitly presented as involving both hardware and software components (as opposed to software only implicitly executed by hardware) could arguably be annotated both as <a class="span">artifact</a> or <a class="span">plan</a>. These cases are resolved according to context: if the composite is discussed as a passive, physical object, the <a class="span" nolink>artifact</a> type is applied; if its behaviour is discussed in any way, <a class="span" nolink>plan</a> is assigned.

## Classes and neutral collections
Many words referring to collections of individual entities are neutral in the sense that they can be used with (almost) any entity type (consider e.g. <q>set</q> (neutral) vs. <q>crowd</q> (non-neutral)). Separated from context, it would not be possible to determine what type to assign to such expressions. However, in context, these expressions are assigned with the same type as the entities that are members of the collection: the annotation does not differentiate between individuals and collectives ([Individuals, collectives, and universals](ontological-basis.html#individuals-collectives-and-universals)).

## <a class="relation" nolink>apply-to</a> vs. <a class="relation" nolink>input</a>

In expressions such as <q>method using X</q> and <q>method based on X</q>, the relation between <q>method</q> and <q>X</q> is annotated either as <a class="relation" nolink>apply-to</a> or <a class="relation" nolink>input</a> depending on what <q>X</q> is. If <q>X</q> is static data (<a class="span" nolink>data-item</a> or similar) <a class="relation" nolink>input</a> is used; if it is a method, approach or similar, <a class="relation" nolink>apply-to</a> is used. (See <a class="relation">apply-to</a>; <a class="relation">input</a>)

## <a class="relation" nolink>attribute</a> vs. <a class="relation" nolink>condition</a>

Expressions such as <q>document in English</q> are annotated with the <a class="relation" nolink>attribute</a> relation type:

<div class="ann-annotation">
document English
T1 - 0 8 document
T2 - 9 16 English
R1 ATTRIBUTE Arg1:T1 Arg2:T2
</div>

