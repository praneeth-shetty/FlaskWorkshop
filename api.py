import requests
import json

def CatApi():
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url=url,timeout=5).json()
    return response[0]['url']

def DogApi():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url=url,timeout=5).json()
    return response['message']
