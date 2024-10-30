project = 'Vapor_Examples'
copyright = '2024, Ian'
author = 'Ian'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_nb',
    # other Sphinx extensions
]

# From geocat:
# extensions = [
#     'sphinx_gallery.gen_gallery',
#     'nbsphinx',
#     'sphinx_gallery.load_style',
#     "sphinx_design",
# ]



html_theme_options = {
    "logo": {
        "image_light": '_static/images/NSF_NCAR_light.svg',
        "image_dark": '_static/images/NSF_NCAR_dark.svg',
    }
}


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import sphinx_rtd_theme
html_theme = "sphinx_book_theme"
html_static_path = ['_static']


nb_execution_mode = "off"  # Options: "off", "auto", "force"
