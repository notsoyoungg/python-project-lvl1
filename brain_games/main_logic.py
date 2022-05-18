import prompt


def main(g, question):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_question)
    i = 0
    while i < 3:
      get = game()
      print(f'Question: {get[0]}')
      answer = prompt.string('Your answer: ')
      if answer.lower() == str(get[1]).lower():
        print('Correct!')
        i += 1
        if i == 3:
          print(f'Congratulations, {name}!')
      else:
        print(f"'{answer}' is wrong answer ;( Correct answer was '{get[1]}'.")
        print(f"Let's try again, {name}")
        break
