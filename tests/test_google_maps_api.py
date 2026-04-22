from utils.checking import Checking
from utils.api import GoogleMapsAPI

class TestCreatePlace:
    """Класс содержащий тесты по работе с локацией"""

    def test_create_new_place(self):
        """Тест по созданию, изменению и удалению новой локации"""

        check = Checking()

        print("Метод POST")
        result_post = GoogleMapsAPI.create_new_place()  # вызов метода по созданию новой локации
        check.check_status_code(result_post, 200)
        check_post = result_post.json()
        place_id = check_post.get("place_id")  # получения place_id для метода GET
        check.check_json_for_keys_in_the_response(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        check.check_json_for_values_in_the_response(result_post, 'status', 'OK')


        print("\nМетод GET POST")
        result_get_new_location = GoogleMapsAPI.get_new_place(place_id)  # отправка метода Get
        check.check_status_code(result_get_new_location, 200)
        check.check_json_for_keys_in_the_response(result_get_new_location, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        check.check_json_for_values_in_the_response(result_get_new_location, 'address', "29, side layout, cohen 09")

        print("\nМетод PUT")
        result_put = GoogleMapsAPI.put_new_place(place_id)  # изменение данных о созданной локации
        check.check_status_code(result_put, 200)
        check.check_json_for_keys_in_the_response(result_put, ['msg'])
        check.check_json_for_values_in_the_response(result_put, 'msg', 'Address successfully updated')

        print("\nМетод GET PUT")
        result_get_update_location = GoogleMapsAPI.get_new_place(place_id)  # отправка метода Get
        check.check_status_code(result_get_update_location, 200)
        check.check_json_for_keys_in_the_response(result_get_update_location, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        check.check_json_for_values_in_the_response(result_get_update_location, 'address', "100 Lenina street, RU")

        print("\nМетод DELETE")
        result_delete = GoogleMapsAPI.delete_new_place(place_id)  # удаление данных о созданной локации
        check.check_status_code(result_delete, 200)
        check.check_json_for_keys_in_the_response(result_delete, ['status'])
        check.check_json_for_values_in_the_response(result_delete, 'status', 'OK')

        print("\nМетод GET DELETE")
        result_get_delete_location = GoogleMapsAPI.get_new_place(place_id)  # отправка метода Get
        check.check_status_code(result_get_delete_location, 404)
        check.check_json_for_keys_in_the_response(result_get_delete_location, ['msg'])
        print((result_get_delete_location.json()).get("msg"))
        check.check_json_for_values_in_the_response(result_get_delete_location, 'msg', "Get operation failed, looks like place_id  doesn't exists")
        check.check_json_search_word_in_value(result_get_delete_location, 'msg', 'failed')
