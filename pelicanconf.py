#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Eric, Etan, Fred, Genny, & Steve'
SITENAME = u'The Nest'
SITEURL = ''
STATIC_PATHS = ['images']

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

TYPOGRIFY = True

# Blogroll
LINKS = (#('Twitter', 'http://twitter.com/thenestmusic'),
         ('Mailing list signup', 'http://eepurl.com/Bdzlf'),
         ('Facebook', 'https://www.facebook.com/TheNestBand'),)

# Social widget
#SOCIAL = (('Twitter', 'http://twitter.com/thenestmusic'),
#          ('Facebook', 'https://www.facebook.com/TheNestMusic'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# basic
# cebong
# chunk
# pelican-cait
THEME = "theme"

FILES_TO_COPY = (('CNAME', 'CNAME'),)
