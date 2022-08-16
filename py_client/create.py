import requests

endpoint = "http://localhost:8000/api/products/" # HTML raw text response

get_response = requests.post(endpoint, params={'abc': 123}, data={'title': 'create'}) # http request

print(get_response.text)
