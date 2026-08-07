from datetime import UTC, datetime

# 1. Basic Project Info
project = "funcy-pipe"
copyright = f"{datetime.now(UTC).year}, Michael Bianco"
author = "Michael Bianco"

# 2. Extensions
# AutoAPI is the sole API generator (AST-based; avoids importing patched modules).
# autodoc/napoleon/autodoc-typehints/paramlinks are intentionally omitted.
extensions = [
    "myst_parser",  # Enable Markdown
    "sphinx_design",  # UI Components (Grids/Cards)
    "sphinx_copybutton",  # Code copy button
    "sphinx.ext.viewcode",  # View source code
    "sphinx.ext.intersphinx",  # Link to external docs
    "autoapi.extension",  # Auto-generate API reference
    "sphinx_llm.txt",  # LLM-friendly documentation (llms.txt / llms-full.txt)
]

# Configure AutoAPI
autoapi_dirs = ["../funcy_pipe"]
autoapi_type = "python"
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
]
autoapi_keep_files = False

exclude_patterns = [
    "_build",
]

# Intersphinx configuration
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}
intersphinx_timeout = 10

# sphinx-llm runs a nested markdown build; keep it sequential for clearer errors
llms_txt_build_parallel = False

# 3. Markdown Support Configuration
source_suffix = {
    ".md": "markdown",
    # AutoAPI generates temporary reStructuredText sources during the build.
    ".rst": "restructuredtext",
}

myst_enable_extensions = [
    "colon_fence",  # Use ::: for directives (much cleaner MD)
    "deflist",  # Support for definition lists
    "substitution",  # Use {{ variables }} in Markdown
    "tasklist",  # Enable GitHub-style checkboxes
    "attrs_block",  # CSS classes directly in markdown
    "attrs_inline",  # CSS classes inline
    "smartquotes",  # Typographic curly quotes
]

# Support heading anchors in MyST for README includes
myst_heading_anchors = 3

# 4. Theme & Appearance (Shibuya)
html_theme = "shibuya"
html_baseurl = "https://iloveitaly.github.io/funcy-pipe/"
html_static_path = ["_static"]
html_extra_path = [".nojekyll"]
html_css_files = ["custom.css"]

html_theme_options = {
    "accent_color": "blue",
    "github_url": "https://github.com/iloveitaly/funcy-pipe",
    "nav_links": [
        {"title": "API Reference", "url": "autoapi/funcy_pipe/index"},
    ],
}

# 5. sphinx-llm: publish machine-readable docs alongside HTML
llms_txt_enabled = True
llms_txt_full_build = True
llms_txt_description = (
    "funcy-pipe: Funcy methods with Pipe-style operators for chainable "
    "Python data transformation."
)
