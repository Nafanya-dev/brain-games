from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def data():
    question = randint(1, 100)
    right_answer = 'yes'
    if question % 2 != 0:
        right_answer = 'no'
    return question, right_answer
