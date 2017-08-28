---
layout: base
title: 'member-collection'
shortdef: 'member part-of collection'
---

## <a class="relation" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Definition

Relation between a non-functional part of a collection and that collection.

### Examples

* <q>collection of images</q>

  <div class="ann-annotation">
  collection of images
  T1 DATA-ITEM 0 10 collection
  T2 DATA-ITEM 14 20 images
  R1 MEMBER-COLLECTION Arg1:T2 Arg2:T1
  </div>

* <q>articles in Wikipedia</q>

  <div class="ann-annotation">
  articles in Wikipedia
  T1 DATA-ITEM 0 8 articles
  T2 DATA-ITEM 11 21 Wikipedia
  R1 MEMBER-COLLECTION Arg1:T1 Arg2:T2
  </div>

* <q>collection of wireless devices</q>

  <div class="ann-annotation">
  collection of wireless devices
  T1 ARTIFACT 0 10 collection
  T2 ARTIFACT 14 30 wireless devices
  R1 MEMBER-COLLECTION Arg1:T2 Arg2:T1
  </div>

* <q>members of the community</q>

  <div class="ann-annotation">
  members of the community
  T1 PERSON 0 7 members
  T2 PERSON 14 24 community
  R1 MEMBER-COLLECTION Arg1:T1 Arg2:T2
  </div>

* <q>corpus of clinical text</q>

  <div class="ann-annotation">
  corpus of clinical text
  T1 DATA-ITEM 0 6 corpus
  T2 DATA-ITEM 10 23 clinical text
  R1 MEMBER-COLLECTION Arg1:T2 Arg2:T1
  </div>

* <q>set of labels</q>

  <div class="ann-annotation">
  set of labels
  T1 DATA-ITEM 0 3 set
  T2 DATA-ITEM 7 13 labels
  R1 MEMBER-COLLECTION Arg1:T2 Arg2:T1
  </div>

* <q>list of names</q>

  <div class="ann-annotation">
  list of names
  T1 DATA-ITEM 0 4 list
  T2 DATA-ITEM 8 13 names
  R1 MEMBER-COLLECTION Arg1:T2 Arg2:T1
  </div>

### Argument types

Arg1: <a class="span">artifact</a> or <a class="span">data-item</a> or <a class="span">process</a> or <a class="span">plan</a> or <a class="span">person</a> or <a class="span">intelligent-agent</a> or <a class="span">organization</a>

Arg2: same type as Arg1


### Direction

From member to collection.

### Further details

<a class="relation" nolink>member-collection</a> is understood to be distinguished from the related part-of relation <a class="relation">component-object</a> in that it is non-functional: the parts of a collection are not “in a specific spatial/temporal position with respect to each other which supports their functional role with respect to the whole.” [9].

### References

Contrast <a class="relation">component-object</a>, see also Section 8.4.