import requests

BASE = "https://api.github.com/users/Immanuel-11"
response = requests.get(BASE+"/repos")
repos = response.json()
print(f"{requests.get(BASE).json()['name']} has {len(repos)} repos\n")
language = lambda datum: datum['language'] if datum['language'] else "-"
for repo in repos:
    print(f"{repo['name']:<18}  |  {language(repo):<10} | \N{WHITE MEDIUM STAR} {repo['stargazers_count']}")