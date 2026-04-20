import json
from utils.api import GoogleMapsAPI

class TestCreatePlace:
    """Класс содержащий тест по работе с локацией"""

    def test_create_new_place(self):
        """Тест по созданию, изменению и удалению новой локации"""

        print("Метод POST")
        result_post = GoogleMapsAPI.create_new_place()  # вызов метода по созданию новой локации