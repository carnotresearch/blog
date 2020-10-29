# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os
import sys

import alabaster
import ablog


# -- Project information -----------------------------------------------------

project = 'Carnot Research Blog'
copyright = '2020-Present, Carnot Research Pvt. Ltd.'
author = 'Carnot Research Pvt. Ltd.'

version = ''
release = ''

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.extlinks',
    'ablog',
    'alabaster',
    'sphinx.ext.intersphinx',
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# ABLOG

templates_path = [ablog.get_html_templates_path()]

blog_title = 'Carnot Research Blog'
blog_baseurl = 'http://blog.carnotresearch.com'

blog_languages = {
    'en': ('English', None),
}
blog_default_language = 'en'

blog_feed_archives = True
blog_feed_fulltext = True

blog_feed_length = None

disqus_shortname = 'carnotresearch'
disqus_pages = False

html_style = 'alabaster.css'
html_theme = 'alabaster'

html_sidebars = {
   '**': ['postcard.html', 'recentposts.html',
          'tagcloud.html', 'categories.html',
          'archives.html', ]
}

html_theme_path = [alabaster.get_path()]
html_theme_options = {
    'travis_button': True,
    'github_user': 'carnotresearch',
    'description': 'Blog by Carnot Research',
}