from random import randint

game_question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game():
    number = randint(1, 100)
    divisor = 2
    while number % divisor != 0:
        divisor += 1
    if divisor == number:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return(number, correct_answer)
