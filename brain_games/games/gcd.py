from random import randint
import math

RULE = "Find the greatest common divisor of given numbers."


def get_random_number():
    START_RANGE = 1
    END_RANGE = 50
    return randint(START_RANGE, END_RANGE)


def round_data(first_random_operand=get_random_number,
               second_random_operand=get_random_number):
    first_operand = first_random_operand()
    second_operand = second_random_operand()
    question = f"{first_operand} {second_operand}"
    right_answer = str(math.gcd(first_operand, second_operand))
    return question, right_answer
