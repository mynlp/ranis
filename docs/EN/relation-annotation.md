---
layout: base
title:  'Relation annotation'
---

# Relation annotation

## General annotation guidelines

The following guidelines apply to relation annotations in general. Detailed, type-specific guidelines are presented in the sections below. Throughout the detailed guidelines, the expression “process or plan” is understood to refer to any of the types <a class="span">process</a>, <a class="span">plan</a> , or <a class="span">plan-or-process</a>.

### Scope

Relation annotation is sentence-based: with the exception of <a class="relation" nolink>coreference</a> annotations, all relation annotations associate annotations appearing in the same sentence. Additionally, only relations that are explicit from such local syntactic context are annotated (see [Explicit statements](annotation-scope.html#explicit-statements)).

### General structure

Taken broadly, the annotated relation structure is predicate-focused, with relations expressing participation in processes through statements involving verbal or nominalized expressions primarily structured around the verbs.

### Relation argument selection

In cases involving multiple references to the same entity, each of which could serve as the argument for an annotated relation, the reference that is syntactically closest to the expression stating the relation is selected. In particular, syntactically proximate anaphoric expressions (<a class="span" nolink>reference</a>, see [Span annotation](span/reference.html)) are selected over their syntactically more distant antecedents.
For example, in structures such as “corpus introduced by . . . , which is processed”, the <a class="span" nolink>reference</a> “which” rather than the <a class="span" nolink>data-item</a> “dataset” is marked as the <a class="relation" nolink>input</a> of “processing”.

## Type-specific guidelines

<ul>
{% for p in site.EN_relation %}
  <li><a class="relation" href="{{ p.url | remove_first:'/' }}">{{ p.title }}</a>: {{ p.shortdef }}</li>
{% endfor %}
</ul>
