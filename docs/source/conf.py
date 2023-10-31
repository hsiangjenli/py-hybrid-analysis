import sys; sys.path.insert(0, "..")
import datetime
import pyhybridanalysis

print(pyhybridanalysis)

# -- Project information -----------------------------------------------------
author = "Hsiang-Jen Li"
project = "pyHybridAnalysis"

version = "0.0.0"
copyright = f"{datetime.datetime.now().year}, {author}"

# -- Theme configuration -----------------------------------------------------
html_theme = 'furo'
html_title = "<br>pyHA"
html_static_path = ["_static"]
suppress_warnings = ['autodoc.import_object']

intersphinx_mapping = {
    'python': ('https://docs.python.org/', None),
    'numpy': ('http://docs.scipy.org/doc/numpy', None),
    'pandas': ('http://pandas.pydata.org/pandas-docs/dev', None),
}

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'nbsphinx',
]

def setup(app):
    def rst_jinja_render(app, _, source):
        rst_context = {"pyhybridanalysis": pyhybridanalysis}
        source[0] = app.builder.templates.render_string(source[0], rst_context)

    app.connect('source-read', rst_jinja_render)