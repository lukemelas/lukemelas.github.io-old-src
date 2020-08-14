#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Luke Melas-Kyriazi'
SITENAME = "Luke Melas-Kyriazi"
SITEURL = '' 

MY_SITEURL = 'lukemelas.github.io'

PATH = 'content'

STATIC_PATHS = ['assets', 'assets/icons/favicon.ico']

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

DEFAULT_DATE_FORMAT = "%A %d %B %Y"

EXTRA_PATH_METADATA = {
    'assets/icons/favicon.ico': {'path': 'favicon.ico'}
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# # Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python', 'http://python.org/'),
#          ('Github', 'http://github.com/'),)

# Colors (for code?)
COLOR_SCHEME_CSS = 'monokai.css'

# Menu 
MENUITEMS = (('Home', '/'), )
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

# Helper
FALSE = False

# Social widget (I believe not used)
SOCIAL = (('github', 'https://github.com/lukemelas'),
          ('linkedin', 'https://linkedin.com/in/lukemelas'),)

DEFAULT_PAGINATION = False

# NEW
#HEADER_COVER = 'static/my_image.png'
HEADER_COVER = '"' # no background image
HEADER_COVER = 'assets/images/general/background.jpg' 

# CSS
CSS_OVERRIDE = ['assets/css/custom.css', 'assets/css/light-theme.css', 'assets/css/dark-theme.css', 'assets/css/dark-theme.js']

# Theme
# THEME = 'theme/attila'
THEME = 'theme/medius'

# AUTHOR(S) -- NOTE: The data for the home page (index.html) is in the index.html
#                    file in the theme:         theme/attila/templates/index.html
AUTHORS_BIO = {
    "luke": {
        "name": "Luke Melas-Kyriazi",
        "cover": "assets/images/general/background.jpg",
        "image": "assets/images/general/headshot.jpg",
        "location": "Cambridge, MA",
        "bio": "I'm Luke, a student at Harvard interested in mathematics and computer science. I hope you enjoy my writing and open-source code."
    }
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

## Comments
# DISQUS_SITENAME = "lukemelas"

# Analytics
GOOGLE_ANALYTICS = "UA-119150275-1"

# DARK MODE
THEME_COLOR = 'light'  # 'dark'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True
