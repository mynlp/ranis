---
layout: base
title: 'English-Japanese scheme mapping'
---

# English-Japanese scheme mapping

These guidelines build in significant part on the previously introduced annotation guidelines for Japanese relation annotation [7]. However, a number of systematic differences have been introduced in the representation. Most notably, a larger number of specific span types is annotated for English, and the relation annotation scheme reverses the direction of a number of relations to improve consistency with some previously introduced annotation schemes. In the introduction of these changes to the scheme, care has been taken to make it possible to deterministically map annotations from the English to the Japanese scheme. This section details this mapping.

  Note: For convenience of reference, the content of this section is currently duplicated also in the definitions of individual span and relation annotation types. As it may be difficult to maintain the information consistently in two different locations, future revisions of this guideline may wish to remove one copy or the other.

## Span annotation mapping

The following simple mappings apply regardless of possible attributes, relations, etc.

* <a class="span" nolink>modality</a> → MEASURE
* <a class="span" nolink>quantity</a> → MEASURE
* <a class="span" nolink>language</a> → TERM
* <a class="span" nolink>plan</a> → TERM
* Relation trigger → ∅

The following mappings differ based on the presence or absence of the JUDGMENT flag.

* <a class="span" nolink>quality</a> + <a class="flag" nolink>judgment</a> → MEASURE
* <a class="span" nolink>quality</a> - <a class="flag" nolink>judgment</a> → TERM
* <a class="span" nolink>process</a> + <a class="flag" nolink>judgment</a> → MEASURE
* <a class="span" nolink>process</a> - <a class="flag" nolink>judgment</a> → TERM

The following mappings differ based on the presence or absence of the NAME flag. Note that for these
cases, if the annotation that is assigned the NAME flag is nested within another annotation of the same
type, the inner annotation is removed and the type assigned to the outer annotation.

<div class="ann-annotation">
Linux operating system → Linux operating system
T1 PLAN 0 5 Linux
T2 PLAN 0 22 Linux operating system
T3 OBJECT 25 47 Linux operating system
A1 Name T1
</div>

* <a class="span" nolink>person</a> + <a class="flag" nolink>name</a> → OBJECT
* <a class="span" nolink>person</a> - <a class="flag" nolink>name</a> → TERM
* <a class="span" nolink>organization</a> + <a class="flag" nolink>name</a> → OBJECT
* <a class="span" nolink>organization</a> - <a class="flag" nolink>name</a> → TERM
* <a class="span" nolink>data-item</a> + <a class="flag" nolink>name</a> → OBJECT
* <a class="span" nolink>data-item</a> - <a class="flag" nolink>name</a> → TERM
* <a class="span" nolink>artifact</a> + <a class="flag" nolink>name</a> → OBJECT
* <a class="span" nolink>artifact</a> - <a class="flag" nolink>name</a> → TERM
* <a class="span" nolink>location</a> + <a class="flag" nolink>name</a> → OBJECT
* <a class="span" nolink>location</a> - <a class="flag" nolink>name</a> → TERM

## Relation annotation mapping

The English relation annotation scheme is a largely direct adaptation of the Japanese scheme, with the most frequent changes simply reversing the direction of a number of relations. To map from the English relation annotation scheme presented in this guideline to the Japanese relation annotation scheme, apply the following.

The following simple mappings apply regardless of other annotations:

* <a class="relation" nolink>input</a>: reverse

  <div class="ann-annotation">
  A B [Eng] → A B [Jpn]
  T1 - 0 1 A
  T2 - 2 3 B
  T3 - 12 13 A
  T4 - 14 15 B
  R1 INPUT Arg1:T1 Arg2:T2
  R2 INPUT Arg1:T4 Arg2:T3
  </div>

* <a class="relation" nolink>output</a>: reverse

  <div class="ann-annotation">
  A B [Eng] → A B [Jpn]
  T1 - 0 1 A
  T2 - 2 3 B
  T3 - 12 13 A
  T4 - 14 15 B
  R1 OUTPUT Arg1:T1 Arg2:T2
  R2 OUTPUT Arg1:T4 Arg2:T3
  </div>

* <a class="relation" nolink>in-out</a>: reverse

  <div class="ann-annotation">
  A B [Eng] → A B [Jpn]
  T1 - 0 1 A
  T2 - 2 3 B
  T3 - 12 13 A
  T4 - 14 15 B
  R1 IN-OUT Arg1:T1 Arg2:T2
  R2 IN-OUT Arg1:T4 Arg2:T3
  </div>

* <a class="relation" nolink>origin</a>: reverse

  <div class="ann-annotation">
  A B [Eng] → A B [Jpn]
  T1 - 0 1 A
  T2 - 2 3 B
  T3 - 12 13 A
  T4 - 14 15 B
  R1 ORIGIN Arg1:T1 Arg2:T2
  R2 ORIGIN Arg1:T4 Arg2:T3
  </div>

* <a class="relation" nolink>destination</a>: reverse

  <div class="ann-annotation">
  A B [Eng] → A B [Jpn]
  T1 - 0 1 A
  T2 - 2 3 B
  T3 - 12 13 A
  T4 - 14 15 B
  R1 DESTINATION Arg1:T1 Arg2:T2
  R2 DESTINATION Arg1:T4 Arg2:T3
  </div>

* <a class="relation" nolink>agent</a>: reverse, change type

  <div class="ann-annotation">
  A B [Eng] → A B [Jpn]
  T1 - 0 1 A
  T2 - 2 3 B
  T3 - 12 13 A
  T4 - 14 15 B
  R1 AGENT Arg1:T1 Arg2:T2
  R2 PERFORM Arg1:T4 Arg2:T3
  </div>

* <a class="relation" nolink>target</a>: reverse

  <div class="ann-annotation">
  A B [Eng] → A B [Jpn]
  T1 - 0 1 A
  T2 - 2 3 B
  T3 - 12 13 A
  T4 - 14 15 B
  R1 TARGET Arg1:T1 Arg2:T2
  R2 TARGET Arg1:T4 Arg2:T3
  </div>

* <a class="relation" nolink>attribute</a>: reverse

  <div class="ann-annotation">
  A B [Eng] → A B [Jpn]
  T1 - 0 1 A
  T2 - 2 3 B
  T3 - 12 13 A
  T4 - 14 15 B
  R1 ATTRIBUTE Arg1:T1 Arg2:T2
  R2 ATTRIBUTE Arg1:T4 Arg2:T3
  </div>

* <a class="relation" nolink>condition</a>: reverse

  <div class="ann-annotation">
  A B [Eng] → A B [Jpn]
  T1 - 0 1 A
  T2 - 2 3 B
  T3 - 12 13 A
  T4 - 14 15 B
  R1 CONDITION Arg1:T1 Arg2:T2
  R2 CONDITION Arg1:T4 Arg2:T3
  </div>

* <a class="relation" nolink>coreference</a>: reverse, change type

  <div class="ann-annotation">
  A B [Eng] → A B [Jpn]
  T1 - 0 1 A
  T2 - 2 3 B
  T3 - 12 13 A
  T4 - 14 15 B
  R1 COREFERENCE Arg1:T1 Arg2:T2
  R2 EQUIVALENCE Arg1:T4 Arg2:T3
  </div>


Additionally, the following simple mappings differ based on the argument types or the presence or absence of particular flags:

* <a class="relation" nolink>attribute</a> for <a class="relation" nolink>modality</a>: change type

  <div class="ann-annotation">
  A B [Eng] → A B [Jpn]
  T1 - 0 1 A
  T2 MODALITY 2 3 B
  T3 - 12 13 A
  T4 - 14 15 B
  R1 ATTRIBUTE Arg1:T1 Arg2:T2
  R2 EVALUATE Arg1:T4 Arg2:T3
  </div>

* <a class="relation" nolink>attribute</a> with <a class="relation" nolink>judgment</a> flag: change type

  <div class="ann-annotation">
  A B [Eng] → A B [Jpn]
  T1 - 0 1 A
  T2 - 2 3 B
  T3 - 12 13 A
  T4 - 14 15 B
  A1 Judgment T2
  R1 ATTRIBUTE Arg1:T1 Arg2:T2
  R2 EVALUATE Arg1:T4 Arg2:T3
  </div>

