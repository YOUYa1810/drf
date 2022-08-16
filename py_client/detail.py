import requests

endpoint = "http://localhost:8000/api/products/3/" # HTML raw text response

get_response = requests.get(endpoint, params={'abc': 123}, data={'title': 'hello'}) # http request

print(get_response.text)
