import requests
URL = "https://reqres.in/api/users?page=2"
GetURL = "https://reqres.in/api/users/2"
GetURLSec = "https://reqres.in/api/users/23"

response = requests.get(URL)

print(response)

print(response.content)

print(response.headers)