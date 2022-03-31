import requests
import json
from pprint import pprint

url = 'https://api.github.com/users/'
user = 'EkaterinaAnufrieva'

response = requests.get(f'{url}{user}/repos')

j_data = response.json()

repos = {
    'name':[]
}
for i in j_data:
    repos['name'].append(i['name'])

with open ('repos_file.json', 'w') as file:
    json.dump(repos, file)

print(f'У пользователя {user} есть репозитарии: {repos["name"]}')
