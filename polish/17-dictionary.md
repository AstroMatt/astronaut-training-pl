---
categories: appendix
language: polish
---

# Słownik Pojęć

<table id="dictionary">
{% for entry in site.data.dictionary %}
    <tr>
        <td class="abbr">{{ entry.word }}</td>
        <td class="definition">{{ entry.definition }}</td>
    </tr>
{% endfor %}
</table>
