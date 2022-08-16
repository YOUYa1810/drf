import requests
from getpass import getpass
endpoint = "http://localhost:8000/api/products/" # HTML raw text response
password = getpass()
auth_endpoint = "http://localhost:8000/api/auth/" # HTML raw text response
auth_res = requests.post(auth_endpoint,json={'username': 'cfe', 'password': password})
print(auth_res.json())

if auth_res.status_code == 200:
    token = auth_res.json()['token']
    

headers = {
    'Authorization': f'Bearer {token}'
}
get_response = requests.get(endpoint, headers=headers, params={'abc': 123}, data={'title': 'hello'}) # http request

print(get_response.text)
