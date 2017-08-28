---
layout: base
title:  'Relation annotation'
generated: 'true'
---

<ul>
{% for p in site.EN_relation %}
  <li><a href="{{ p.url | remove_first:'/' }}">{{ p.title }}</a>: {{ p.shortdef }}</li>
{% endfor %}
</ul>
