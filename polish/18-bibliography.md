---
categories: appendix
language: polish
---

# Bibliografia

<table id="bibliography">

{% for entry in site.data.bibliography %}
    <tr>
        <td>[{{ entry.title }}]</td>
        <td>{{ entry.author }}, <i>{{ entry.title }}</i>, {{ entry.publisher }}, {{ entry.date }}</td>
    </tr>
{% endfor %}
</table>
