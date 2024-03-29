from datetime import datetime, timedelta  # Імпортуєм модуль і потрібні функції


def get_upcoming_birthdays(users):  # Визначаєм функцію
    today = datetime.today().date()  # Визначаєм сьогоднішню дату
    today_str = today.strftime("%Y.%m.%d")  # переводим обьєкт часу в рядок
    users_new = []  # Створюєм новий список для зберігання привітань
    for user in users:  # Проходимся по кожному елементу списку
        birthday_this_year_str = today_str[:4] + user["birthday"][4:]  # Додаємо поточний рік і зберігаєм в рядок
        birthday_this_year = datetime.strptime(birthday_this_year_str, "%Y.%m.%d").date()  # Створення обьєкту часу
        if birthday_this_year < today:  # Перевіряєм, чи вже минув день народження в цьому році
            birthday_this_year_str = str(int(today_str[:4])+1) + user["birthday"][4:]  # Збільшуєм рік на 1
            birthday_this_year = datetime.strptime(birthday_this_year_str, "%Y.%m.%d").date()  # Створення обьєкту часу
        difference = birthday_this_year.toordinal() - today.toordinal()  # Рахуєм різницю між днем народження та поточним днем
        if difference < 7:  # Якщо різниця менше 7 днів
            day_of_week = birthday_this_year.isoweekday()  # Визначаєм день тижня
            if day_of_week == 7:  # Якщо це неділя
                future_date = birthday_this_year + timedelta(days=1)  # Додаємо 1 день до  дати
                birthday_this_year_str = future_date.strftime("%Y.%m.%d")  # переводим обьєкт часу в рядок
            elif day_of_week == 6:  # Якщо це субота
                future_date = birthday_this_year + timedelta(days=2)  # Додаємо 2 дня до  дати
                birthday_this_year_str = future_date.strftime("%Y.%m.%d")  # переводим обьєкт часу в рядок
            user.update({"congratulation_date": birthday_this_year_str})   # створюєм ключ congratulation_date, дані якого у форматі рядка 'рік.місяць.дата'
            user.pop("birthday")  # видаляєм ключ "birthday"
            users_new.append(user)  # добавляєм словник в список
    return users_new  #  повертаєм Список привітань на цьому тижні

users = [  # список cлоників для прикладу
    {"name": "John Wick", "birthday": "1985.01.29"},
    {"name": "Lara Croft", "birthday": "1990.01.01"},
    {"name": "John Doe", "birthday": "1985.01.28"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)  # викликаєм функцію і зберігаєм в змінній
print("Список привітань на цьому тижні:", upcoming_birthdays)  # друкуєм список привітань
