from random import randint

RULE = "What is the result of the expression?"


def data():
    operators = ['+', '-', '*']
    operator = operators[randint(0, 2)]
    first_operand = str(randint(1, 10))
    second_operand = str(randint(1, 10))

    question = f"{first_operand} {operator} {second_operand}"
    right_answer = str(eval(first_operand + operator + second_operand))
    return question, right_answer
