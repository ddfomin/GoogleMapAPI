"""Список HTTP методов"""

import requests

headers = {"Content-type": "application/json"}
cookies = None

def get(url):
    return requests.get(url, headers=headers, cookies=cookies)

def post(url, body):
    return requests.post(url, json=body, headers=headers, cookies=cookies)

def put(url, body):
    return requests.put(url, json=body, headers=headers, cookies=cookies)

def delete(url, body):
    return requests.delete(url, json=body, headers=headers, cookies=cookies)