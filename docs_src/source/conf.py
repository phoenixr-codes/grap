# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'grap'
copyright = '2023, phoenixR'
author = 'phoenixR'
release = '0.1.0b1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx_copybutton",
    "sphinxcontrib.repl",
    "sphinxcontrib_trio",
    "sphinxemoji.sphinxemoji",
]

todo_include_todos = True
repl_mpl_disable = True

autodoc_default_options = dict.fromkeys('''
    members
    inherited-members
    undoc-members
    '''.split(),
    True
)
autodoc_typehints = 'description'
autoclass_content = 'both'

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

