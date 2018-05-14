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
MENUITEMS = (('Home', '/'), )


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
THEME = 'pelican-themes/attila'

# AUTHOR(S)
AUTHORS_BIO = {
    "luke": {
        "name": "Zutrinken",
        "cover": "https://arulrajnet.github.io/attila-demo/assets/images/avatar.png",
        "image": "https://arulrajnet.github.io/attila-demo/assets/images/avatar.png",
        "website": "http://blog.arulraj.net",
        "location": "Chennai",
        "bio": "This is the place for a small biography with max 200 characters. Well, now 100 are left. Cool, hugh?"
    }
}


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
