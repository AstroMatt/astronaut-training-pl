#!/usr/bin/env python3
import datetime


project = 'Analiza procesu selekcji, przygotowania do długotrwałych misji oraz treningu EVA w wybranych agencjach kosmicznych w celu zaproponowania programu szkolenia polskiego astronauty w kontekście przyszłych misji księżycowych'

html_context = {
    'university': 'Wyższa Szkoła Oficerska Sił Powietrznych',
    'faculty': 'Wydział Lotnictwa',
    'thesis': 'Praca Magisterska',
    'thesis_title': project,
    'author': 'Mateusz Harasymczuk<br>nr albumu 3094',
    'supervisor': 'prof. dr hab. inż. płk. rez. Marek Grzegorzewski',
    'proofreading': 'gen. bryg. pil. Mirosław Hermaszewski, kosmonauta Soyuz-30',
    'city': 'Dęblin',
    'year': '2019',
}

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.imgmath',
    'sphinx.ext.autosectionlabel',
    'sphinxcontrib.bibtex',
]

todo_emit_warnings = False
todo_include_todos = True

language = 'pl'
master_doc = 'index'
today_fmt = '%Y-%m-%d'
source_suffix = ['.rst']
imgmath_image_format = 'png'

numfig = True
numfig_format = {
    'section': 'Rozdz. %s',
    'figure': 'Ryc. %s',
    'table': 'Tab. %s',
    'code-block': 'List. %s',
}

version = '{now:%Y-%m-%d}'.format(now=datetime.datetime.now())
release = '{now:%Y-%m-%d}'.format(now=datetime.datetime.now())

html_theme = 'thesis'
html_theme_path = ['_themes']

# Fix for: LaTeX Backend Fails with Citations In Figure Captions
latex_elements = {
 'preamble': r'''
     \usepackage{etoolbox}
     \AtBeginEnvironment{figure}{\renewcommand{\phantomsection}{}}
 '''
}

exclude_patterns = [
    'not-used/*',
    'README.rst'
]
