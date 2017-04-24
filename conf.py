#!/usr/bin/env python3

import sys
import os
import datetime


sys.path.append(os.path.abspath('.'))

project = 'Proces szkolenia astronautów do długotrwałych lotów i spacerów kosmicznych'
author = 'Matt Harasymczuk'

extensions = [
    'sphinx.ext.todo',
]

language = 'pl'
copyright = '2012-{date:%Y}, Matt Harasymczuk <matt@astromatt.space>'.format(date=datetime.date.today())
master_doc = 'index'
today_fmt = '%Y-%m-%d'
source_suffix = ['.rst']

version = '1.0'
release = '1.0'

html_theme = 'sphinx_rtd_theme'
html_sidebars = {'sidebar': ['localtoc.html', 'sourcelink.html', 'searchbox.html']}
html_show_sphinx = False
htmlhelp_basename = 'Proces szkolenia astronautów do długotrwałych lotów i spacerów kosmicznych'
