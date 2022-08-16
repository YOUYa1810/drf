import requests

endpoint = "http://localhost:8000/api/products/1/update/" # HTML raw text response

get_response = requests.put(endpoint, params={'abc': 123}, json={'title': 'new hello'}) # http request

print(get_response.text)
