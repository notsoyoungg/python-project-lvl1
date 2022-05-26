from random import choice
from random import randint

RULES = 'What is the result of the expression?'


def generate_round():
    action = choice(('*', '+', '-'))
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    question = f'{num1} {action} {num2}'
    if action == '*':
        correct_answer = num1 * num2
    if action == '+':
        correct_answer = num1 + num2
    if action == '-':
        correct_answer = num1 - num2
    return question, str(correct_answer)
