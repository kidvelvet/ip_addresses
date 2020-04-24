import requests

api_key = '7eeef434f1a537bd1d56c09a9b6c4dba61c584c4432d1b899481fb44'
ip_address = '190.102.239.207'

api_url = f'https://api.ipdata.co/{ip_address}?api-key={api_key}'


response = requests.get(api_url)
print(response.json())
