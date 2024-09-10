# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import pathlib
import sys
from datetime import datetime

import toml
from sphinx_gallery.sorting import FileNameSortKey

sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())


# Info from poetry config:
info = toml.load("../../pyproject.toml")["tool"]["poetry"]

project = info["name"]
author = ", ".join(info["authors"])
release = info["version"]

copyright = (
    f"2023 - {datetime.now().year}, n-squared lab, FAU Erlangen-Nürnberg, Germany"
)

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
HERE = pathlib.Path(__file__).parent
with (HERE.parent.parent / "README.md").open() as f:
    out = f.read()

out = out.replace("docs/source/", "")

with (HERE / "README.md").open("w+") as f:
    f.write(out)


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx_gallery.gen_gallery",
    "rinoh.frontend.sphinx",
    "myst_parser",
]

# autosummary_generate = True
autoclass_content = "both"
autodoc_typehints = "description"

autosummary_generate = True
autosummary_generate_overwrite = True

add_function_parentheses = False


napoleon_numpy_docstring = True

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]

# -- Options for intersphinx extension ---------------------------------------
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference/", None),
    "matplotlib": ("https://matplotlib.org/stable/", None),
    "pandas": ("https://pandas.pydata.org/docs/", None),
    "sklearn": ("https://scikit-learn.org/stable/", None),
    "torch": ("https://pytorch.org/docs/stable/", None),
    "torchvision": ("https://pytorch.org/vision/stable/", None),
}

# -- Options for sphinx_gallery ----------------------------------------------
sphinx_gallery_conf = {
    "examples_dirs": "../../examples",  # path to your example scripts
    "gallery_dirs": "auto_examples",  # path to where to save gallery generated output
    "filename_pattern": r"\.py",
    "remove_config_comments": True,
    "only_warn_on_example_error": True,
    "show_memory": True,
    "within_subsection_order": FileNameSortKey,
}