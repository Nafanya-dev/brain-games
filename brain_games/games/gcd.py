from random import randint
import math

RULE = "Find the greatest common divisor of given numbers."


def get_random_number():
    START_RANGE = 1
    END_RANGE = 50
    return randint(START_RANGE, END_RANGE)


def get_arguments():
    return (get_random_number(), get_random_number())


def get_round(first_operand,
              second_operand):
    question = f"{first_operand} {second_operand}"
    right_answer = str(math.gcd(first_operand, second_operand))
    return question, right_answer
