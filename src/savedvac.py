import json
from abc import ABC, abstractmethod

from src.vacancies import Vacancy


class AbstractSaver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        """
        Абстрактный метод для добавления вакансии в хранилище.

        Parameters:
        - vacancy (Vacancy): Вакансия для добавления.

        Returns:
        - bool: True, если вакансия успешно добавлена, False в противном случае.
        """
        pass

    @abstractmethod
    def get_vacancies_by_criteria(self, criteria):
        """
        Абстрактный метод для получения списка вакансий по заданным критериям.

        Parameters:
        - criteria (dict): Критерии для фильтрации вакансий.

        Returns:
        - list: Список вакансий, соответствующих критериям.
        """
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        """
        Абстрактный метод для удаления вакансии из хранилища.

        Parameters:
        - vacancy (Vacancy): Вакансия для удаления.

        Returns:
        - bool: True, если вакансия успешно удалена, False в противном случае.
        """
        pass


class JSONSaver(AbstractSaver):
    def __init__(self, filename="vacancies.json"):
        self.filename = filename
        self.vacancies = []

    def add_vacancy(self, vacancy):
        self.vacancies.append(vars(vacancy))

    def get_vacancies_by_criteria(self, criteria):
        return [
            Vacancy(**vacancy)
            for vacancy in self.vacancies
            if all(vacancy.get(key) == value for key, value in criteria.items())
        ]

    def delete_vacancy(self, vacancy):
        vacancy_data = vars(vacancy)
        if vacancy_data in self.vacancies:
            self.vacancies.remove(vacancy_data)
            self.save_to_file()
            return True
        return False

    def save_to_file(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.vacancies, file, indent=4, ensure_ascii=False)
