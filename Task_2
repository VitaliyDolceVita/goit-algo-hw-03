import random  # Імпортуємо модуль випадкових чисел


def get_numbers_ticket(min1, max1, quantity):  # Визначаєм функцію з трьома параметрами
    numbers = []  # Створюємо пустий список для зберігання номерів
    for i in range(min1, max1 + 1, 1):  # Запускаємо цикл для генерації чисел
        numbers.append(i)  # добавляєм число в список
    selected_numbers = random.sample(numbers, quantity)  # берем  quantity-кількість унікальних чисел
    selected_numbers.sort()  # сортуємо числа
    return selected_numbers  # повертаємо відсортовані числа


while True:
    min_number = input("Введіть мінімальне число не менше одиниці:")
    if min_number.isdigit():
        min_number = int(min_number)
        if min_number < 1:
            print("Введене число менше одиниці. Введіть заново")
            continue
        else:
            break
    else:
        print("Ви ввели не число. Введіть заново")
        continue

while True:
    max_number = input("Введіть максимальне можливе число у наборі (не більше 1000):")
    if max_number.isdigit():
        max_number = int(max_number)
        if max_number > 1000:
            print("Введене число більше 1000. Введіть заново")
            continue
        else:
            break
    else:
        print("Ви ввели не число. Введіть заново")
        continue

while True:
    q_number = input("Введіть кількість чисел, які потрібно вибрати (значення між мінімальним і максимальним):")
    if q_number.isdigit():
        q_number = int(q_number)
        if max_number < q_number or q_number < min_number:
            print("Введене число не між мінімальним і максимальним. Введіть заново")
            continue
        else:
            break
    else:
        print("Ви ввели не число. Введіть заново")
        continue


lottery_numbers = get_numbers_ticket(min_number, max_number, q_number)  # викликаємо функцію
print("Ваші лотерейні числа:", lottery_numbers)  # Виводимо лотерейні числа на екран
