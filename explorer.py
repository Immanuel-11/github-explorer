import requests
import sys
import json
from pathlib import Path

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
    user_repo = f"{user['name']} has {len(repos)} repos\n"
    print(user_repo)
    for repo in repos:
        language = repo["language"] or "-"
        print(f"{repo['name']:<18}  |  {language:<10} | \N{WHITE MEDIUM STAR} {repo['stargazers_count']}")
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    summary = {
        "name": user["name"],
        "public_repos": len(repos),
        "repos": [
            {"name": r["name"], "language": r["language"], "stars": r["stargazers_count"]}
            for r in repos
        ],
    }
    with open(output_dir / f"{username}.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    sys.exit(1)