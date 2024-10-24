def fake_divide (first, second):
    if second != 0:
        try:
            answer = int(first / second)

        except ZeroDivisionError:
            answer = 'Ошибка'

        print(answer)



