from random import randint
from math import sqrt

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    number = randint(1, 100)
    correct_answer = 'no'
    if is_prime(number):
        correct_answer = 'yes'
    return number, correct_answer


def is_prime(num):
    if num == 1:
        return False
    divisor = 2
    while divisor <= sqrt(num) and num % divisor != 0:
        divisor += 1
    if divisor < sqrt(num):
        return False
    return True
