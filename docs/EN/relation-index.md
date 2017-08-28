---
layout: base
title:  'Relation annotation'
generated: 'true'
---

<ul>
{% for p in site.relation %}
  <li><a href="{{ p.url | remove_first:'/' }}">{{ p.title }}</a>: {{ p.shortdef }}</li>
{% endfor %}
</ul>
