import requests
import sys

if len(sys.argv) < 2:
    print("Usage: python explorer.py <username>")
    sys.exit(1)

username = sys.argv[1]

BASE = f"https://api.github.com/users/{username}"


try:
    user_response = requests.get(BASE, timeout=10)
    if user_response.status_code == 404:
        print(f"User '{username}' not found on GitHub.")
        sys.exit(1)
    user_response.raise_for_status()
    repos_response = requests.get(f"{BASE}/repos", timeout=10)
    repos_response.raise_for_status()
    repos = repos_response.json()
    user = user_response.json()
    print(f"{user['name']} has {len(repos)} repos\n")
    for repo in repos:
        language = lambda datum: datum['language'] if datum['language'] else "-"
        print(f"{repo['name']:<18}  |  {language(repo):<10} | \N{WHITE MEDIUM STAR} {repo['stargazers_count']}")
except requests.exceptions.RequestException as e:
    print(f"Request failed {e}")
    sys.exit(1)