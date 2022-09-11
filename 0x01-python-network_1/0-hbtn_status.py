#!/usr/bin/python3
"""
Write Python script to fetche https://intranet.hbtn.io/status
"""

import requests

""" Function makes a request to a url."""
r = requests.get('https://intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(r.text)))
print("\t- content: {}".format(r.text))
