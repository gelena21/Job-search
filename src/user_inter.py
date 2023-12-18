from src.classes_api import HeadHunterAPI, SuperJobAPI
from src.savedvac import JSONSaver
from src.utils import get_top_vacancies, print_vacancies, sort_vacancies, filter_vacancies
from dotenv import load_dotenv

load_dotenv()


def user_interaction():
    # Получение выбора пользователя
    platform = input("Выберите платформу (Headhunter/Superjob): ").lower()

    if platform not in ("headhunter", "superjob"):
        print(f"Некорректная платформа {platform}. Выход из программы.")
        return

    # Инициализация соответствующего API
    if platform == "headhunter":
        api = HeadHunterAPI()
    elif platform == "superjob":
        api = SuperJobAPI()
        return api

    search_query = input("Введите поисковый запрос: ")

    # Взаимодействие с пользователем
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input(
        "Введите ключевые слова описания характеристик работника для фильтрации вакансий (через пробел): "
    ).lower().split()

    # Фильтрация вакансий
    filtered_vacancies = filter_vacancies(api.get_vacancies(search_query), filter_words)

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
        json_saver.save_to_file()
