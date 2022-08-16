import requests

product_id = input('delete id:\n')
try:
    product_id = int(product_id)
except:
    print(f'{product_id} is not a valid product id')
endpoint = f"http://localhost:8000/api/products/{product_id}/delete/" # HTML raw text response

get_response = requests.delete(endpoint, params={'abc': 123}) # http request

print(get_response.status_code, get_response.status_code==204)
