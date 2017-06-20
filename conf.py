#!/usr/bin/env python3

import sys
import os
import datetime


sys.path.append(os.path.abspath('.'))

project = 'Proces szkolenia astronautów do długotrwałych lotów i spacerów kosmicznych'
author = 'Matt Harasymczuk'

extensions = [
    'sphinx.ext.todo',
    'sphinxcontrib.bibtex',
]

todo_emit_warnings = False
todo_include_todos = True

language = 'pl'
master_doc = 'index'
today_fmt = '%Y-%m-%d'
source_suffix = ['.rst']

version = '1.0'
release = '1.0'

html_theme = 'thesis'
html_theme_path = ['_themes']
