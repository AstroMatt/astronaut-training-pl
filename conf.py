#!/usr/bin/env python3
import datetime
import os
import re
import subprocess
import sys


sys.path.append(os.path.abspath('.'))

project = 'Proces szkolenia astronautów do długotrwałych lotów i spacerów kosmicznych'
author = 'Matt Harasymczuk'

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.imgmath',
    'sphinxcontrib.bibtex',
]

extensions_dir = os.path.join(os.path.dirname(__file__), '..', '_extensions')
sys.path.append(extensions_dir)

todo_emit_warnings = False
todo_include_todos = True

language = 'pl'
master_doc = 'index'
today_fmt = '%Y-%m-%d'
source_suffix = ['.rst']
imgmath_image_format = 'svg'

numfig = True
numfig_format = {
    'section': 'Rozd. %s',
    'figure': 'Ryc. %s',
    'table': 'Tab. %s',
    'code-block': 'List. %s',
}

version = '1.0'
release = '1.0'

html_theme = 'thesis'
html_theme_path = ['_themes']

# Fix for: LaTeX Backend Fails with Citations In Figure Captions
latex_elements = {
 'preamble': r'''
     \usepackage{etoolbox}
     \AtBeginEnvironment{figure}{\renewcommand{\phantomsection}{}}
 '''
}

exclude_patterns = ['not-used/*.rst']
