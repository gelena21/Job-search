# utils.py

from typing import List

from src.vacancies import Vacancy


def sort_vacancies(vacancies):
    """
    Сортирует вакансии по зарплате.

    Parameters:
    - vacancies (List[Vacancy]): Список вакансий.

    Returns:
    - List[Vacancy]: Отсортированный список вакансий.
    """
    return sorted(vacancies, key=lambda x: x.salary)


def get_top_vacancies(vacancies, n):
    """
    Возвращает топ-N вакансий.

    Parameters:
    - vacancies (List[Vacancy]): Список вакансий.
    - n (int): Количество вакансий для вывода.

    Returns:
    - List[Vacancy]: Топ-N вакансий.
    """
    return vacancies[:n]


def print_vacancies(vacancies):
    """
    Выводит информацию о вакансиях в консоль.

    Parameters:
    - vacancies (List[Vacancy]): Список вакансий.
    """
    for i, vacancy in enumerate(vacancies, start=1):
        print(f"{i}. {vacancy.title} ({vacancy.salary}): {vacancy.link}")


def filter_vacancies(
    vacancies: List[Vacancy], filter_words: List[str]
) -> List[Vacancy]:
    """
    Фильтрует вакансии по ключевым словам.

    Parameters:
    - vacancies (List[Vacancy]): Список вакансий.
    - filter_words (List[str]): Список ключевых слов для фильтрации.

    Returns:
    - List[Vacancy]: Отфильтрованный список вакансий.
    """
    filtered_vacancies = []

    for vacancy in vacancies:
        # Проверяем, содержатся ли все ключевые слова в описании вакансии
        if all(word.lower() in vacancy.description.lower() for word in filter_words):
            filtered_vacancies.append(vacancy)

    return filtered_vacancies
