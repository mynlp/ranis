---
layout: base
title:  'Representation'
---

# Representation

The annotation uses two primary annotation primitives: typed text
*spans* and typed binary *relations*.  Additionally, a third
primitive, annotation *flags*, are used to identify additional aspects
of other annotations. These abstract categories of annotation are
briefly defined below.

## Span annotations

Span annotations mark a specific sequence of characters in the text of
a single document and associate it with exactly one type. For example,
a span annotation could mark <q>Barack Obama</q> and associate it with
the type <a class="span">person</a>. 

<div class="ann-annotation">
Barack Obama
T1 PERSON 0 12 Barack Obama
</div>

Span annotations typically mark continuous sequences of characters,
but can also be discontinuous in cases where the relevant expression
is split in the source text. The most frequent source of discontinuity
are coordinations, for example the span <q>Barack Obama</q> in <q>Barack
and Michelle Obama</q>. 

<div class="ann-annotation">
Barack and Michelle Obama
T1 PERSON 0 6;20 25 Barack Obama
</div>

The set of span types applied in the annotation and their definitions
are given in [Span annotation](span-annotation.html).

## Relation annotations

Relation annotations are binary and directed, hold between span
annotations, and are each associated with exactly one type. For
example, the relation A−KNOWS→B could be used to mark the <a
class="rel" nolink>knows</a> relation between annotations A and B,
which could in turn be span annotations of type <a class="span"
nolink>person</a>.  

<div class="ann-annotation">
Obama selected Biden as his running mate
T1 PERSON 0 5 Obama
T2 PERSON 15 20 Biden
R1 KNOWS Arg1:T1 Arg2:T2
</div>

The applied representation only involves directed relations and does
not constrain their properties (symmetry, transitivity, etc.). The
underlying semantic relationships that the relations denote may be
understood to be e.g. symmetric (A−R→B implies B−R→A). Please refer to
the relation definitions for detailed specification of such
properties. The set of relation types applied in the annotation and
their definitions are given in [Relation annotation](relation-annotation.html).

## Flag annotation

Flag annotations are simple binary values associated with a single
annotation each. For example, the annotation of type <a class="span"
nolink>person</a> marking the span <q>Barack Obama</q> could be
assigned the flag <a class="flag" nolink>name</a> to identify that it
is the mention of the name of a person. 

<div class="ann-annotation">
Barack Obama
T1 PERSON 0 12 Barack Obama
A1 Name T1
</div>

The set of flag types applied in the annotation and their definitions
are given in [Flag annotation](flag-annotation.html).

(Note that flag annotations are termed "attribute annotations" in some
related materials. This arguably more readily understood term is
avoided here to minimize the risk of confusion with the relation type
<a class="flag">attribute</a>.)
