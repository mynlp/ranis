---
layout: base
title:  'Span annotation'
---

# Span annotation

## General annotation guidelines

The following guidelines apply to span annotation in general, in
addition to the type-specific guidelines presented below. Note that
the syntactic guidelines relate primarily to the annotation for
continuants such as physical objects. For the annotation of processes,
qualities, and other non-continuant types, see the section for the
relevant type below.

### Name mention annotation

The following guidelines apply to the annotation of mentions of
(proper) names ("named entity annotation"). (see [NAME](flag/name.html))

**Specificity**: Name mention annotations mark spans that specifically identify the entity referred to.

**Structure**: Name mention annotations most typically mark sequences
of proper nouns constituting a name, but other fixed expressions that
are established as referring to specific entities are also annotated.
Name mention annotations can span any parts of speech that are part of
names (<q>United States of America</q>).

**Extent**: Name mention annotations cover the minimal span of
characters containing the name of the referenced entity. Words that
are not fixed parts of the name, including determiners (<q>[the]
NIST</q>), head nouns (<q>PTB [corpus]</q>; contrast <q>British National
Corpus</q>), modifiers (<q>[19th century] French</q>), and honorifics
(<q>[Prof.]  Charniak</q>), are not included in the name mention
annotation span, even if they further specify the referrent.

**Nesting**: Name mention annotations do not contain (nest) any other
annotations. In cases where multiple candidate name mention
annotations appear nested, only the outermost is marked.

### Nominal mention annotation

The following guidelines apply to the annotation of nominal mentions.

**Specificity**: Nominal mentions of entitites of types in annotation
scope are marked regardless of specificity.

**Structure**: Nominal mentions typically consist of a head noun with
adjective and noun premodifiers.  Determiners (<q>the</q>, <q>a</q>),
prepositional phrases (<q>of ...</q>, <q>with ...</q>), subordinate clauses
(<q>... that has ...</q>) and similar postmodififers are not normally
included in annotated spans. (Exceptions are allowed in cases where an
expression with such structure has become fixed and is necessary as a
whole for identifying the referrent.)

**Extent**: Nominal mention annotations cover the full span of
characters containing the most specific mention, excluding modifiers
not pertaining to type. Words referring to subjective aspects or
properties that pertain to e.g. an individual instance being discussed
rather than to its specific type (e.g. <q>[tall] person</q>) are excluded
from the span of the nominal annotation. (Note that e.g. <q>tall</q> for
<q>tall person</q> is annotated as a separate span with type 
<a class="span">quality</a> spans, associated with the annotation with
an <a class="rel">attribute</a> relation.)

**Nesting**: Nominal mention annotations contain (nest) any name
mention annotations that occur in their span. Nominal mention
annotations may also nest other nominal mention annotations according
to type-specific rules.

## Type-specific guidelines

<ul>
{% for p in site.EN_span %}
  <li><a class="span" href="..{{ p.url }}">{{ p.title }}</a>: {{ p.shortdef }}</li>
{% endfor %}
</ul>
