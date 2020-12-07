from collections import namedtuple
import os
from github import Github, InputFileContent
from pprint import pprint


github_user = str(input('What user do you want to search for? '))
gh = Github()
github_account = gh.get_user(github_user)
Repo = namedtuple('Repo', 'name stars forks update pushed')


def get_repo_stats(user, n=5):
    """ Example from 100 Days of Code"""
    repos = []
    for repo in user.get_repos():
        if repo.fork:
            continue

        repos.append(Repo(name=repo.name,
                          stars=repo.stargazers_count,
                          forks=repo.forks_count,
                          update=repo.updated_at,
                          pushed=repo.pushed_at))

    return sorted(repos, key=lambda x: x.stars, reverse=True)[:n]


pprint(get_repo_stats(github_account))
