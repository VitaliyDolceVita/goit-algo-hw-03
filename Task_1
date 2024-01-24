from datetime import datetime  # Імпортуєм модуль


def get_days_from_today(date):  # Визначаєм функцію
    while True:  # Створююєм безкінечний цикл
        try:
            datetime_object = datetime.strptime(date, "%Y-%m-%d")  # Перетворення рядка в об'єкт datetime
            break  # Виходим з циклу
        except ValueError:  # Обробляєм помилку з неправильно введеними даними
            print("Неправильно введена дата.")  # Повідомляєм користувача про неправильно введену дату
            date = input("Введіть дату у форматі 'РРРР-ММ-ДД' (наприклад: 2020-10-09)")  # Зчитуємо дату у вигляді рядка
            continue  # Йдем на наступну ітерацію циклу
    current_date = datetime.today()  # Поточна дата
    return current_date.toordinal() - datetime_object.toordinal()  # Повертаємо розрахунок кількості днів


date_string = input("Введіть дату у форматі 'РРРР-ММ-ДД' (наприклад: 2020-10-09)")  # Зчитуємо дату у вигляді рядка
print(get_days_from_today(date_string))  # Викликаєм функцію і друкуємо результат
