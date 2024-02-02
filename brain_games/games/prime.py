from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num, i=2):
    if num <= 2:
        return num == 2
    if num % i == 0:
        return False
    if i * i > num:
        return True
    return is_prime(num, i + 1)


def data():
    question = randint(1, 50)
    right_answer = 'yes' if is_prime(question) else 'no'

    return question, right_answer
