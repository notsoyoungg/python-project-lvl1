from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    number = randint(1, 100)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer


def is_prime(num):
    divisor = 2
    while num % divisor != 0:
        divisor += 1
    if divisor == num:
        return True
    return False
