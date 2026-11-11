import requests

response = requests.get("https://api.github.com/users/Immanuel-11")
data = response.json()

print(f"API status code: {response.status_code}")
print(f"user name: {data['name']}")
print(f"No. of repos: {data['public_repos']}")
