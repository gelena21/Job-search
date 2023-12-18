import os

from dotenv import load_dotenv
import requests
from abc import ABC, abstractmethod

from src.vacancies import Vacancy

load_dotenv()


class AbstractAPI(ABC):
    """
    Абстрактный класс для работы с API поиска работы.
    """

    @abstractmethod
    def get_vacancies(self, search_query):
        """
        Получает список вакансий по поисковому запросу.

        Parameters:
        - search_query (str): Поисковой запрос.

        Returns:
        - list: Список вакансий.
        """
        pass


class HeadHunterAPI(AbstractAPI):
    """
    API поиска работы HeadHunter.
    """

    def get_vacancies(self, search_query):
        url = f"https://api.hh.ru/vacancies?text={search_query}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            vacancies = [
                Vacancy(
                    title=vacancy["name"],
                    link=vacancy["alternate_url"],
                    salary=vacancy.get("salary"),
                )
                for vacancy in data["items"]
            ]
            return vacancies
        else:
            return []


class SuperJobAPI(AbstractAPI):
    """
    API поиска работы SuperJob.
    """

    def get_vacancies(self, search_query):
        headers = {
            "X-Api-App-Id": os.getenv("API_S_JOB")
        }
        url = f"https://api.superjob.ru/2.0/vacancies/?keyword={search_query}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            vacancies = [
                Vacancy(
                    title=vacancy["profession"],
                    link=vacancy["link"],
                    salary={
                        "from": vacancy['payment_from'],
                        "to": vacancy['payment_to'],
                    },
                )
                for vacancy in data["objects"]
            ]
            return vacancies
        else:
            return []


def get_vacancies(search_query, api_name="hh"):
    """
    Получает список вакансий по поисковому запросу.

    Parameters:
    - search_query (str): Поисковой запрос.
    - api_name (str): Название API поиска работы.

    Returns:
    - list: Список вакансий.
    """

    if api_name == "hh":
        return HeadHunterAPI().get_vacancies(search_query)
    elif api_name == "superjob":
        return SuperJobAPI().get_vacancies(search_query)
    else:
        raise ValueError(f"Неизвестный API: {api_name}")
