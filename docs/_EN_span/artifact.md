---
layout: base
title: 'artifact'
shortdef: 'physical object intentionally produced for a purpose'
---

## <a class="span" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Scope

References to physical objects that have been intentionally produced
for a specific purpose are annotated as <a class="span"
nolink>artifact</a>, including collections and universals of such
objects. All criteria are required: entities that are non-physical,
not intentionally produced, or not produced for a specific purpose are
not in scope of <a class="span" nolink>artifact</a> annotation.


### Syntactic constraints

Names and nominal mentions (see Span annotation: [Name mention annotation](../span-annotation.html#name-mention-annotation) and [Nominal mention annotation](../span-annotation.html#nominal-mention-annotation))


### Examples

* <q>car</q>

  <div class="ann-annotation">
  drive a car
  T1 PROCESS 0 5 drive
  T2 ARTIFACT 8 11 car 
  </div>

* <q>sensor</q>

  <div class="ann-annotation">
  data from a single sensor
  T1 DATA-ITEM 0 4 data
  T2 QUANTITY 11 18 single 
  T3 ARTIFACT 19 25 sensor
  </div>

* <q>supercomputer</q>

  <div class="ann-annotation">
  ranking of supercomputers
  T1 DATA-ITEM 0 7 ranking
  T2 ARTIFACT 11 25 supercomputers
  </div>

* <q>sensor network</q>

  <div class="ann-annotation">
  queries in sensor networks
  T1 DATA-ITEM 0 7 queries
  T2 ARTIFACT 11 26 sensor networks
  </div>

* <q>UNIX workstation</q>

  <div class="ann-annotation">
  software for UNIX workstations
  T1 PLAN 0 8 software
  T2 PLAN 13 17 UNIX
  T3 ARTIFACT 13 30 UNIX workstations
  </div>

* <q>air-conditioner</q>

  <div class="ann-annotation">
  maintenance of an air-conditioner
  T1 PROCESS 0 11 maintenance
  T2 ARTIFACT 17 33 air-conditioner
  </div>

* <q>hardware</q>

  <div class="ann-annotation">
  hardware and software are fundamental for computer systems
  T1 ARTIFACT 0 8 hardware
  T2 PLAN 13 21 software
  T3 QUALITY 26 37 fundamental
  T4 ARTIFACT 42 50 computer
  T5 PLAN 42 58 computer systems
  </div>

* <q>Penicillin</q>

  <div class="ann-annotation">
  a possible penicillin for web spamming
  T1 QUALITY 2 10 possible
  T2 ARTIFACT 11 21 penicillin
  T3 PLAN-OR-PROCESS 26 38 web spamming
  </div>



### References

The semantic scope of <a class="span" nolink>artifact</a> annotations
is a subset of `object`_BFO (see Ontological basis: [Top-level organization](../ontological-basis.html#top-level-organization)).  Contrast information
artifacts <a class="span">data-item</a> and <a class="span">plan</a>.
