from random import randint

game_question = 'Find the greatest common divisor of given numbers.'


def game():
    a = randint(1, 100)
    b = randint(1, 100)
    question = (f'{a} {b}')
    if a % b == 0:
        cortege = (question, b)
        return(cortege)
    if b % a == 0:
        cortege = (question, a)
        return(cortege)
    if a > b:
        c = a % b
        while c != 0:
            c = a % b
            if a / b == int(a / b):
                cortege = (question, b)
                return(cortege)
                break
            a = b
            b = c
    else:
        c = b % a
        while c != 0:
            c = b % a
            if b / a == int(b / a):
                cortege = (question, a)
                return(cortege)
                break
            b = a
            a = c
