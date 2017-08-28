---
layout: base
title:  'Flag annotation'
---

# Flag annotation

## General annotation guidelines

## Type-specific guidelines

<ul>
{% for p in site.EN_flag %}
  <li><a class="flag" href="{{ p.url | remove_first:'/' }}">{{ p.title }}</a>: {{ p.shortdef }}</li>
{% endfor %}
</ul>
