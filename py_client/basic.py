import requests

# endpoint = "https://httpbin.org/anything" # REST API HTTP request

endpoint = "http://localhost:8000/api/" # HTML raw text response

get_response = requests.post(endpoint, params={'abc': 123}, data={'title': 'hello'}) # http request

print(get_response.text)

# # js object notation ~ python dict

# # {
# #   "args": {},
# #   "data": "",
# #   "files": {},
# #   "form": {},
# #   "headers": {
# #     "Accept": "*/*",
# #     "Accept-Encoding": "gzip, deflate",
# #     "Host": "httpbin.org",
# #     "User-Agent": "python-requests/2.28.1",
# #     "X-Amzn-Trace-Id": "Root=1-62f1199d-53bca006538c70c142ead481"
# #   },
# #   "json": null,
# #   "method": "GET",
# #   "origin": "86.195.137.170",
# #   "url": "https://httpbin.org/anything"
# # } 
# print(get_response.json())

# {'args': {}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.28.1', 'X-Amzn-Trace-Id': 'Root=1-62f119f5-0f2ccf67367a0c7d000b7e71'}, 'json': None, 'method': 'GET', 'origin': '86.195.137.170', 'url': 'https://httpbin.org/anything'}