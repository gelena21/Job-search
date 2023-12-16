from src.classes_api import HeadHunterAPI, SuperJobAPI
from src.savedvac import JSONSaver
from src.vacancies import Vacancy
from utils import filter_vacancies, get_top_vacancies, print_vacancies, sort_vacancies
from dotenv import load_dotenv

load_dotenv()

hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()
json_saver = JSONSaver("vacancies.json")


def user_interaction():
    # Получение выбора пользователя
    platform = input("Выберите платформу (Headhunter/Superjob): ").lower()
    print(f"DEBUG: Приведенная платформа: {platform}")

    if platform != "headhunter" and platform != "superjob":
        print(f"Некорректная платформа {platform}. Выход из программы.")
        return
    api = None
    # Инициализация соответствующего API
    if platform == "headhunter":
        api = HeadHunterAPI()
        hh_api.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

    elif platform == "superjob":
        api = SuperJobAPI()
    else:
        print("Некорректная платформа. Выход из программы.")
        return
    search_query = input("Введите поисковый запрос: ")
    # Получение вакансий
    vacancies = api.get_vacancies(search_query)

    # Создание экземпляра класса для сохранения вакансий
    json_saver = JSONSaver("vacancies.json")

    # Взаимодействие с пользователем
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input(
        "Введите ключевые слова описания характеристик работника для фильтрации вакансий (через пробел): ").split()

    # Фильтрация вакансий
    filtered_vacancies = filter_vacancies(vacancies, filter_words)

    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    sorted_vacancies = sort_vacancies(filtered_vacancies)

    # Получение топ-N вакансий
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    # Вывод вакансий в консоль
    print("Результаты поиска:")
    print_vacancies(top_vacancies)

    # Спросить пользователя, хочет ли он сохранить найденные вакансии
    save_choice = input("Хотите сохранить найденные вакансии? (да/нет): ").lower()
    if save_choice == "да":
        json_saver = JSONSaver("vacancies.json")
        for vacancy in top_vacancies:
            json_saver.add_vacancy(vacancy)


if __name__ == "__main__":
    user_interaction()
