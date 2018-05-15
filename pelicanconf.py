#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Luke Melas-Kyriazi'
SITENAME = "Luke's Notes"
SITEURL = '' 

PATH = 'content'

STATIC_PATHS = ['assets', 'assets/icons/favicon.ico']

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

EXTRA_PATH_METADATA = {
    'assets/icons/favicon.ico': {'path': 'favicon.ico'}
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python', 'http://python.org/'),
         ('Github', 'http://github.com/'),)

# Colors (for code?)
COLOR_SCHEME_CSS = 'monokai.css'

# Menu 
MENUITEMS = (('Home', '/'), 
             ('Image Colorization', '/image-colorization.html'),)


# Social widget (I believe not used)
SOCIAL = (('github', 'https://github.com/lukemelas'),
          ('linkedin', 'https://linkedin.com/in/lukemelas'),)

DEFAULT_PAGINATION = False

# NEW
#HEADER_COVER = 'static/my_image.png'
HEADER_COVER = '"' # no background image
HEADER_COVER = 'assets/images/hvd-blur-compressed-2.jpg' 

# CSS
CSS_OVERRIDE = ['assets/css/custom.css']

# Theme
THEME = 'theme/attila'

# AUTHOR(S) -- NOTE: The data for the home page (index.html) is in the index.html
#                    file in the theme:         theme/attila/templates/index.html
AUTHORS_BIO = {
    "luke": {
        "name": "Luke Melas-Kyriazi",
        "cover": "assets/images/hvd-blur-compressed-2.jpg",
        "image": "assets/images/headshot2.jpg",
        "location": "Cambridge, MA",
        "bio": "I'm Luke, an undergraduate at Harvard studying mathematics and computer science. I hope you enjoy my writing and open-source code."
    }
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

## Comments
#DISQUS_SITENAME = "attilademo"

# Analytics
GOOGLE_ANALYTICS = "UA-119150275-1"

