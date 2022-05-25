from random import randint

GAME_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game():
    number = randint(1, 100)
    return(number, check_for_prime(number))


def check_for_prime(num):
    divisor = 2
    while num % divisor != 0:
        divisor += 1
    if divisor == num:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return(correct_answer)
