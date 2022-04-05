import requests

chemin = 'https://jsonplaceholder.typicode.com/'

users = requests.get(chemin+'users').json()

for user in users:
    print(user)
    break
