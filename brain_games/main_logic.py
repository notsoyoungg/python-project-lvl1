import prompt


def logic(func, variable):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(variable)
    i = 0
    while i < 3:
        data = func()
        print(f'Question: {data[0]}')
        inp = prompt.string('Your answer: ')
        if inp.lower() == str(data[1]).lower():
            print('Correct!')
            i += 1
            if i == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{inp}' is wrong answer ;( Correct answer was '{data[1]}'.")
            print(f"Let's try again, {name}")
            break
