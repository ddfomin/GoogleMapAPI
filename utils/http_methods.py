"""HTTP методы с логированием"""
import allure
import requests
from utils.logger import Logger


@allure.step("GET запрос")
def get(url):
    """GET запрос"""
    Logger.add_request(url, "GET")
    response = requests.get(url)
    Logger.add_response(response)
    return response


@allure.step("POST запрос")
def post(url, body):
    """POST запрос"""
    Logger.add_request(url, "POST")
    response = requests.post(url, json=body)
    Logger.add_response(response)
    return response


@allure.step("PUT запрос")
def put(url, body):
    """PUT запрос"""
    Logger.add_request(url, "PUT")
    response = requests.put(url, json=body)
    Logger.add_response(response)
    return response


@allure.step("DELETE запрос")
def delete(url, body):
    """DELETE запрос"""
    Logger.add_request(url, "DELETE")
    response = requests.delete(url, json=body)
    Logger.add_response(response)
    return response