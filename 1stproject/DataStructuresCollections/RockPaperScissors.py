import random


def game():
    print()
    print()
    print("=============================================")
    print("Hello Player. Welcome to Rock Paper Scissors.")
    print("=============================================")
    list_choices = ['Rock', 'Paper', 'Scissors']
    player_choice = input("Enter r for Rock, p for Paper, s for Scissors = ")
    if player_choice in 'rRsSpP':
        if player_choice in 'rR':
            player_choice = 'Rock'
        elif player_choice in 'pP':
            player_choice = 'Paper'
        else:
            player_choice = 'Scissors'
        print(f'Player choice is {player_choice}')
    else:
        print("Invalid choice. Try again!")

    computer_choice = random.choice(list_choices)
    print(f'Computer choice is {computer_choice}')
    if player_choice == computer_choice:
        print("Game is drawn.")
    elif player_choice == 'Rock' and computer_choice == 'Paper':
        print(f'Computer wins! {computer_choice} beats {player_choice}!!!')
    elif player_choice == 'Paper' and computer_choice == 'Scissors':
        print(f'Computer wins! {computer_choice} beats {player_choice}!!!')
    elif player_choice == 'Scissors' and computer_choice == 'Rock':
        print(f'Computer wins! {computer_choice} beats {player_choice}!!!')
    else:
        print(f'Player wins! {player_choice} beats {computer_choice}!!!')


while True:
    game()
