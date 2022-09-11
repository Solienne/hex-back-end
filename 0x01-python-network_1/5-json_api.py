#!/usr/bin/python3
"""
 script takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
from sys import argv


if __name__ == '__main__':
    """ Function sends post request"""
    if len(argv) >= 2:
        l = argv[1]
    else:
        l = ""
    try:
        d = {'q': l}
        r = requests.post('http://0.0.0.0:5000/search_user', data=d).json()
        if "id" in r and "name" in r:
            print('[{}] {}'.format(r['id'], r['name']))
        else:
            print('No result')
    except BaseException:
        print('Not a valid JSON')
