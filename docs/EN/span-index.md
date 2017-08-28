---
layout: base
title:  'Span annotation'
generated: 'true'
---

<ul>
{% for p in site.EN_span %}
  <li><a href="..{{ p.url }}">{{ p.title }}</a>: {{ p.shortdef }}</li>
{% endfor %}
</ul>
