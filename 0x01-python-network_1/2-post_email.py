#!/usr/bin/python3
"""
script takes in a URL and an email address
sends POST request to the passed URL with the email as parameter
and displays the body of the response
"""

import requests
from sys import argv

def urlRequest(url, email):
    """ Function that sends a post request """
    values = {'email': email}
    r = requests.get(url, params=values)
    print(r.text.decode('utf-8'))

if __name__ == "__main__":
    urlRequest(sys.argv[1], sys.argv[2])
