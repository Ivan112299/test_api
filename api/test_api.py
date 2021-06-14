import requests

response = requests.get('https://petstore.swagger.io/v2/store/inventory')

print(response)
print(response.status_code)