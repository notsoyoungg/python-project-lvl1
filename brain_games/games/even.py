from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    question = randint(1, 100)
    correct_answer = 'yes'
    if question % 2 != 0:
        correct_answer = 'no'
    return question, correct_answer
