import prompt


def start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_QUESTION)
    ROUNDS_AMOUNT = 3
    for i in range(ROUNDS_AMOUNT):
        data = game.game()
        print(f'Question: {data[0]}')
        inp = prompt.string('Your answer: ')
        if inp.lower() == str(data[1]).lower():
            print('Correct!')
        else:
            print(f"'{inp}' is wrong answer ;( Correct answer was '{data[1]}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
