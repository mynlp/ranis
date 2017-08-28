---
layout: base
title: 'quantity'
shortdef: 'numbers and measurements'
---

## <a class="span" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Scope

Occurrences of numbers, exact and approximate magnitudes and
multitudes and measurements with or without specific units are
annotated as <a class="span" nolink>quantity</a>, with the exception
of numbers that are, in context, references to time (e.g. <q>1999</q>;
see <a class="span">time</a>).


### Syntactic constraints

None.


### Examples

* <q>two</q>

  <div class="ann-annotation">
  two evaluation metrics
  T1 QUANTITY 0 3 two
  T2 PLAN 4 22 evaluation metrics
  </div>

* <q>42</q>

  <div class="ann-annotation">
  42 databases
  T1 QUANTITY 0 2 42
  T2 DATA-ITEM 3 12 databases
  </div>

* <q>many</q>

  <div class="ann-annotation">
  many problems
  T1 QUANTITY 0 4 many
  T2 PLAN 5 13 problems
  </div>

* <q>several</q>

  <div class="ann-annotation">
  several researchers
  T1 QUANTITY 0 7 several
  T2 PERSON 8 19 researchers
  </div>

* <q>small number</q>

  <div class="ann-annotation">
  small number of topics
  T1 QUANTITY 0 12 small number
  T2 DATA-ITEM 16 22 topics
  </div>

* <q>almost 2000</q>

  <div class="ann-annotation">
  almost 2000 people's judgments
  T1 QUANTITY 0 11 almost 2000
  T2 PERSON 12 18 people
  T3 DATA-ITEM 21 30 judgments
  </div>

* <q>over 95%</q>

  <div class="ann-annotation">
  over 95% caliber estimation accuracy
  T1 QUANTITY 0 8 over 95%
  T2 DATA-ITEM 9 36 caliber estimation accuracy
  </div>

* <q>120 x 60 ft<sup>2</sup></q>

  <div class="ann-annotation">
  120 x 60 ft2 area
  T1 QUANTITY 0 12 120 x 60 ft2
  T2 LOCATION 13 17 area
  </div>



### References

See Ontological basis: [Other annotated types](../ontological-basis.html#other-annotated-types). Note exception <a class="span">time</a>.
