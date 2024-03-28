#!/usr/bin/python3
"""
This script retrieves the user ID from the GitHub API using the provided username and password.
Usage: ./10-my_github.py [github_username] [github_password]
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
    print(r.json().get('id'))
