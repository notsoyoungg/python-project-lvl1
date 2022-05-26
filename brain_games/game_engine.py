import prompt

ROUNDS_AMOUNT = 3


def start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)
    for i in range(ROUNDS_AMOUNT):
        (question, correct_answer) = game.generate_round()
        print(f'Question: {question}')
        inp = prompt.string('Your answer: ')
        if inp.lower() == correct_answer:
            print('Correct!')
        else:
            print(f"'{inp}' is wrong answer ;( "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
