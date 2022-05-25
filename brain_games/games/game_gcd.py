from random import randint

GAME_QUESTION = 'Find the greatest common divisor of given numbers.'


def game():
    a = randint(1, 50)
    b = randint(1, 50)
    question = (f'{a} {b}')
    return(question, find_HCF(a, b))


def find_HCF(num1, num2):
    max_divisor = num1
    if num1 % num2 == 0:
        max_divisor = num2
    else:
        biggest_num = max(num2, num1)
        smallest_num = min(num2, num1)
        result = biggest_num % smallest_num
        while result != 0:
            result = biggest_num % smallest_num
            if biggest_num / smallest_num == int(biggest_num / smallest_num):
                max_divisor = smallest_num
                break
            biggest_num = smallest_num
            smallest_num = result
    return(max_divisor)