from typing import List

from src.vacancies import Vacancy


def sort_vacancies(vacancies):
    """
    Сортирует вакансии по зарплате.

    Parameters:
    - vacancies (List[Dict]): Список вакансий.

    Returns:
    - List[Dict]: Отсортированный список вакансий.
    """
    return sorted(vacancies, key=lambda x: x.get('salary', 0))


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
    - vacancies (List[Dict]): Список вакансий.
    """
    for i, vacancy in enumerate(vacancies, start=1):
        title = vacancy.get('title', 'Название вакансии отсутствует')
        salary = vacancy.get('salary', 'Зарплата не указана')
        link = vacancy.get('link', 'Ссылка не указана')
        print(f"{i}. {title} ({salary}): {link}")


def filter_vacancies(vacancies, filter_words):
    """
    Фильтрует вакансии по заданным ключевым словам.

    Parameters:
    - vacancies (list): Список вакансий.
    - filter_words (list): Ключевые слова.

    Returns:
    - list: Список отфильтрованных вакансий.
    """

    filtered_vacancies = []
    for vacancy in vacancies:
        for filter_word in filter_words:
            if filter_word in vacancy.experience:
                filtered_vacancies.append(vacancy)
                break

    return filtered_vacancies

