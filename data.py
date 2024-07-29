import datetime


class Constants:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru'


class APICourierUrls:
    CREATING_COURIER_URL = '/api/v1/courier/'
    COURIER_LOGIN_URL = '/api/v1/courier/login'
    DELETE_COURIER_URL = '/api/v1/courier/'

class APICourierResponseTexts:
    CREATING_COURIER_ALREADY_EXISTS_ERROR = 'Этот логин уже используется'
    CREATING_COURIER_NO_REQUIRED_FIELD_ERROR = 'Недостаточно данных для создания учетной записи'

    COURIER_LOGIN_WRONG_LOGIN_PASS_ERROR = 'Учетная запись не найдена'
    COURIER_LOGIN_NO_LOGIN_PASS_ERROR = 'Недостаточно данных для входа'

    DELETE_COURIER_NO_ID_ERROR = 'Недостаточно данных для удаления курьера'
    DELETE_COURIER_NON_EXISTENT_ID_ERROR = 'Курьера с таким id нет'

class APIOrdersUrls:
    CREATING_ORDER_URL = '/api/v1/orders'
    GETTING_LIST_OF_ORDERS_URL = '/api/v1/orders'
    ACCEPT_ORDER_URL = '/api/v1/orders/accept/'
    RECEIVE_ORDER_BY_NUMBER_URL = '/api/v1/orders/track?t='

class APIOrdersResponseTexts:
    ACCEPT_ORDER_WITHOUT_COURIER_OR_ORDER_ID_ERROR = 'Недостаточно данных для поиска'
    ACCEPT_ORDER_NON_EXISTENT_COURIER_ID_ERROR = 'Курьера с таким id не существует'
    ACCEPT_ORDER_NON_EXISTENT_ORDER_ID_ERROR = 'Заказа с таким id не существует'

    RECEIVE_ORDER_BY_NUMBER_WITHOUT_TRACK_ERROR = 'Недостаточно данных для поиска'
    RECEIVE_ORDER_BY_NUMBER_NON_EXISTENT_TRACK_ERROR = 'Заказ не найден'

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
