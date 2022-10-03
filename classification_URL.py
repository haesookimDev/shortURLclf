import sys
import os
import numpy as np

def clf_short_url(url):
    shortURL = False
    isDomain = False

    isDomain = check_url_domain(url)

    shortURL = isDomain

    return {'isShort':shortURL, 'URL':url}

def check_url_domain(url):
    
    isDomain = False

    # this part compares the URL with the domain of the URL Shortening service
    
    return isDomain