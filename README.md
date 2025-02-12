# Проект автоматизации тестирования API сервиса Яндекс Самокат
1. Основа для написания автотестов — фреймворк pytest
2. Установить зависимости — pip install -r requirements.txt
3. Команда для запуска — pytest -v
4. Константы и данные для тестов - data.py
5. Генератор создания нового курьера и нового заказа - generator.py
6. Фикстуры для тестов - conftest.py

# TestAPICreatingCourier:
- test_creating_courier_new_courier_data_true - Проверка создания нового курьера
- test_creating_courier_courier_already_exists_error_message - Проверка создания двух одинаковых курьеров
- test_creating_courier_no_required_field_error_message - Проверка создания курьера, при передачи в ручку не всех обязательных полей

# TestAPICourierLogin:
- test_courier_login_registered_courier_data_true - Проверка авторизации курьера
- test_courier_login_wrong_login_pass__error_message - Проверка авторизации курьера с неправильно указанным логином или паролем
- test_courier_login_no_login_pass_error_message - Проверка авторизации курьера без указания логина или пароля

# TestAPIDeleteCourier:
- test_delete_courier_exists_id_true - Проверка удаления курьера
- test_delete_courier_no_id_error_message - Проверка удаления курьера, если отправить запрос без id
- test_delete_courier_non_existent_id_error_message - Проверка удаления курьера, если отправить запрос с несуществующим id

# TestAPICreatingOrder:
- test_creating_order_can_specify_color_true - Проверка создания заказа

# TestAPIGettingOrdersList:
- test_getting_orders_list_true - Проверка получения списка заказов

# TestAPIAcceptOrder:
- test_accept_order_existing_courier_and_order_id_true - Проверка принятия заказа
- test_accept_order_without_courier_id_error_message - Проверка принятия заказа без указания id курьера
- test_accept_order_without_order_id_error_message - Проверка принятия заказа без указания id заказа
- test_accept_order_non_existent_courier_id_error_message - Проверка принятия заказа с передачей неверного id курьера
- test_accept_order_non_existent_order_id_error_message - Проверка принятия заказа с передачей неверного id заказа

# TestAPIReceiveOrderByNumber:
- test_receive_order_by_number_existing_track_true - Проверка получения заказа по его номеру
- test_receive_order_by_number_without_track_error_message - Проверка получения заказа по его номеру, без указания номера
- test_receive_order_by_number_non_existent_track_error_message - Проверка получения заказа по его номеру, с указанием несуществующего номера
