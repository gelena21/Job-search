import requests
import json


class Api:
    """
    Класс для доступа к API HeadHunter и Superjob.
    """

    def __init__(self, platform):
        self.platform = platform

    def send_request(self, search_query):
        """
        Отправляет запрос к API.

        Parameters:
        - search_query (str): Поисковый запрос.

        Returns:
        - requests.Response: Ответ от API.
        """

        if self.platform == 'Headhunter':
            url = f'https://api.hh.ru/vacancies/?text={search_query}'
        elif self.platform == 'Superjob':
            url = f'https://api.superjob.ru/vacancies/?text={search_query}'

        response = requests.get(url)

        return response

    def get_vacancies(self, search_query):
        """
        Получает вакансии из выбранной платформы.

        Parameters:
        - search_query (str): Поисковый запрос.

        Returns:
        - list: Список вакансий.
        """

        response = self.send_request(search_query)

        if response.status_code == 200:
            data = json.loads(response.text)
            vacancies = []

            for vacancy_data in data['items']:
                vacancy = Vacancy(vacancy_data['title'], vacancy_data['href'],
                              vacancy_data['salary'], vacancy_data['experience'])
                vacancies.append(vacancy)

            return vacancies
        else:
            raise Exception(f'Ошибка запроса: {response.status_code}')
class Vacancy:
    def __init__(self, title, link, salary, experience):
        self.experience = experience
        self.title = title
        self.link = link
        self.salary = salary

        def compare_salary(self, other_vacancy):
            """
            Сравнивает зарплату текущей вакансии с другой вакансией.

            Parameters:
            - other_vacancy (Vacancy): Другая вакансия для сравнения.

            Returns:
            - int: Результат сравнения (-1, 0, 1).
            """
            self_salary = self.extract_salary_value(self.salary)
            other_salary = self.extract_salary_value(other_vacancy.salary)

            return (self_salary > other_salary) - (self_salary < other_salary)

        def get(self, key):
            """
            Получает значение из словаря.

            Parameters:
            - key (str): Ключ.

            Returns:
            - str: Значение.
            """
            if key in self.__dict__:
                return self.__dict__[key]
            else:
                return None

    def validate_data(self):
        """
        Валидация данных вакансии.

        Returns:
        - bool: True, если данные валидны, False в противном случае.
        """
        return all([self.title, self.link, self.salary, self.experience])

    def extract_salary_value(self, salary):
        """
        Извлекает числовое значение зарплаты из строки.

        Parameters:
        - salary (str): Строка с зарплатой.

        Returns:
        - int: Числовое значение зарплаты.
        """
        salary_start = salary.find('от')
        if salary_start != -1:
            salary = salary[salary_start + 3:]

        salary_end = salary.find('руб.')
        if salary_end != -1:
            salary = salary[:salary_end]

        try:
            return float(salary.replace(' ', ''))
        except ValueError:
            return None

    def __str__(self):
        """
        Возвращает строковое представление объекта вакансии.

        Returns:
        - str: Строковое представление вакансии.
        """
        return f"{self.title} ({self.salary}): {self.experience}"
