import datetime
import os
from requests import Response


class Logger:
    # Константы класса (можно вынести наружу или оставить здесь)
    log_dir = "logs"

    @staticmethod
    def write_log_to_file(data: str):
        """Запись данных в лог-файл"""
        # Создаем уникальное имя файла при каждом вызове
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = os.path.join(Logger.log_dir, f"log_{timestamp}.log")

        # Создаем папку, если её нет
        os.makedirs(Logger.log_dir, exist_ok=True)

        with open(file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    @staticmethod
    def add_request(url: str, method: str):
        """Логирование запроса"""
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Request method: {method}\n"
        data_to_add += f"Request URL: {url}\n"
        data_to_add += "\n"

        Logger.write_log_to_file(data_to_add)

    @staticmethod
    def add_response(result: Response):
        """Логирование ответа"""
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)

        data_to_add = f"Response code: {result.status_code}\n"
        data_to_add += f"Response text: {result.text}\n"
        data_to_add += f"Response headers: {headers_as_dict}\n"
        data_to_add += f"Response cookies: {cookies_as_dict}\n"
        data_to_add += f"\n-----\n"

        Logger.write_log_to_file(data_to_add)