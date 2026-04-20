import utils.http_methods as http

base_url = "https://rahulshettyacademy.com"
key = "?key=qaclick123"


class GoogleMapsAPI:
    """Класс содержащий методы для тестирования Google Maps API. Здесь Мы будем хранить все,
    что необходимо для отправки нашего запроса - url, path, body и т.д."""

    @staticmethod
    def create_new_place():
        """Метод по созданию новой локации"""

        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resource = "/maps/api/place/add/json"  # ресурс метода POST
        post_url = base_url + post_resource + key
        print(post_url)

        result_post = http.post(post_url, json_for_create_new_place)
        print(result_post.json())
        print(result_post.status_code)
        return result_post