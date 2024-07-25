import datetime


class Constants:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru'


class APICourierUrls:
    COURIER_LOGIN_URL = '/api/v1/courier/login'
    CREATING_COURIER_URL = '/api/v1/courier/'
    DELETE_COURIER_URL = '/api/v1/courier/'


class APIOrdersUrls:
    CREATING_ORDER_URL = '/api/v1/orders'
    GETTING_LIST_OF_ORDERS_URL = '/api/v1/orders'
    ACCEPT_ORDER_URL = '/api/v1/orders/accept/'
    RECEIVE_ORDER_BY_NUMBER_URL = '/api/v1/orders/track?t='


class OrdersData:
    TODAY = datetime.date.today()
    TOMORROW = TODAY + datetime.timedelta(days=1)
    DAY_AFTER_TOMORROW = TODAY + datetime.timedelta(days=2)
    TODAY_PLUS10_DAYS = TODAY + datetime.timedelta(days=10)

    ORDER_FORM = {
        "firstName": "Narutotestqqq",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": f"{TOMORROW}",
        "comment": "Saske, come back to Konoha"
    }
