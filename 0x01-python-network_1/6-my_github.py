#!/usr/bin/python3
""" Python that fetches an id from api.github.com/users """

import requests as res
from sys import argv


if __name__ == "__main__":
    try:
        r = res.get('https://api.github.com/user', auth=(argv[1], argv[2]))
        print(r.json().get('id'))
    except BaseException:
        pass
