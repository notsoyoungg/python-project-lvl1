from random import randint

game_question = 'Answer "yes" if the number is even, otherwise answer "no".'


def game():
    question = randint(1, 100)
    if question % 2 == 0:
        correct_answer = 'yes'
    if question % 2 != 0:
        correct_answer = 'no'
    return(question, correct_answer)
