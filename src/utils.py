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
    Фильтрует вакансии по ключевым словам.

    Parameters:
    - vacancies (List[dict]): Список словарей с данными о вакансиях.
    - filter_words (List[str]): Список ключевых слов для фильтрации.

    Returns:
    - List[dict]: Отфильтрованный список вакансий.
    """
    filtered_vacancies = []

    for vacancy in vacancies:
        if vacancy.get('salary') is not None:
            description = vacancy.get('profession', '') + vacancy.get('candidat', '')
            # Для вакансий от SuperJob
            if any(word.lower() in description.lower() for word in filter_words):
                filtered_vacancies.append(vacancy)
            # Для вакансий от HeadHunter
            elif 'snippet' in vacancy and 'requirement' in vacancy['snippet'] and any(
                    word.lower() in vacancy['snippet']['requirement'].lower() for word in filter_words):
                filtered_vacancies.append(vacancy)
        else:
            print(f"Вакансия без указанной зарплаты: {vacancy}")

    return filtered_vacancies
