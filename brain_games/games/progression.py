from random import randint

RULE = 'What number is missing in the progression?'


def generate_round():
    progression_length = randint(5, 10)
    progression_step = randint(2, 4)
    current_member = randint(1, 20)
    i = 0
    progression = []
    while i < progression_length:
        progression.append(str(current_member + progression_step))
        current_member = current_member + progression_step
        i += 1
    index_of_missing = randint(0, (len(progression) - 1))
    correct_answer = progression[index_of_missing]
    progression[index_of_missing] = '..'
    question = ' '.join(progression)
    return question, str(correct_answer)
