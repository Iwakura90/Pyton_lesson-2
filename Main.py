import requests

url = 'https://www.banki.ru/products/currency/cash/sankt-peterburg/'
response = requests.get(url)
print(response)
