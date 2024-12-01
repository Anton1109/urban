def personal_sum(numbers):
    result = 0 # Сумма чисел
    incorrect_data = 0 # Счетчик некорректных данных

    for item in numbers:
        try:
            result += int(item) # Пробуем преобразовать в число и добавить к результату
        except (ValueError, TypeError): # Обрабатываем исключения, если элемент некорректный
            incorrect_data += 1

    return result, incorrect_data # Возвращаем кортеж

def calculate_average(numbers):

    try:

        if not isinstance(numbers, (list, tuple, set)):  # Проверяем, является ли входной аргумент коллекцией
            raise TypeError('В numbers записан некорректный тип данных')


    except TypeError:
        print("Некорректный тип данных")


        total_sum, incorrect_data = personal_sum(numbers) # Вызываем функцию personal_sum для обработки элементов

        try:
            valid_count = len(numbers) - incorrect_data
            average = total_sum / valid_count  # Вычисляем среднее, исключая деление на 0
            return average
        except ZeroDivisionError:

            return 0



    except TypeError:
        print("В numbers записан некорректный тип данных")
        return None

print(f'Результат 1: {personal_sum("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип

print(f'Результат 2: {personal_sum([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3

print(f'Результат 3: {personal_sum([567] )}') # Передана не коллекция

print(f'Результат 4: {personal_sum([42, 15, 36, 13])}') # Всё должно работать