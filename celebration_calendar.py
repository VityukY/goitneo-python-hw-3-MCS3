from collections import defaultdict
from datetime import datetime


def get_birthdays_per_week(
    data,
):  # перевірки на: пусте імя, на довжину даних, на відповідність полів (name/birthday)
    if not data:
        print("There is no birthdays to analize")
        return

    grouped_days = defaultdict(list)
    today = datetime.today().date()

    for user in data:
        if "name" not in user.keys() or "birthday" not in user.keys():
            print("data must be containe by name and dates (datetime(YYYY, MM, DD))")
            return
        if len(user) != 2:
            print("Incorect data type")
            return

        name = user["name"]  # визначаєм імя
        if not name:
            print("All users must have name, or code atleast")
            return

        birthday = user["birthday"].date()  # Конвертуємо до типу date*
        birthday_this_year = birthday.replace(
            year=today.year
        )  # змінюєм рік на поточний

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)  #

        delta_days = (birthday_this_year - today).days  # виводим різницю між днями
        if delta_days >= 7:
            continue

        day = datetime.strftime(birthday_this_year, "%A")  # визначаємо день тижня

        weekends = [
            "Saturday",
            "Sunday",
        ]

        if day in weekends:
            day = "Monday"  # назначаємо на понеділок вітання по вихідним
        grouped_days[day].append(name)  # групуємо по дню і забиваєм іменами

    for key, value in grouped_days.items():
        val = ", ".join(value)  # збираєм імена у формат
        print("{:<10}:{:<10}".format(key, val))  # виводим форматовану відповідь


"""
Дані для тестування функцій
data = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 4)},
    {"name": "Todd Howard", "birthday": datetime(1955, 10, 5)},
    {"name": "Mate Damon", "birthday": datetime(1955, 10, 6)},
    {"name": "Greek Salad", "birthday": datetime(1955, 10, 7)},
    {"name": "David Bowwie", "birthday": datetime(1955, 10, 8)},
    {"name": "Sem Winchester", "birthday": datetime(1955, 10, 9)},
    {"name": "Din Winchester", "birthday": datetime(1955, 10, 10)},
    {"name": "Gabe Newell ", "birthday": datetime(1955, 10, 11)},
    {"name": "Abby Last", "birthday": datetime(1955, 10, 12)},
    {"name": "Steve Rogers", "birthday": datetime(1955, 10, 13)},

    birthday_callendar(data) # 
]
"""
if __name__ == "__main__":
    data = [
        {"names": "Bill Gates", "birthday": datetime(1955, 10, 4)},
    ]
    get_birthdays_per_week(data)
