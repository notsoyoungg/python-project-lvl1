from random import randint

RULES = 'What number is missing in the progression?'


def generate_round():
    progression_length = randint(5, 10)
    progression_step = randint(2, 4)
    first_member = randint(1, 20)
    i = 0
    progression = []
    while i < progression_length:
        progression.append(first_member + progression_step)
        first_member = first_member + progression_step
        i += 1
    index_of_missing = randint(0, (len(progression) - 1))
    correct_answer = progression[index_of_missing]
    progression[index_of_missing] = '..'
    question = ''
    for i in progression:
        question = question + str(i) + ' '
    return question.strip(), str(correct_answer)
