# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'ORBE.AI'
copyright = '2022, Orbe.AI'
author = 'Orbe.AI'

release = '1.0'
version = '1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.images'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]

html_logo = 'images/logo/logo_orbe.png'

html_theme_options = {
    'logo_only': True,
    'display_version': False
}

#html_context = {
#"display_github": False, # Add 'Edit on Github' link instead of 'View page source'
#"last_updated": False,
#"commit": False,
#}

# -- Options for EPUB output
# epub_show_urls = 'footnote'


