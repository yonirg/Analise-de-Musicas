import sphinx
import sphinx_rtd_theme

sphinx-quickstart

html_theme = "sphinx_rtd_theme"

html_last_updated_fmt = '%d %b %Y'

## caso queira utilizar data
from datetime import date
today_fmt = '%Y-%m-%d %H:%M'

## Data completa
str(date.today())

## Ano
str(date.today().year)

##Dia
str(date.today().day)
