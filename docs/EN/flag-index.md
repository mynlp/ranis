---
layout: base
title:  'Flag annotation'
generated: 'true'
---

<ul>
{% for p in site.flag %}
  <li><a href="{{ p.url | remove_first:'/' }}">{{ p.title }}</a>: {{ p.shortdef }}</li>
{% endfor %}
</ul>