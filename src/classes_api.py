# classes_api.py

import os
from abc import ABC, abstractmethod

import requests
from dotenv import load_dotenv

load_dotenv()


class AbstractAPI(ABC):
    @abstractmethod
    def get_vacancies(self, search_query):
        """
        Абстрактный метод для получения списка вакансий.

        Parameters:
        - search_query (str): Поисковый запрос для запроса вакансий.

        Returns:
        - list: Список вакансий.
        """
        pass


class HeadHunterAPI(AbstractAPI):
    def __init__(self):
        """
        Конструктор класса HeadHunterAPI.
        Устанавливает базовый URL и заголовки для запросов к API HeadHunter.
        """
        self.base_url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "YourApp/1.0 (your@email.com)"}

    def get_vacancies(self, search_query):
        """
        Получает список вакансий с использованием API HeadHunter.

        Parameters:
        - search_query (str): Поисковый запрос для запроса вакансий.

        Returns:
        - list: Список вакансий.
        """
        url = f"{self.base_url}/vacancies"
        params = {"text": search_query}
        response = requests.get(url, headers=self.headers, params=params)

        if response.status_code == 200:
            return response.json().get("items", [])
        else:
            print(
                f"Failed to retrieve vacancies from HeadHunter. Status code: {response.status_code}"
            )
            return []


class SuperJobAPI(AbstractAPI):
    def __init__(self):
        """
        Конструктор класса SuperJobAPI.
        Устанавливает базовый URL, API-ключ и заголовки для запросов к API SuperJob.
        """
        self.base_url = "https://api.superjob.ru/2.0/vacancies"
        self.api_key = os.getenv("API_S_JOB")
        self.headers = {"X-Api-App-Id": self.api_key}

    def get_vacancies(self, search_query):
        """
        Получает список вакансий с использованием API SuperJob.

        Parameters:
        - search_query (str): Поисковый запрос для запроса вакансий.

        Returns:
        - list: Список вакансий.
        """
        url = f"{self.base_url}/vacancies/"
        params = {"keywords": search_query}
        response = requests.get(url, headers=self.headers, params=params)

        if response.status_code == 200:
            return response.json().get("objects", [])
        else:
            print(
                f"Failed to retrieve vacancies from SuperJob. Status code: {response.status_code}"
            )
            return []
