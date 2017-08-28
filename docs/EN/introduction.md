---
layout: base
title:  'Introduction'
---

# Introduction

This document presents the English entity and relation annotation
guidelines for the NII English relations corpus. These guidelines
build in significant part on the previously developed annotation
guidelines for Japanese relation annotation [7, 8].

This document is structured as follows. First, the representation
applied in the annotation is introduced in [Representation](representation.html), defining the
basic annotation primitives used in the effort. Then, the general
guidelines determining the scope of the annotation are presented in
[Annotation scope](annotation-scope.html). The ontological basis of the annotation scheme and an
overview of the defined annotated types is then given in [Ontological basis](ontological-basis.html).
Finally, the detailed guidelines for each of the annotation types
defined for the three annotation primitives are presented in [Span annotation](span-annotation.html), [Relation annotation](relation-annotation.html), and [Flag annotation](flag-annotation.html) sections.

## Conventions

The following conventions are followed in this document.

* **example text**: <q>quoted italic font</q>
* **span type**: <a class="span" nolink>small capital font</a>
* **relation type**: <a class="rel" nolink>bold small capital font</a>
* **flag type**: <a class="flag" nolink>bold small capital font</a>
* **relation (A, B)**:

  <div class="ann-annotation">
  A B
  T1 - 0 1 A
  T2 - 2 3 B
  R1 RELATION Arg1:T1 Arg2:T2
  </div>

* **ontology term**: `fixed width font`
* **ontology term_ontology**: `fixed width font`_subscript (TODO)
