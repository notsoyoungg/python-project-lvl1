from random import randint

RULE = 'Find the greatest common divisor of given numbers.'


def generate_round():
    random_number1 = randint(1, 50)
    random_number2 = randint(1, 50)
    question = (f'{random_number1} {random_number2}')
    return question, str(find_gcd(random_number1, random_number2))


def find_gcd(num1, num2):
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
    return max_divisor
