from random import randint

RULE = "What number is missing in the progression?"


def get_progression(first_term=0, diff=2, num_of_members=9):
    progression = [first_term]
    for _ in range(num_of_members):
        progression.append(progression[-1] + diff)
    return progression


def get_question_string(progression, position):
    question_string = []
    for char in progression:
        question_string.append(str(char))
    question_string.append(question_string[position])
    question_string[position] = '..'
    return question_string


def get_num_position():
    START_POSITION = 0
    END_POSITION = 9
    return randint(START_POSITION, END_POSITION)


def get_arguments():
    MIN_INITIAL_RANGE = 1
    MAX_INITIAL_RANGE = 100
    MIN_DIFF = 2
    MAX_DIFF = 10

    first_term = randint(MIN_INITIAL_RANGE, MAX_INITIAL_RANGE)
    diff = randint(MIN_DIFF, MAX_DIFF)
    progression = get_progression(first_term, diff)
    position = get_num_position()
    return (get_question_string(progression, position),)


def get_round(question_string):
    right_answer = question_string[-1]
    question = ' '.join(question_string[:-1])
    return question, right_answer
