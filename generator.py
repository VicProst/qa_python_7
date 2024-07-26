import json
import allure
import requests
import random
import string
from data import Constants, APICourierUrls, APIOrdersUrls, OrdersData


@allure.step('Зарегистрировать нового курьера и вернуть его login, password и first_name')
def register_new_courier_and_return_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    login_pass = []
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    payload = {"login": login, "password": password, "firstName": first_name}
    response = requests.post(Constants.MAIN_URL + APICourierUrls.CREATING_COURIER_URL, data=payload)
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)
    return response, login_pass

@allure.step('Создать новый заказ и вернуть его track')
def creating_new_order():
    payload = json.dumps(OrdersData.ORDER_FORM)
    response = requests.post(Constants.MAIN_URL + APIOrdersUrls.CREATING_ORDER_URL, data=payload)
    track = response.json()["track"]
    return track
