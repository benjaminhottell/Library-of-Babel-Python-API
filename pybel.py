#!/usr/bin/env python

__author__ = "Victor Cortez"
__version__ = "1.0"
__maintainer__ = "Victor Cortez"
__email__ = "victorcortezcb@gmail.com"
__status__ = "In Production"

import typing as t

import requests


_API_URL = 'https://libraryofbabel.info/download.cgi'


# Return true if and only if the input string is an alphanumeric, ASCII string
# (i.e. it consists only of a-z, A-Z, 0-9)
def _is_alnum(s:"str"):
    return s.isascii() and s.isalnum()

def getbook(
        hexagon:"str",
        wall:"int",
        shelf:"int",
        volume:"int") -> "str":

    # Normalize user input

    hexagon = hexagon.strip().lower()

    # Validate user input

    if not _is_alnum(hexagon):
        raise ValueError('Hexagon must be an alphanumeric string')

    if wall > 4 or wall < 1:
        raise ValueError('Wall must be in range 1-4 (inclusive)')

    if shelf > 5 or shelf < 1:
        raise ValueError('Shelf must be in range 1-5 (inclusive)')

    if volume > 32 or volume < 1:
        raise ValueError('Volume must be in range 1-32 (inclusive)')

    # Convert user ints into strings
    # Volume must have 2 digits, so left pad with a 0 if needed

    volume_str = str(volume).zfill(2)
    wall_str = str(wall)
    shelf_str = str(shelf)

    # Build and submit request

    form : "t.Dict[str,str]" = {
        "hex": hexagon,
        "wall": wall_str,
        "shelf": shelf_str,
        "volume": volume_str,
        "page": "1",
        "title": "startofthetext"
    }

    text = requests.post(_API_URL, data=form)

    # Cleaning the raw text, so "content" turns into the pure book
    content = text.text[len("startofthetext")+ 2::].rsplit('\n', 4)[0]

    return content

