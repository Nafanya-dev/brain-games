from random import randint

RULE = "What number is missing in the progression?"


def get_progression():
    MIN_INITIAL_RANGE = 1
    MAX_INITIAL_RANGE = 100
    MIN_DIFF = 2
    MAX_DIFF = 10

    first_term = str(randint(MIN_INITIAL_RANGE, MAX_INITIAL_RANGE))
    diff = randint(MIN_DIFF, MAX_DIFF)
    progression = [first_term]

    while len(progression) < 10:
        progression.append(str(int(progression[-1]) + diff))
    return progression


def get_question_string(progression_list, number_position):
    progression = progression_list[:]
    progression[number_position] = '..'
    return ' '.join(progression), progression_list[number_position]


def get_num_position():
    START_POSITION = 0
    END_POSITION = 9
    return randint(START_POSITION, END_POSITION)


def get_arguments():
    return (get_progression(), get_num_position())


def round_data(progression,
               position):
    question, right_answer = get_question_string(progression,
                                                 position)
    return question, right_answer
