import random

correct_message = 'c'
higher_messgage = 'h'
lower_message = 'l'

def verify_input(value): 
    if value != correct_message or value != higher_messgage or value != lower_message: 
        print(f'Invalid input! Please enter (H) for higher, (L) for lower and (H) for correct.')


def guess(x): 
    min_cap = 1
    max_cap = x

    attempts = 0

    feedback_message = ''
    while feedback_message != correct_message: 
        if min_cap != max_cap: 
            c_guess = random.randint(min_cap, max_cap)
        else: 
            c_guess = max_cap

        feedback_message = input(f'Is the number {c_guess} too high (H), too low (L) or correct (C). - ').lower()
        verify_input(feedback_message)
        attempts = attempts + 1

        if feedback_message == higher_messgage: 
            min_cap = c_guess + 1
        elif feedback_message == lower_message: 
            max_cap = c_guess - 1

    print(f'Wohoo! The computer successfully guessed your number ({c_guess}) in {attempts} attempts!')

guess(10)







