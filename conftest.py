import pytest
import requests
from data import Constants, APICourierUrls
from generator import register_new_courier_and_return_login_password


@pytest.fixture
def reg_new_courier_return_login_pass_del_this_courier():
    response, login_pass = register_new_courier_and_return_login_password()
    yield response, login_pass
    payload = {"login": login_pass[0], "password": login_pass[1]}
    courier_login_in = requests.post(Constants.MAIN_URL + APICourierUrls.COURIER_LOGIN_URL, data=payload)
    courier_id = courier_login_in.json()['id']
    q = requests.delete(Constants.MAIN_URL + APICourierUrls.DELETE_COURIER_URL + str(courier_id))
    if q.status_code == 200:
        print('Созданный курьер удален')
    else:
        print('Ошибка')
