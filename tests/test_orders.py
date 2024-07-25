import json
import pytest
import allure
import requests
from data import Constants, APIOrdersUrls, OrdersData, APICourierUrls
from conftest import reg_new_courier_return_login_pass_del_this_courier
from generator import creating_new_order


@allure.epic('test_creating_order')
class TestCreatingOrder:

    @allure.title('Проверка создания заказа')
    @allure.description('Можно создать заказ с разными параметрами цвета')
    @pytest.mark.parametrize('color', ["BLACK", "GREY", ["BLACK", "GREY"], []])
    def test_creating_order_can_specify_color_true(self, color):
        OrdersData.ORDER_FORM["color"] = color
        payload_string = json.dumps(OrdersData.ORDER_FORM)
        response = requests.post(Constants.MAIN_URL + APIOrdersUrls.CREATING_ORDER_URL, data=payload_string)
        assert response.status_code == 201 and 'track' in response.text


@allure.epic('test_getting_orders_list')
class TestGettingOrdersList:

    @allure.title('Проверка получения списка заказов')
    @allure.description('Можно получить список всех заказов')
    def test_getting_orders_list_true(self):
        response = requests.get(Constants.MAIN_URL + APIOrdersUrls.GETTING_LIST_OF_ORDERS_URL)
        assert response.status_code == 200 and "orders" in response.text


@allure.epic('test_accept_order')
class TestAcceptOrder:

    @allure.title('Проверка принятия заказа')
    @allure.description('Можно принять заказ с существующими id курьера и заказа')
    def test_accept_order_existing_courier_and_order_id_true(self, reg_new_courier_return_login_pass_del_this_courier):
        login_pass = reg_new_courier_return_login_pass_del_this_courier[1]
        payload = {"login": login_pass[0], "password": login_pass[1]}
        courier_login_in = requests.post(Constants.MAIN_URL + APICourierUrls.COURIER_LOGIN_URL, data=payload)
        courier_id = courier_login_in.json()['id']
        track = creating_new_order()
        order = requests.get(Constants.MAIN_URL + APIOrdersUrls.RECEIVE_ORDER_BY_NUMBER_URL + str(track))
        order_id = order.json()['order']['id']
        response = requests.put(Constants.MAIN_URL + APIOrdersUrls.ACCEPT_ORDER_URL + str(order_id) + '?courierId=' + str(courier_id))
        assert response.status_code == 200 and response.text == '{"ok":true}'

    @allure.title('Проверка принятия заказа без указания id курьера')
    @allure.description('Если не передать id курьера, запрос вернёт ошибку')
    def test_accept_order_without_courier_id_error_message(self):
        track = creating_new_order()
        order = requests.get(Constants.MAIN_URL + APIOrdersUrls.RECEIVE_ORDER_BY_NUMBER_URL + str(track))
        order_id = order.json()['order']['id']
        response = requests.put(Constants.MAIN_URL + APIOrdersUrls.ACCEPT_ORDER_URL + str(order_id) + '?courierId=')
        assert response.status_code == 400 and response.json()["message"] == 'Недостаточно данных для поиска'

    @allure.title('Проверка принятия заказа без указания id заказа')
    @allure.description('Если не передать id заказа, запрос вернёт ошибку')
    def test_accept_order_without_order_id_error_message(self, reg_new_courier_return_login_pass_del_this_courier):
        login_pass = reg_new_courier_return_login_pass_del_this_courier[1]
        payload = {"login": login_pass[0], "password": login_pass[1]}
        courier_login_in = requests.post(Constants.MAIN_URL + APICourierUrls.COURIER_LOGIN_URL, data=payload)
        courier_id = courier_login_in.json()['id']
        response = requests.put(Constants.MAIN_URL + APIOrdersUrls.ACCEPT_ORDER_URL + '?courierId=' + str(courier_id))
        assert response.status_code == 400 and response.json()["message"] == 'Недостаточно данных для поиска'

    @allure.title('Проверка принятия заказа с передачей неверного id курьера')
    @allure.description('Если передать неверный id курьера, запрос вернёт ошибку')
    def test_accept_order_non_existent_courier_id_error_message(self, reg_new_courier_return_login_pass_del_this_courier):
        login_pass = reg_new_courier_return_login_pass_del_this_courier[1]
        payload = {"login": login_pass[0], "password": login_pass[1]}
        courier_login_in = requests.post(Constants.MAIN_URL + APICourierUrls.COURIER_LOGIN_URL, data=payload)
        courier_id = courier_login_in.json()['id'] + 123456
        track = creating_new_order()
        order = requests.get(Constants.MAIN_URL + APIOrdersUrls.RECEIVE_ORDER_BY_NUMBER_URL + str(track))
        order_id = order.json()['order']['id']
        response = requests.put(Constants.MAIN_URL + APIOrdersUrls.ACCEPT_ORDER_URL + str(order_id) + '?courierId=' + str(courier_id))
        assert response.status_code == 404 and response.json()["message"] == 'Курьера с таким id не существует'

    @allure.title('Проверка принятия заказа с передачей неверного id заказа')
    @allure.description('Если передать неверный id заказа, запрос вернёт ошибку')
    def test_accept_order_non_existent_order_id_error_message(self, reg_new_courier_return_login_pass_del_this_courier):
        login_pass = reg_new_courier_return_login_pass_del_this_courier[1]
        payload = {"login": login_pass[0], "password": login_pass[1]}
        courier_login_in = requests.post(Constants.MAIN_URL + APICourierUrls.COURIER_LOGIN_URL, data=payload)
        courier_id = courier_login_in.json()['id']
        track = creating_new_order()
        order = requests.get(Constants.MAIN_URL + APIOrdersUrls.RECEIVE_ORDER_BY_NUMBER_URL + str(track))
        order_id = order.json()['order']['id'] + 123456
        response = requests.put(Constants.MAIN_URL + APIOrdersUrls.ACCEPT_ORDER_URL + str(order_id) + '?courierId=' + str(courier_id))
        assert response.status_code == 404 and response.json()["message"] == 'Заказа с таким id не существует'


@allure.epic('test_receive_order_by_number')
class TestReceiveOrderByNumber:

    @allure.title('Проверка получения заказа по его номеру')
    @allure.description('Можно получить заказ, если указать его существующий номер')
    def test_receive_order_by_number_existing_track_true(self):
        track = creating_new_order()
        response = requests.get(Constants.MAIN_URL + APIOrdersUrls.RECEIVE_ORDER_BY_NUMBER_URL + str(track))
        assert response.status_code == 200 and "order" in response.text

    @allure.title('Проверка получения заказа по его номеру, без указания номера')
    @allure.description('Запрос без номера заказа возвращает ошибку')
    def test_receive_order_by_number_without_track_error_message(self):
        response = requests.get(Constants.MAIN_URL + APIOrdersUrls.RECEIVE_ORDER_BY_NUMBER_URL)
        assert response.status_code == 400 and response.json()["message"] == 'Недостаточно данных для поиска'

    @allure.title('Проверка получения заказа по его номеру, с указанием несуществующего номера')
    @allure.description('Запрос с несуществующим номером заказа возвращает ошибку')
    def test_receive_order_by_number_non_existent_track_error_message(self):
        track = creating_new_order() + 123456789
        response = requests.get(Constants.MAIN_URL + APIOrdersUrls.RECEIVE_ORDER_BY_NUMBER_URL + str(track))
        assert response.status_code == 404 and response.json()["message"] == 'Заказ не найден'
