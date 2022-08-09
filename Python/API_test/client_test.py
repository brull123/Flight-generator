from urllib import response
import requests

base_url = "http://127.0.0.1:5000/"

response = requests.get(base_url+"api/LKPR/EBBR/None/100/500")
print(response.json())