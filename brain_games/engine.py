import prompt


def play(game):
    number_of_rounds = 3
    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print(game.RULE)
    for _ in range(number_of_rounds):
        question, right_answer = game.round_data()
        print(f"Question: {question}")
        user_answer = prompt.string("Yuor answer: ")
        if right_answer == user_answer:
            print('Correct!')
        else:
            print(
                f'\'{user_answer}\' is wrong answer ;(.'
                f' Correct answer was \'{right_answer}\'.'
            )
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
