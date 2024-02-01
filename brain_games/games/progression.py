from random import randint

RULE = "What number is missing in the progression?"


def data():
    first_num = str(randint(1, 100))
    stride_length = randint(2, 10)
    number_position = randint(0, 9)
    progression = [first_num]

    while len(progression) < 10:
        progression.append(str(int(progression[-1]) + stride_length))

    right_answer = progression[number_position]
    progression[number_position] = '..'
    question = ' '.join(progression)

    return question, right_answer
