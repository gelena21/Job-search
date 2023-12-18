class Vacancy:
    def __init__(self, title, link, salary):
        self.title = title
        self.link = link
        self.salary = salary
        self.check_salary()

    def check_salary(self):
        if self.salary and isinstance(self.salary, dict):
            from_ = self.salary.get("from")
            to = self.salary.get("to")
            self.salary["from"] = from_ if from_ else 0
            self.salary["to"] = to if to else 0
        else:
            self.salary = {
                "from": 0,
                "to": 0,
            }

    def __str__(self):
        """
        Возвращает строковое представление объекта вакансии.

        Returns:
        - str: Строковое представление вакансии.
        """
        return f"{self.title} ({self.salary})"
