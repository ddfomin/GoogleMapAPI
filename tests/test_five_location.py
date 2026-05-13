from utils.checking import Checking
from utils.api import GoogleMapsAPI
import allure
import pytest


@allure.feature("Управление локациями")
@allure.story("Полный цикл CRUD операций")
def test_complete_places_management():
    """Создание 5 локаций -> сохранение -> проверка -> удаление 2-х -> фильтрация"""

    with allure.step("Создание 5 локаций"):
        api = GoogleMapsAPI()
        place_ids = []
        for _ in range(5):
            response = api.create_new_place()
            Checking.check_status_code(response, 200)
            place_ids.append(response.json()["place_id"])
        allure.attach(f"Созданы ID: {', '.join(place_ids)}", "Результат")

    with allure.step("Сохранение в файл"):
        with open("file.txt", "w") as f:
            f.write("\n".join(place_ids))

    with allure.step("Проверка получения всех локаций"):
        with open("file.txt") as f:
            for place_id in f.read().splitlines():
                response = api.get_new_place(place_id)
                assert response.status_code == 200

    with allure.step("Удаление 2-й и 4-й локаций"):
        with open("file.txt") as f:
            ids = f.read().splitlines()
        api.delete_new_place(ids[1])
        api.delete_new_place(ids[3])
        allure.attach(f"Удалены: {ids[1]}, {ids[3]}", "Удаленные")

    with allure.step("Фильтрация существующих локаций"):
        with open("file.txt") as f:
            all_ids = f.read().splitlines()

        existing = []
        for place_id in all_ids:
            if api.get_new_place(place_id).status_code == 200:
                existing.append(place_id)

        with open("new_file.txt", "w") as f:
            f.write("\n".join(existing))

        allure.attach(f"Существуют: {len(existing)} из {len(all_ids)}", "Итог")
        assert len(existing) == 3


if __name__ == '__main__':
    pytest.main([__file__, '-v'])