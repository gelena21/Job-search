from src.classes_api import HeadHunterAPI, SuperJobAPI
from src.savedvac import JSONSaver
from src.vacancies import Vacancy
from utils import filter_vacancies, get_top_vacancies, print_vacancies, sort_vacancies
from dotenv import load_dotenv
load_dotenv()


def user_interaction():
    # Создание экземпляров классов для работы с API и вакансиями
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()
    json_saver = JSONSaver("vacancies.json")

    hh_api.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                                    ' (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    # Получение вакансий с разных платформ
    hh_vacancies = hh_api.get_vacancies("Python")
    superjob_vacancies = superjob_api.get_vacancies("Python")

    # Создание вакансий для примера
    vacancy1 = Vacancy(
        "Python Developer",
        "https://hh.ru/vacancy/123456",
        "100 000-150 000 руб.",
        "Требования: опыт работы от 3 лет...",
    )
    vacancy2 = Vacancy(
        "Data Scientist",
        "https://superjob.ru/vacancy/789012",
        "120 000-160 000 руб.",
        "Требования: знание Python, опыт с ML...",
    )

    # Сохранение вакансий в файл
    json_saver.add_vacancy(vacancy1)
    json_saver.add_vacancy(vacancy2)

    # Взаимодействие с пользователем
    print("Доступные платформы: HeadHunter, SuperJob")

    # Выбор платформы
    platform = input("Выберите платформу (HeadHunter/SuperJob): ").capitalize()

    if platform not in ["HeadHunter", "SuperJob"]:
        print("Некорректная платформа. Выход из программы.")
        return

    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input(
        "Введите ключевые слова для фильтрации вакансий (через пробел): "
    ).split()

    # Получение вакансий с выбранной платформы
    platform_vacancies = (
        hh_vacancies if platform == "HeadHunter" else superjob_vacancies
    )

    # Фильтрация вакансий
    filtered_vacancies = filter_vacancies(platform_vacancies, filter_words)

    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    # Сортировка вакансий
    sorted_vacancies = sort_vacancies(filtered_vacancies)

    # Получение топ-N вакансий
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    # Вывод вакансий в консоль
    print("Результаты поиска:")
    print_vacancies(top_vacancies)

    # Спросить пользователя, хочет ли он сохранить найденные вакансии
    save_choice = input("Хотите сохранить найденные вакансии? (да/нет): ").lower()
    if save_choice == "да":
        for vacancy in top_vacancies:
            json_saver.add_vacancy(vacancy)


if __name__ == "__main__":
    user_interaction()
