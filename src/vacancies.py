class Vacancy:
    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

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

    def validate_data(self):
        """
        Валидация данных вакансии.

        Returns:
        - bool: True, если данные валидны, False в противном случае.
        """
        return all([self.title, self.link, self.salary, self.description])

    def extract_salary_value(self, salary):
        """
        Извлекает числовое значение зарплаты из строки.

        Parameters:
        - salary (str): Строка с зарплатой.

        Returns:
        - int: Числовое значение зарплаты.
        """
        try:
            salary_values = [int(s) for s in salary.replace(" ", "").split("-")]
            return sum(salary_values) // len(salary_values)
        except (ValueError, TypeError):
            return 0

    def __str__(self):
        """
        Возвращает строковое представление объекта вакансии.

        Returns:
        - str: Строковое представление вакансии.
        """
        return f"{self.title} ({self.salary}): {self.description}"
