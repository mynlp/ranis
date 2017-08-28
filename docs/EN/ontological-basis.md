---
layout: base
title:  'Ontological basis'
---

# Ontological basis

This section briefly presents the ontological foundations of the
annotation and the relationship of the annotated types to the relevant
ontological categories.

The Basic Formal Ontology (BFO) [1] is used as the foundation for
organizing the span types defined for the annotation. BFO is a small
top-level ontology that has been broadly adopted in particular in
recent efforts to develop ontologies for science.

Additionally, for various types of entities relating specifically to
information entities, we base our definitions on the Information
Artifact Ontology (IAO) [2], originally a part of the Ontology for
Biomedical Investigations (OBI) [3, 4]. OBI and IAO are explicitly
based on BFO and thus compatible with its definitions.

## Top-level organization

BFO uses `entity` as its top-level term and divides it at the
uppermost level into *continuants* such as physical objects and
*occurrents* such as processes (relations are understood to constitute
a category distinct from entities). In the definition of the annotated
span types, this basic division as well as much of the upper-level
organization of BFO is followed, with a number of pragmatically
motivated differences. Most obviously, the annotation avoids the
technical BFO terms in favor of less precise but more readily
undersood labels, such as TIME instead of `temporal region`. Part of the
top-level structure of BFO is shown in the following with the relevant
related types applied in the annotation.

(Indentation represents *is-a* relations, ellipsis (...) signifies
omission of intervening structure. Only limited depth and detail
relevant to the present effort shown, e.g. omitting `spatiotemporal
region`_BFO , which is not used in the annotation.)

<table class="underline-th">
<tr>
  <th>Reference ontology</th>
  <th>Annotation</th>
</tr>
<tr>
  <td><code>occurrent</code></td>
  <td>-</td>
</tr>
<tr>
  <td class="indent1"><code>processual entity</code></td>
  <td><a class="span">process</a></td>
</tr>
<tr>
  <td class="indent1"><code>temporal region</code></td>
  <td><a class="span">time</a></td>
</tr>
<tr>
  <td><code>continuant</code></td>
  <td>-</td>
</tr>
<tr>
  <td class="indent1"><code>spatial region</code></td>
  <td><a class="span">location</a></td>
</tr>
<tr>
  <td class="indent1"><code>independent continuant</code></td>
  <td>-</td>
</tr>
<tr>
  <td class="indent2"><code>object</code></td>
  <td><a class="span">artifact</a>, <a class="span">person</a></td>
</tr>
<tr>
  <td class="indent1"><code>dependent continuant</code></td>
  <td>-</td>
</tr>
<tr>
  <td class="indent2"><code>... quality</code></td>
  <td><a class="span">quality</a></td>
</tr>
</table>

The definitions of the relevant BFO terms are provided below for
reference. Note that the (broadly) corresponding types applied in the
annotation differ from these definitions in some cases.

* `occurrent`: An entity that has temporal parts and that happens,
unfolds or develops through time.

* `processual entity`: An occurrent that exists in time by occurring or
happening, has temporal parts and always involves and depends on some
entity.

* `temporal region`: An occurrent that is part of time.

* `continuant`: An entity that exists in full at any time in which it
exists at all, persists through time while maintaining its identity
and has no temporal parts.

* `spatial region`: A continuant that is neither bearer of quality
entities nor inheres in any other entities. (Examples: the sum total
of all space in the universe, parts of the sum total of all space in
the universe)

* `independent continuant`: A continuant that is a bearer of quality and realizable entity entities, in which other entities inhere and which itself cannot inhere in anything.

* `object`: An independent continuant that is spatially extended, maximally self-connected and selfcontained [...] and possesses an internal unity. The identity of substantial object entities is independent of that of other entities and can be maintained through time.

* `dependent continuant`: A continuant that is either dependent on one or other independent continuant bearers or inheres in or is borne by other entities.

* `quality`: A specifically dependent continuant that is exhibited if it inheres in an entity or entities at all (a categorical property).

For further detail on BFO, refer to the literature on the topic [1];
for detailed definitions of the annotated types, refer to [Span annotation](span-annotation.html).

## Information entities

Information entities such as digital data are highly relevant in the
target domain of the annotation effort. The annotated types
corresponding to these entities are defined with reference to IAO
`information content entity`, which *is-a* `generically dependent
continuant`_BFO (see [Top-level organization](#top-level-organization)).  Part of the relevant structure of
IAO is shown in the following.

(As above, indentation represents *is-a* relations, ellipsis (...)
signifies omission of intervening structure, and only limited depth
and detail relevant to the present effort shown.)

<table class="underline-th">
<tr>
  <th>Reference ontology</th>
  <th>Annotation</th>
</tr>
<tr>
  <td><code>... dependent continuant</code></td>
  <td>-</td>
</tr>
<tr>
  <td class="indent1"><code>information content entity</code></td>
  <td>-</td>
</tr>
<tr>
  <td class="indent2"><code>data item</code></td>
  <td><a class="span">data-item</a></td>
</tr>
<tr>
  <td class="indent2"><code>textual entity</code></td>
  <td><a class="span">data-item</a></td>
</tr>
<tr>
  <td class="indent2"><code>directive information entity</code></td>
  <td><a class="span">plan</a></td>
</tr>
</table>

The definitions of the relevant IAO terms are provided below for reference.

* `information content entity`: an information content entity is an
entity that is generically dependent on some artifact and stands in
relation of aboutness to some entity. [IAO presently takes aboutness
(*is-about*) to be a primitive relation with no definition beyond
"relates an information artifact to an entity."]

* `data item`: a data item is an information content entity that is
intended to be a truthful statement about something (modulo, e.g.,
measurement precision or other systematic errors) and is
constructed/acquired by a method which reliably tends to produce
(approximately) truthful statements.

* `textual entity`: A textual entity is a part of a manifestation
[...], a generically dependent continuant whose concretizations are
patterns of glyphs intended to be interpreted as words, formulas,
etc. (Examples: Words, sentences, paragraphs, and the written
(non-figure) parts of publications are all textual entities)

* `directive information entity`: An information content entity whose
concretizations indicate to their bearer how to realize them in a
process.

The annotation simplifies substantially over the IAO definitions on
two points. First, no distinction is made between `data item`,
`textual entity`, or related terms such as `document`, `document
part`, and `symbol`; with all being typed <a class="span">data-item</a>.
Second, no distinction is made between subtypes of `directive
information entity`, marking e.g. `objective specification`, `plan
specification`, `source code module` and `data format specification`
as <a class="span">plan</a>.

## Other annotated types

In addition to the annotated entity types corresponding to upper-level
ontological categories ([Ontological basis](#top-level-organization)) and information entities ([Information entities](#information-entities)), a small number of other annotation types are defined to capture
specific phenomena in text. These are briefly presented below.

**References**: The types <a class="span">reference</a> and <a
class="span">external-reference</a> are defined to capture two
distinct but related categories of references to text, the former
within the document (e.g. anaphoric <q>it</q>) and the latter to other
documents (e.g. citations of other articles). These types are defined
only to support the representation of factual claims in annotated
documents and are not aligned with any ontological categories.

**QUANTITY**: The applied top-level ontology does not aim to account
for numbers. The annotation type <a class="span">quantity</a> is
defined to capture numbers and measurements.

**MODALITY**: Explicit statements regarding belief, probability and
similar, including explicitly negated statements (e.g. <q>not</q>) are
annotated as <a class="span">modality</a>. This type is not aligned
with any ontological categories.

**Rare types**: The annotation aims to associate the great majority of
all entities that the authors explicitly mention with a relevant type,
but does not aim for exhaustive coverage of all possible entities (see
[Ontological basis](ontological-basis.html#ontological-basis)). Mentions of entities that do not fall within any of the
defined categories are annotated with the "empty" type <a
class="span">other</a>. Specific types capturing rare entities that
are particularly relevant to a domain are defined in a data-driven
fashion. At the time of this writing, the following types have been
defined following this process: <a class="span">language</a>, <a
class="span">organization</a>, <a class="span">domain</a>, and <a
class="span">formula</a>. Refer to these sections for information on
these types.

## Ambiguous types

In addition to basic types broadly corresponding to ontological
categories, a few types explicitly representing ambiguities between
the basic types are defined.

The division between continuants and occurrents is fundamental to the
ontological basis of the annotated types. However, in natural language
the division between the two is not always clear, and, for many
practical uses of annotation, the distinction is not systematically
required. Consider, for example, the expression <q>web search</q>:
depending on context, this expression could refer to at least any of
the following: a specific process, a function (e.g. of a particular
software) that could be realized as such a process, a goal to be
achieved, or a set of steps for doing so. Such ambiguities persist in
statements such as <q>web search is inefficient</q> and <q>method M
improves web search performance</q>. However, resolution of this
ambiguity is not required to identify e.g. that the latter statement
expresses that <q>method M</q> has a positive effect on <q>web search</q>.

In the annotation, systematic ambiguity between expressions referring
to processes, entities that can be realized as such processes, and
information entities that indicate how to realize such processes is
captured without resolution with the type <a
class="span">plan-or-process</a>, which is used in cases where this
ambiguity occurs. In these cases, the annotation thus does not
systematically differentiate between continuants and occurrents, but
does preserve the closely related distinction between "static"
entities that cannot take processual participants and (potentially)
"dynamic" ones that can.

A second, considerably rarer systematic ambiguity occurs in some cases
between references to people, computational methods emulating
intelligent behaviour, and abstract, theoretical actors. For example,
in documents on game theory, authors may refer to <q>intelligent
agents</q> to intentionally abstract over human actors and others
exhibiting (arguably) intelligent behaviour. The annotation type <a
class="span">intelligent-agent</a> is defined to annotate references
where this ambiguity occurs.

## Individuals, collectives, and universals

The distinction between individuals (e.g. Barack Obama), collections
of individuals (e.g. members of congress) and universals (e.g. people)
is fundamental in many formal ontological descriptions of
reality. Individuals such as specific people are said to *instantiate*
(stand in the *instance-of* relation to) universals such as the human
species. Universals have multiple instances, while individuals have
none. These categories do not overlap and are clearly distinguishable.

However, in natural language, references to individuals, universals
and collectives are frequently ambiguous. While references to
e.g. <q>Barack Obama</q> clearly identify an individual person,
references to e.g. <q>Microsoft Windows</q> may, depending on context,
refer to a specific individual copy of the software, some particular
set of copies, or the universal constituted by all individual copies
of the software.

For the purposes of this annotation effort, the distinction between
individuals, collectives, and universals is ignored. Thus, for
example, <q>Barack Obama</q>, <q>congress members</q> and
<q>humans</q> are all annotated as <a class="span">person</a>.
