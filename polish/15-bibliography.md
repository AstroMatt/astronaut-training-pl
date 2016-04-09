---
categories: appendix
---

# Bibliografia

<table id="bibliography">
{% for entry in site.data.bibliography %}
    <tr>
        {% assign title = entry.title %}
        <td>{% bibliography title %}</td>
        <td>{{ entry.author }}, <i>{{ entry.title }}</i>, {{ entry.publisher }}, {{ entry.date }}</td>
    </tr>
{% endfor %}
</table>
