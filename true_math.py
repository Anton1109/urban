from math import inf

def true_divide (first, second):
    if second != 0:
        try:
            answer = int(first / second)

        except ZeroDivisionError:
            answer = inf

        print(answer)

