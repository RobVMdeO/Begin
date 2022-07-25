import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Adivina un número entre 1 y {x}: '))
        if guess < random_number:
            print('Lo siento, intenta de nuevo. Muy bajo')
        elif guess > random_number:
            print('Lo siento, intenta de nuevo. Muy alto.')

    print(f'Bravo!!! Felicitaciones!!. Has adivinado el número {random_number} correctamente!!')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Es {guess} muy grande (G), muy chico (CH), o es correcto (C)?? ').lower()
        if feedback == 'g':
            high = guess - 1
        elif feedback == 'ch':
            low = guess + 1

    print(f'Siii!!! He adivinado tu número, {guess}, correctamente!')


computer_guess(100)