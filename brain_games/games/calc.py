from random import randint

RULE = "What is the result of the expression?"


def get_random_operator():
    MIN_INDEX = 0
    MAX_INDEX = 2
    operators = ['+', '-', '*']
    return operators[randint(MIN_INDEX, MAX_INDEX)]


def get_random_num():
    START_RANGE = 1
    END_RANGE = 10
    return randint(START_RANGE, END_RANGE)


def get_arguments():
    return (get_random_num(), get_random_num(), get_random_operator())


def round_data(first_num,
               second_num,
               operator):
    first_operand = str(first_num)
    second_operand = str(second_num)

    question = f"{first_operand} {operator} {second_operand}"
    right_answer = str(eval(first_operand + operator + second_operand))
    return question, right_answer
