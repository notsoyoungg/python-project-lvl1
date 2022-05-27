import prompt

ROUNDS_AMOUNT = 3


# не уверен, что правильно изменил функцию, т.к. код стал на срочку длиннее
def start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)
    for i in range(ROUNDS_AMOUNT):
        (question, correct_answer) = game.generate_round()
        print(f'Question: {question}')
        input = prompt.string('Your answer: ')
        if input.lower() == correct_answer:
            print('Correct!')
        else:
            print(f"'{input}' is wrong answer ;( "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
