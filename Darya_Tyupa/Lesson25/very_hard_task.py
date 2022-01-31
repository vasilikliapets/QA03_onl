import json
import requests
from pprint import pprint
from github import Github

response = requests.get('https://api.github.com/users/DaryaTyupa').json()
pprint(response)

g = Github()
user = g.get_user('DaryaTyupa')
for repo in user.get_repos():
    print(repo)
    print(repo.full_name)
    print(repo.default_branch)
    print(repo.get_pulls_comments())
