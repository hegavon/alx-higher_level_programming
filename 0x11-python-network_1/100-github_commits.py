#!/usr/bin/python3

"""
This script uses the GitHub API to list the last 10 commits
for a given repository and owner.
Usage: ./100-github_commits.py [github_repo] [github_owner]
"""

from sys import argv
import requests

if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    r = requests.get(url)
    list_commits = r.json()
    for commit in list_commits[0:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
