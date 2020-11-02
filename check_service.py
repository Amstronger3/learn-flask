import requests

new_user = {
    'username': 'Bruce',
}

response = requests.get('http://localhost:5000/users/add/')

print(response.json())
