import prompt


def main(func, variable):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(variable)
    i = 0
    while i < 3:
      anwer_or_question = func()
      print(f'Question: {anwer_or_question[0]}')
      answer = prompt.string('Your answer: ')
      if answer.lower() == str(anwer_or_question[1]).lower():
        print('Correct!')
        i += 1
        if i == 3:
          print(f'Congratulations, {name}!')
      else:
        print(f"'{answer}' is wrong answer ;( Correct answer was '{anwer_or_question[1]}'.")
        print(f"Let's try again, {name}")
        break
