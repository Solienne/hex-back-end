#!/usr/bin/python3
"""
script takes in a URL and an email address
sends POST request to the passed URL with the email as a parameter
and displays the body of the response
"""

import requests
from sys import argv


def urlRequest(url, email):
    """ Function that sends a post request """
    values = {'email': email}

    r = requests.post(url, data=values)
    print(r.text)

if __name__ == "__main__":
    urlRequest(argv[1], argv[2])
