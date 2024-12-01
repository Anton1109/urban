class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class Car:
    def __init__(self, model, vin, numbers):
        self.__model = model
        self.__vin = vin
        self.__numbers = numbers

        if not self.__is_valid_vin(vin):
            raise IncorrectVinNumber(f'Некорректный тип vin номер')

        if not self.__is_valid_numbers(numbers):
            raise IncorrectCarNumbers(f'Неверная длина номера')

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')

        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')

        return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')

        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')

        return True

    def get_model(self):
        return self.__model

    def get_vin(self):
        return self.__vin

    def get_numbers(self):
        return self.__numbers

    def __str__(self):
        return f'{self.__model} успешно создан'

try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.get_model()} успешно создан')


try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.get_model()} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.get_model()} успешно создан')