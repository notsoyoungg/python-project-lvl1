from random import randint

game_question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game():
    number = randint(1, 100)
    if number % 2 != 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return(number, correct_answer)
