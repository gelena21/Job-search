def sort_vacancies(vacancies):
    """
    Сортирует вакансии по зарплате.

    Parameters:
    - vacancies (List[Dict]): Список вакансий.

    Returns:
    - List[Dict]: Отсортированный список вакансий.
    """
    return sorted(vacancies, key=lambda vacancy: (vacancy.salary["from"] + vacancy.salary["to"]) / 2)


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
    for num_vacancy, vacancy in enumerate(vacancies, start=1):
        title = vacancy.title if hasattr(vacancy, 'title') else 'Название вакансии отсутствует'
        salary = getattr(vacancy, 'salary', 'Зарплата не указана')
        link = getattr(vacancy, 'link', 'Ссылка не указана')

        print(f"{num_vacancy}. {title} ({salary}): {link}")


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
            if filter_word in vacancy.title.lower():
                filtered_vacancies.append(vacancy)
                break

    return filtered_vacancies
