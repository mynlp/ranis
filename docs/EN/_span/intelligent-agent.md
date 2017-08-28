---
layout: base
title: 'intelligent-agent'
shortdef: 'human or other intelligent agent'
---

## <a class="span" nolink>{{ page.title }}</a>: {{ page.shortdef }}


### Scope

References that include in their scope humans as well as other
intelligent agents (whether computational, abstract, or merely
hypothetical) are annotated as 
<a class="span" nolink>intelligent-agent</a>, including references
to agent individuals, groups, and universals.


### Syntactic constraints

Following <a class="span">person</a> and <a class="span">plan</a>
constraints.


### Examples

* <q>agent</q>

  <div class="ann-annotation">
  bilateral multi-issue negotiation between self-interested autonomous agents
  T1 PLAN-OR-PROCESS 0 33 bilateral multi-issue negotiation
  T2 INTELLIGENT-AGENT 42 75 self-interested autonomous agents 
  </div>

* <q>learners</q>

  <div class="ann-annotation">
  datasets defined for learners in the system
  T1 DATA-ITEM 0 8 datasets
  T2 PROCESS 9 16 defined
  T3 INTELLIGENT-AGENT 21 29 learners
  T4 PLAN 37 43 system 
  </div>

* <q>mediator</q>

  <div class="ann-annotation">
  the mediator determines the values
  T1 INTELLIGENT-AGENT 4 12 mediator
  T2 PROCESS 13 23 determines
  T3 DATA-ITEM 28 34 values 
  </div>

* <q>opponent</q>

  <div class="ann-annotation">
  players learn which queries their opponents made
  T1 INTELLIGENT-AGENT 0 7 players
  T2 PROCESS 8 13 learn
  T3 DATA-ITEM 20 27 queries
  T4 REFERENCE 28 33 their
  T5 INTELLIGENT-AGENT 34 43 opponents
  T6 PROCESS 44 48 made
  </div>

* <q>traders</q>

  <div class="ann-annotation">
  constraints on the offers traders express through bids
  T1 PLAN 0 11 constraints
  T2 DATA-ITEM 19 25 offers
  T3 INTELLIGENT-AGENT 26 33 traders
  T4 PROCESS 34 41 express
  T5 DATA-ITEM 50 54 bids
  </div>

* <q>committee</q>

  <div class="ann-annotation">
  argumentation among committees of agents
  T1 PLAN-OR-PROCESS 0 13 argumentation
  T2 INTELLIGENT-AGENT 20 30 committees
  T3 INTELLIGENT-AGENT 34 40 agents
  </div>

* <q>teams</q>

  <div class="ann-annotation">
  model temporal properties of agents and their teams
  T1 PROCESS 0 5 model
  T2 QUALITY 6 25 temporal
  T3 INTELLIGENT-AGENT 29 35 agents
  T4 REFERENCE 40 45 their
  T5 INTELLIGENT-AGENT 46 51 teams
  </div>



### Further details

<a class="span" nolink>intelligent-agent</a> annotation requires the
annotated mention to involve actual ambiguity between the <a
class="span">person</a> and <a class="span">plan</a> types, most
typically arising from authors' intentional use of terms that are
ambiguous between the two. Mentions that can only be understood as
referring to people are instead annotated as <a
class="span">person</a>, and mentions that can only be understood as
referring to software are instead annotated as <a
class="span">plan</a>, regardless of claimed level of intelligence.


### References

See [Ontological basis](../ontological-basis.html#ambiguous-types) for more information on ambiguous types. Contrast <a
class="span">person</a>, <a class="span">plan</a>.
