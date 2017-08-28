---
layout: base
title: 'modality'
shortdef: 'probability and negation'
---

## <a class="span" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Scope

Expressions regarding the probability of propositions being true,
including expressions of negation and speculation, are annotated as 
<a class="span" nolink>modality</a>.


### Syntactic constraints

Modal verbs (<q>can</q>, <q>may</q>, <q>must</q>), words similarly
expressing ability, necessity, likelihood, etc., (<q>able</q>,
<q>need</q>, <q>likely</q>), words expressing negation (<q>not</q>,
<q>without</q>) or absence (<q>lack</q>), and multiword expressions
with these meanings (<q>had better</q>).


### Examples

* <q>can</q>

  <div class="ann-annotation">
  rules can be represented
  T1 PLAN 0 5 rules
  T2 MODALITY 6 9 can
  T3 PROCESS 13 24 represented
  </div>

* <q>not</q>

  <div class="ann-annotation">
  data not found
  T1 DATA-ITEM 0 4 data
  T2 MODALITY 5 8 not
  T3 PROCESS 9 14 found
  </div>

* <q>cannot</q>

  <div class="ann-annotation">
  cross-validation cannot be performed
  T1 PLAN 0 16 cross-validation
  T2 MODALITY 17 23 cannot
  T3 PROCESS 27 36 performed
  </div>

* <q>may</q>

  <div class="ann-annotation">
  performance may be achieved
  T1 QUALITY 0 11 performance
  T2 MODALITY 12 15 may
  T3 PROCESS 18 27 achieved
  </div>

* <q>might</q>

  <div class="ann-annotation">
  services might interest users
  T1 PLAN 0 8 services
  T2 MODALITY 9 14 might
  T3 PROCESS 15 23 interest
  T4 PERSON 24 29 users
  </div>

* <q>should</q>

  <div class="ann-annotation">
  bidders should calculate their bids
  T1 PERSON 0 7 bidders
  T2 MODALITY 8 14 should
  T3 PROCESS 15 24 calculate
  T4 REFERENCE 25 30 their
  T5 DATA-ITEM 31 35 bids
  </div>

* <q>without</q>

  <div class="ann-annotation">
  text data without syntactic annotation
  T1 DATA-ITEM 0 9 text data
  T2 MODALITY 10 17 without
  T3 DATA-ITEM 18 38 syntactic annotation
  </div>

* <q>possible</q>

  <div class="ann-annotation">
  possible to automatically construct
  T1 MODALITY 0 8 possible
  T2 QUALITY 11 25 automatically
  T3 PROCESS 26 35 construct
  </div>



### Further details

Multiple consecutive modality-expressing words whose joint meaning is
straightforwardly compositional (e.g. <q>may not</q>) are marked with
separate <a class="span" nolink>modality</a> annotations instead of
one, but single words such as <q>cannot</q> are marked with at most a
single <a class="span" nolink>modality</a> annotation. The word
<q>will</q> is annotated as <a class="span" nolink>modality</a> when
used to express likelihood but not when used to mark future tense.
