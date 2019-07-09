from datetime import datetime

import sphinx_rtd_theme

TODAY = datetime.today()

name = "tox plugin cookiecutter"
copyright = f"2018-{TODAY.year}"
version = "1.0.0"

extensions = []

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
    "canonical_url": "",
    "logo_only": False,
    "display_version": False,
    "prev_next_buttons_location": "bottom",
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 6,
    "includehidden": True,
}
html_last_updated_fmt = TODAY.isoformat()
