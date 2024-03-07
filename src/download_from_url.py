
import requests

def download_from_url(url):
    response = requests.get(url)
    return response.content.decode()