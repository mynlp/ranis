---
layout: base
title:  'Span annotation'
generated: 'true'
---

<ul>
{% for p in site.span %}
  <li><a href="{{ p.url | remove_first:'/' }}">{{ p.title }}</a>: {{ p.shortdef }}</li>
{% endfor %}
</ul>
