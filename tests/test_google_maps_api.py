from utils.checking import Checking
from utils.api import GoogleMapsAPI
import allure


@allure.epic("Базовый тест на проверку основных запросов: GET, POST, PUT, DELETE")
class TestCreatePlace:
    # Константы для теста
    ORIGINAL_ADDRESS = "29, side layout, cohen 09"
    UPDATED_ADDRESS = "100 Lenina street, RU"
    ERROR_MSG_PART = "failed"
    EXPECTED_ERROR_MSG = "Get operation failed, looks like place_id  doesn't exists"

    @allure.description("Базовый тест по созданию, изменению и удалению новой локации. Проверка GET, POST, PUT, DELETE")
    def test_create_new_place(self):
        """Базовый тест на проверку основных запросов: GET, POST, PUT, DELETE"""

        api = GoogleMapsAPI()  # Создаём экземпляр один раз

        with allure.step("POST: создание новой локации"):
            result_post = api.create_new_place()
            Checking.check_status_code(result_post, 200)

            place_id = result_post.json().get("place_id")
            allure.attach(place_id, "Созданный place_id")

            # Проверки ответа
            Checking.check_json_for_keys_in_the_response(
                result_post,
                ['status', 'place_id', 'scope', 'reference', 'id']
            )
            Checking.check_json_for_values_in_the_response(
                result_post,
                'status',
                'OK'
            )

        with allure.step("GET: проверка созданной локации"):
            result_get = api.get_new_place(place_id)
            Checking.check_status_code(result_get, 200)
            Checking.check_json_for_keys_in_the_response(
                result_get,
                ['location', 'accuracy', 'name', 'phone_number', 'address',
                 'types', 'website', 'language']
            )
            Checking.check_json_for_values_in_the_response(
                result_get,
                'address',
                self.ORIGINAL_ADDRESS
            )

        with allure.step("PUT: обновление адреса локации"):
            result_put = api.put_new_place(place_id)
            Checking.check_status_code(result_put, 200)
            Checking.check_json_for_keys_in_the_response(result_put, ['msg'])
            Checking.check_json_for_values_in_the_response(
                result_put,
                'msg',
                'Address successfully updated'
            )

        with allure.step("GET: проверка обновлённой локации"):
            result_get_updated = api.get_new_place(place_id)
            Checking.check_status_code(result_get_updated, 200)
            Checking.check_json_for_values_in_the_response(
                result_get_updated,
                'address',
                self.UPDATED_ADDRESS
            )

        with allure.step("DELETE: удаление локации"):
            result_delete = api.delete_new_place(place_id)
            Checking.check_status_code(result_delete, 200)
            Checking.check_json_for_keys_in_the_response(result_delete, ['status'])
            Checking.check_json_for_values_in_the_response(
                result_delete,
                'status',
                'OK'
            )

        with allure.step("GET: проверка, что локация удалена"):
            result_get_deleted = api.get_new_place(place_id)
            Checking.check_status_code(result_get_deleted, 404)
            Checking.check_json_for_keys_in_the_response(result_get_deleted, ['msg'])
            Checking.check_json_for_values_in_the_response(
                result_get_deleted,
                'msg',
                self.EXPECTED_ERROR_MSG
            )
            Checking.check_json_search_word_in_value(
                result_get_deleted,
                'msg',
                self.ERROR_MSG_PART
            )

            # Дополнительная информация для отчёта
            error_msg = result_get_deleted.json().get("msg")
            allure.attach(error_msg, "Сообщение об ошибке после удаления")