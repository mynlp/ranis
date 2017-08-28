---
layout: base
title: 'location'
shortdef: 'any part of space'
---

## <a class="span" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Scope

References to points in space, one-, two- or three-dimensional regions
of space, and references to space as a whole are also are annotated as
<a class="span" nolink>location</a>. <a class="span"
nolink>location</a> annotation covers both exact and imprecise as well
as both absolute and relative references to space.


### Syntactic constraints

Names and nominal mentions (see Span annotation: [Name mention annotation](../span-annotation.html#name-mention-annotation) and [Nominal mention annotation](../span-annotation.html#nominal-mention-annotation)). Additionally,
prepositions relating to the boundaries of spatial regions such as
<q>above</q> are included in the extent of <a class="span"
nolink>location</a> annotations.


### Examples

* <q>US</q>

  <div class="ann-annotation">
  downloaded in the US
  T1 PROCESS 0 10 downloaded
  T2 LOCATION 18 20 US 
  </div>

* <q>US airspace</q>

  <div class="ann-annotation">
  flights over the US airspace
  T1 PROCES 0 7 flights
  T2 LOCATION 17 19 US
  T3 LOCATION 17 28  US airspace
  </div>

* <q>surroundings</q>

  <div class="ann-annotation">
  build a map of spectral utilization in their surroundings
  T1 PROCESS 0 5 build
  T2 DATA_ITEM 8 11 map
  T3 PROCESS 15 35 spectral utilization
  T4 REFERENCE 38 44 their
  T5 LOCATION 45 57 surroundings
  </div>

* <q>environment</q>

  <div class="ann-annotation">
  a method for sensor node localization in outdoor environments
  T1 PLAN 2 8 method
  T2 PLAN-OR-PROCESS 12 37 sensor node localization
  T3 LOCATION 40 61 outdoor environments
  </div>

* <q>urban areas</q>

  <div class="ann-annotation">
  car routing in dense urban areas
  T1 PLAN-OR-PROCESS 0 11 car routing
  T2 LOCATION 14 32 dense urban areas
  </div>

* <q>location</q>

  <div class="ann-annotation">
  information about the location of users
  T1 DATA-ITEM 0 11 information
  T2 LOCATION 21 30 location
  T3 PERSON 33 39 users 
  </div>

* <q>world</q>

  <div class="ann-annotation">
  people in the world
  T1 PERSON 0 6 people
  T2 LOCATION 14 19 world 
  </div>

* <q>space</q>

  <div class="ann-annotation">
  control the motion in space
  T1 PROCESS 0 7 control
  T2 PROCESS 11 18 motion
  T3 LOCATION 22 27 space 
  </div>


### References

The semantic scope of <a class="span" nolink>location</a> annotations
matches that of <a class="onto">spatial region<sub>BFO</sub></a> (see
Ontological basis: [Top-level organization](../ontological-basis.html#top-level-organization)). In terms of "classical" named entity recognition tasks,
the semantic scope of <a class="span" nolink>location</a> encompasses
the scope of LOC(ation) and overlaps significantly with GPE
(Geo-Political Entity) [5].
