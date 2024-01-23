from datetime import datetime #Імпортуємо модуль datetime


def get_days_from_today(date):  # Визначаєм функцію
    current_date = datetime.today()  # Поточна дата
    return current_date.toordinal() - date.toordinal()  # Повертаємо розрахунок кількості днів


def get_days_from_today(date):  # Визначаєм функцію
    current_date = datetime.today()  # Поточна дата
    return current_date.toordinal() - date.toordinal()  # Повертаємо розрахунок кількості днів


while True:
    date_string1 = input("Введіть дату у форматі 'РРРР-ММ-ДД' (наприклад: 2020-10-09)")  # Зчитуємо дату у вигляді рядка
    try:
        datetime_object = datetime.strptime(date_string1, "%Y-%m-%d")  # Перетворення рядка в об'єкт datetime
        print(get_days_from_today(datetime_object))  # Викликаєм функцію і друкуємо результат
        break  # Виходим з циклу
    except ValueError:  # Обробляєм помилку з неправильно введеними даними
        print("Неправильно введена дата.")  # Повідомляєм користувача про неправильно введену дату
        continue  # Йдем на наступну ітерацію циклу
