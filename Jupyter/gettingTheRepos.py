import requests
r = requests.get('https://api.github.com/user/repos', headers = {'Authorization':'token 0b807a4131122a1e816b84ed93c71ffaa343e3a1'})
print(r.json())
