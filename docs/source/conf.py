# Configuration file for the Sphinx documentation builder.

import os
import sys

# Add the project root to sys.path to allow autodoc to find configflow
sys.path.insert(0, os.path.abspath('../..'))

# Project information
project = 'ConfigFlow'
copyright = '2025, Your Name'
author = 'Your Name'
release = '0.1.0'

# General configuration
extensions = [
    'sphinx.ext.autodoc',  # Auto-generate docs from docstrings
    'sphinx.ext.napoleon',  # Support Google-style docstrings
    'myst_parser',  # Support Markdown files
]

templates_path = ['_templates']
exclude_patterns = []

# HTML output
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_static/logo.png'  # Optional: Add a logo later
html_favicon = '_static/favicon.ico'  # Optional: Add a favicon later

# Include Markdown support
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Autodoc settings
autodoc_member_order = 'bysource'
autoclass_content = 'both'