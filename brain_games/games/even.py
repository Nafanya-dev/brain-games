from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_random_number():
    START_RANGE = 1
    END_RANGE = 100
    return randint(START_RANGE, END_RANGE)


def get_arguments():
    return (get_random_number(),)


def get_round(num):
    question = num
    right_answer = 'yes'
    if question % 2 != 0:
        right_answer = 'no'
    return question, right_answer
