import pytest
import allure
import requests
from conftest import reg_new_courier_return_login_pass_del_this_courier
from data import Constants, APICourierUrls
from generator import register_new_courier_and_return_login_password


@allure.epic('test_creating_courier')
class TestCreatingCourier:

    @allure.title('Проверка создания нового курьера')
    @allure.description('Можно создать курьера с новыми логином, паролем и именем')
    def test_creating_courier_new_courier_data_true(self, reg_new_courier_return_login_pass_del_this_courier):
        response = reg_new_courier_return_login_pass_del_this_courier[0]
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Проверка создания двух одинаковых курьеров')
    @allure.description('Если создать курьера с логином, который уже есть, возвращается ошибка')
    def test_creating_courier_courier_already_exists_error_message(self, reg_new_courier_return_login_pass_del_this_courier):
        login_pass = reg_new_courier_return_login_pass_del_this_courier[1]
        same_login_pass = {"login": login_pass[0], "password": login_pass[1]}
        response = requests.post(Constants.MAIN_URL + APICourierUrls.CREATING_COURIER_URL, data=same_login_pass)
        assert response.status_code == 409 and response.json()["message"] == 'Этот логин уже используется'

    @allure.title('Проверка создания курьера, при передачи в ручку не всех обязательных полей')
    @allure.description('Если одного из обязательных полей нет, запрос возвращает ошибку')
    @pytest.mark.parametrize('login, password, first_name',
                             [['test765test432', '', 'Victor'],
                             ['', '12345', 'Victor']])
    def test_creating_courier_no_required_field_error_message(self, login, password, first_name):
        payload = {"login": login, "password": password, "firstName": first_name}
        response = requests.post(Constants.MAIN_URL + APICourierUrls.CREATING_COURIER_URL, data=payload)
        assert response.status_code == 400 and response.json()["message"] == 'Недостаточно данных для создания учетной записи'


@allure.epic('test_courier_login')
class TestCourierLogin:

    @allure.title('Проверка авторизации курьера')
    @allure.description('Можно авторизоваться курьеру с существующим логином и паролем')
    def test_courier_login_registered_courier_data_true(self, reg_new_courier_return_login_pass_del_this_courier):
        login_pass = reg_new_courier_return_login_pass_del_this_courier[1]
        payload = {"login": login_pass[0], "password": login_pass[1]}
        response = requests.post(Constants.MAIN_URL + APICourierUrls.COURIER_LOGIN_URL, data=payload)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Проверка авторизации курьера с неправильно указанным логином или паролем')
    @allure.description('Если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    def test_courier_login_wrong_login_pass__error_message(self, reg_new_courier_return_login_pass_del_this_courier):
        login_pass = reg_new_courier_return_login_pass_del_this_courier[1]
        payload = {"login": f'{login_pass[0]+'test'}', "password": f'{login_pass[1]+'12345'}'}
        response = requests.post(Constants.MAIN_URL + APICourierUrls.COURIER_LOGIN_URL, data=payload)
        assert response.status_code == 404 and response.json()["message"] == 'Учетная запись не найдена'

    @allure.title('Проверка авторизации курьера без указания логина или пароля')
    @allure.description('Если авторизоваться без указания логина или пароля, запрос возвращает ошибку')
    @pytest.mark.parametrize('login, password',
                             [['test765test432', ''],
                             ['', '12345']])
    def test_courier_login_no_login_pass_error_message(self, login, password):
        payload = {"login": login, "password": password}
        response = requests.post(Constants.MAIN_URL + APICourierUrls.COURIER_LOGIN_URL, data=payload)
        assert response.status_code == 400 and response.json()["message"] == 'Недостаточно данных для входа'


@allure.epic('test_delete_courier')
class TestDeleteCourier:

    @allure.title('Проверка удаления курьера')
    @allure.description('Можно удалить курьеру с существующим id')
    def test_delete_courier_exists_id_true(self):
        login_pass = register_new_courier_and_return_login_password()[1]
        payload = {"login": login_pass[0], "password": login_pass[1]}
        courier_login_in = requests.post(Constants.MAIN_URL + APICourierUrls.COURIER_LOGIN_URL, data=payload)
        courier_id = courier_login_in.json()['id']
        response = requests.delete(Constants.MAIN_URL + APICourierUrls.DELETE_COURIER_URL + str(courier_id))
        assert response.status_code == 200 and response.text == '{"ok":true}'

    @allure.title('Проверка удаления курьера, если отправить запрос без id')
    @allure.description('Если отправить запрос без id, вернётся ошибка')
    def test_delete_courier_no_id_error_message(self):
        response = requests.delete(Constants.MAIN_URL + APICourierUrls.DELETE_COURIER_URL)
        assert response.status_code == 400 and response.json()["message"] == 'Недостаточно данных для удаления курьера'

    @allure.title('Проверка удаления курьера, если отправить запрос с несуществующим id')
    @allure.description('Если отправить запрос с несуществующим id, вернётся ошибка')
    def test_delete_courier_non_existent_id_error_message(self, reg_new_courier_return_login_pass_del_this_courier):
        login_pass = reg_new_courier_return_login_pass_del_this_courier[1]
        payload = {"login": login_pass[0], "password": login_pass[1]}
        courier_login_in = requests.post(Constants.MAIN_URL + APICourierUrls.COURIER_LOGIN_URL, data=payload)
        courier_id = courier_login_in.json()["id"] + 123456
        response = requests.delete(Constants.MAIN_URL + APICourierUrls.DELETE_COURIER_URL + str(courier_id))
        assert response.status_code == 404 and response.json()["message"] == 'Курьера с таким id нет'
