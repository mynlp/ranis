---
layout: base
title: 'formula'
shortdef: 'mathematical formula'
---

## <a class="span" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Scope

Any mathematical formula appearing in text is annotated as <a
class="span" nolink>formula</a>. Non-mathematical (e.g. chemical)
formulas are *not* in scope of <a class="span" nolink>formula</a>
annotation.


### Syntactic constraints

None. <a class="span" nolink>formula</a> annotations may consist of
only non-alphabetic symbols and numbers.


### Examples

* <q>y = 0</q>

  <div class="ann-annotation">
  y = 0
  T1 FORMULA 0 5 y = 0
  </div>

* <q>m > 1</q>

  <div class="ann-annotation">
  m > 1
  T1 FORMULA 0 5 m > 1
  </div>

* <q>O(&#8730;N)</q>

  <div class="ann-annotation">
  O(√N)
  T1 FORMULA 0 5 O(√N)
  </div>

* <q>p < 0.0001</q>

  <div class="ann-annotation">
  p < 0.0001
  T1 FORMULA 0 10 p < 0.0001
  </div>

* <q>F<sub>1</sub> = 76.59</q>

  <div class="ann-annotation">
  F1 = 76.59
  T1 FORMULA 0 10 F1 = 76.59
  </div>



### Further details

Note that expressions with natural language (as opposed to
mathematical) syntax such as <q>the value of F<sub>1</sub> is 90</q>
are not annotated as <a class="span" nolink>formula</a> even if their
meaning is identical to that of some similar formula
(e.g. <q>F<sub>1</sub> = 90</q>).

