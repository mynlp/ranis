---
layout: base
title: 'reference'
shortdef: 'anaphoric references'
---

## <a class="span" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Scope

The type <a class="span" nolink>reference</a> is used to mark
anaphoric expressions such as <q>it</q> that explicitly reference
previous expressions in scope of the annotation but are not (in their
immediate context) recognizable as referencing a particular semantic
class.


### Syntactic constraints

None.


### Examples

* <q>it</q>

  <div class="ann-annotation">
  the algorithm is well-known but it is not well understood
  T1 PLAN 4 13 algorithm
  T2 QUALITY 17 27 well-known
  T3 REFERENCE 32 34 it
  T4 MODALITY 38 41 not
  T5 QUALITY 42 46 well
  T6 PROCESS 47 57 understood
  </div>

* <q>that</q>

  <div class="ann-annotation">
  solve problems that arise in the evaluation
  T1 PROCESS 0 5 solve
  T2 PLAN 6 14 problems
  T3 REFERENCE 15 19 that
  T4 PROCESS 20 25 arise
  T5 PROCESS 33 43 evaluation 
  </div>

* <q>they</q>

  <div class="ann-annotation">
  words are indexed in a sentence where they are found
  T1 DATA-ITEM 0 5 words
  T2 PROCESS 9 17 indexed
  T3 DATA-ITEM 22 31 sentence
  T4 REFERENCE 32 37 where
  T5 REFERENCE 38 42 they
  T6 PROCESS 47 52 found 
  </div>

* <q>which</q>

  <div class="ann-annotation">
  a server which serves only one job at a time
  T1 PLAN-OR-PROCESS 2 8 server
  T2 REFERENCE 9 14 which
  T3 PROCESS 15 21 serves
  T4 QUALITY 22 26 only
  T5 QUANTITY 27 30 one
  T6 PLAN 31 34 job
  T7 QUALITY 35 44 at a time
  </div>

* <q>its</q>

  <div class="ann-annotation">
  evaluate the system and improve its performance
  T1 PROCESS 0 8 evaluate
  T2 PLAN 13 19 system
  T3 PROCESS 24 31 improve
  T4 REFERENCE 32 35 its
  T5 QUALITY 36 47 performance
  </div>

* <q>their</q>

  <div class="ann-annotation">
  representation of near-synonyms and their contexts
  T1 DATA-ITEM 0 14 representation
  T2 DATA-ITEM 18 31 near-synonyms
  T3 REFERENCE 36 41 their
  T4 DATA-ITEM 42 50 contexts 
  </div>

* <q>whose</q>

  <div class="ann-annotation">
  class of compound nouns whose head noun is derived from a verb
  T1 DATA-ITEM 0 5 class
  T2 DATA-ITEM 9 23 compound nowns
  T4 REFERENCE 24 29 whose
  T5 DATA-ITEM 30 39 head noun
  T6 PROCESS 43 50 derived
  T7 DATA-ITEM 58 62 verb
  </div>

* <q>she</q>

  <div class="ann-annotation">
  an user searches databases to find information he/she needs
  T1 PERSON 3 7 user
  T2 PROCESS 8 16 searches
  T3 DATA-ITEM 17 26 databases
  T4 PROCESS 30 34 find
  T5 DATA-ITEM 35 46 information
  T6 REFERENCE 47 49 he
  T7 REFERENCE 50 53 she
  T8 PROCESS 54 59 needs
  </div>



### Further details

Expressions such as <q>this system</q>, <q>that approach</q>, <q>these
results</q> and similar, where the immediate context of the
referencing expression identifies a semantic class, are not annotated
as <a class="span" nolink>reference</a> but rather with that
class. Additionally, pleonastic uses of potentially referencing
expressions (e.g. <q>it [is clear that]</q> are not annotated, nor are
referencing uses where the referent is out of the scope of the
annotation (e.g. <q>[in the conclusions] ... there</q>).


### References

See also <a class="relation">coreference</a> relation annotation
guidelines.
