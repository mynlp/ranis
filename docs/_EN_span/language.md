---
layout: base
title: 'language'
shortdef: 'natural human language'
---

## <a class="span" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Scope

References to specific human languages, sets of human languages, and
human language in general is annotated are annotated as 
<a class="span" nolink>language</a>,
regardless of specificity. Artificial languages such as programming
languages as well as natural but (non-human) animal "languages" are
out of scope of <a class="span" nolink>language</a> annotation.


### Syntactic constraints

Names and nominal mentions (see Span annotation: [Name mention annotation](../span-annotation.html#name-mention-annotation) and [Nominal mention annotation](../span-annotation.html#nominal-mention-annotation))


### Examples

* <q>English</q>

  <div class="ann-annotation">
  machine translation system into English
  T1 PLAN 0 26 machine translation system
  T2 LANGUAGE 32 39 English
  </div>

* <q>Japanese</q>

  <div class="ann-annotation">
  Japanese word extraction task
  T1 LANGUAGE 0 8 Japanese
  T2 PLAN 0 29 Japanese word extraction task
  </div>

* <q>Arabic</q>

  <div class="ann-annotation">
  Arabic Wikipedia
  T1 LANGUAGE 0 6 Arabic
  T2 DATA-ITEM 0 16 Arabic Wikipedia
  </div>

* <q>natural language</q>

  <div class="ann-annotation">
  expressed in natural language
  T1 PROCESS 0 9 expressed
  T2 LANGUAGE 13 29 natural language
  </div>

* <q>Indian language</q>

  <div class="ann-annotation">
  interpretation of Indian language
  T1 PLAN 0 14 interpretation
  T2 LANGUAGE 18 33 Indian language
  </div>

* <q>polysynthetic languages</q>

  <div class="ann-annotation">
  parsing a polysynthetic languages
  T1 PROCESS 0 7 parsing
  T2 LANGUAGE 10 33 polysynthetic languages
  </div>

* <q>language pairs</q>

  <div class="ann-annotation">
  mapping for all language pairs
  T1 DATA-ITEM 0 7 mapping
  T2 LANGUAGE 15 30 language pairs
  </div>



### References

Contrast <a class="span">plan</a> (programming languages, data format
specifications, etc.)
