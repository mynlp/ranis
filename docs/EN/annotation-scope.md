---
layout: base
title:  'Annotation scope'
---

# Annotation scope

The scope of the annotation is defined as follows.

## Explicit statements

The applied annotation scheme requires each annotation to be
associated with a specific span of text, either directly (span
annotations) or indirectly through other annotations that it refers to
(relation annotations and flags). Further, the annotation only targets
explicit statements in text. Only mentions of objects, processes and
other entities that are explicitly referred to in text are annotated
as spans, and only those relations between these entities that are
explicit from the text are annotated. 

Annotators are expected to apply world knowledge to interpret the
authors' intention and to determine the types of annotations, but not
to introduce annotations without an explicit basis in text. For
example, background knowledge allows an annotator to mark the mention
<q>Barack Obama</q> as <a class="span" nolink>person</a> even if the text
does not identify this category, but, by contrast, a document that
discusses <q>Barack Obama</q> and <q>Michelle Obama</q> without explicit
reference to their relationship would not be marked with a
(hypothetical) <a class="rel" nolink>spouse</a> relation even if the
annotator knows that such a relationship holds true in the world.

## Internal and external

A manuscript can be thought of as involving two "levels" of reality:
that of the authors and the manuscript itself (e.g. <q>in this paper,
we first ...</q>) and the world as described in the manuscript
(e.g. ´<q>method A outperforms method B</q>). Here, concepts relating to
the former are termed external (to the manuscript) and those relating
to the latter internal.

The aim of the annotation is to capture claims that authors make
regarding the world. By contrast, statements relating only to the
manuscript and its authors (in their role as authors) are not relevant
to the annotation. Correspondingly, references to the manuscript (<q>in
this paper</q>, <q>here</q>), references to the authors as authors (<q>we
[present]</q>, <q>we [introduce]</q>), statements regarding the structure
of the manuscript (<q>first, ... then, ... finally</q>) are considered
out of scope of the annotation. By contrast, references to approaches,
systems, programs, processes, etc. that exist independently of the
manuscript are in scope of the annotation, even if first defined or
presented in the manuscript.

## Future work

Statements referring to work that is merely planned, as opposed to at
least partially performed, is considered to be out of scope and no
annotations are created in text presenting plans for such future work.
