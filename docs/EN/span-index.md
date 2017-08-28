---
layout: base
title:  'Span annotation'
generated: 'true'
---

<ul>
{% for p in site.EN_span %}
  <li><a href="{{ p.url | remove_first:'/' }}">{{ p.title }}</a>: {{ p.shortdef }}</li>
{% endfor %}
</ul>
