import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            computer_guess = random.randint(low, high)
        else:
            computer_guess = low
        feedback = input(f'Is {computer_guess} too high (H), too low (L), or correct (C)?? ').lower
        if feedback == 'h':
            high = computer_guess - 1
        elif feedback == 'l':
            low = computer_guess + 1
    
    print(f'De computer heeft, {computer_guess} geraden. ')

computer_guess(1000)
