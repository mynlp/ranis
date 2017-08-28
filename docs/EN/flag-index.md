---
layout: base
title:  'Flag annotation'
generated: 'true'
---

<ul>
{% for p in site.EN_flag %}
  <li><a href="..{{ p.url }}">{{ p.title }}</a>: {{ p.shortdef }}</li>
{% endfor %}
</ul>
