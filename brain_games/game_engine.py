import prompt

ROUNDS_AMOUNT = 3


def start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULE)
    for _ in range(ROUNDS_AMOUNT):
        (question, correct_answer) = game.generate_round()
        print(f'Question: {question}')
        player_answer = prompt.string('Your answer: ')
        if player_answer.lower() == correct_answer:
            print('Correct!')
        else:
            print(f"'{player_answer}' is wrong answer ;( "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
