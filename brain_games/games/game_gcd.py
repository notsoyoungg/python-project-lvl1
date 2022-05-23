from random import randint

game_question = 'Find the greatest common divisor of given numbers.'


def game():
    a = randint(1, 100)
    b = randint(1, 100)
    question = (f'{a} {b}')
    if a % b == 0:
        return(question, b)
    if b % a == 0:
        return(question, a)
    else:
        x = max(b, a)
        y = min(b, a)
        z = x % y
        while z != 0:
            z = x % y
            if x / y == int(x / y):
                return(question, y)
                break
            x = y
            y = z
