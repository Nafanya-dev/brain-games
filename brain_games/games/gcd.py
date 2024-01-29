from random import randint
import math

RULE = "Find the greatest common divisor of given numbers."


def data():
    first_operand = randint(1, 50)
    second_operand = randint(1, 50)

    question = f"{first_operand} {second_operand}"
    right_answer = str(math.gcd(first_operand, second_operand))
    return question, right_answer
