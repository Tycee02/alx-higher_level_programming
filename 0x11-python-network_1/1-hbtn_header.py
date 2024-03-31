#!/usr/bin/python
"""
takes in a URL, sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response.
"""

from urllib import request
import sys

if __name__ == "__main__":
    with request.urlopen(sys.argv[1] as res):
        print(res.info()['X-Request-Id'])
