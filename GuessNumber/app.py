import random


def guess_number(x):
    print("=========================")
    print("Welcome to GuessTheNumber")
    print("=========================")
    print('You must to guess the number choosed by the computer...')

    random_number = random.randint(1, x)

    prediction = 0

    while prediction != random_number:
        prediction = int(input(f'Choose a number beetwen 1 y {x}: '))

        if prediction < random_number:
            print('Try with a bigger number')
        elif prediction > random_number:
            print('Try with a smaller number')
    
    print(f'Congratulations!! You guess the number {prediction} successfully')


guess_number(int(input('Please, insert a number ')))