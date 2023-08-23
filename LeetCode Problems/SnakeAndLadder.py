import random
def roll_dice():
    return random.randint(1, 6)
def play_turn(player, position):
    print(f"{player}'s turn. Press enter to roll the dice...")
    input()
    dice_roll = roll_dice()
    print(f"{player} rolled a {dice_roll}.")
    position += dice_roll
    if position in snakes:
        print(f"Oops! {player} got bitten by a snake and moved down to {snakes[position]}.")
        position = snakes[position]
    elif position in ladders:
        print(f"Great! {player} climbed a ladder and moved up to {ladders[position]}.")
        position = ladders[position]
    return position
def snake_and_ladder_game():
    player1 = input("Enter name of Player 1: ")
    player2 = input("Enter name of Player 2: ")
    player1_position = 0
    player2_position = 0
    while player1_position < 100 and player2_position < 100:
        player1_position = play_turn(player1, player1_position)
        print(f"{player1} is now at position {player1_position}.\n")
        if player1_position >= 100:
            print(f"Congratulations! {player1} wins!")
            break
        player2_position = play_turn(player2, player2_position)
        print(f"{player2} is now at position {player2_position}.\n")
        if player2_position >= 100:
            print(f"Congratulations! {player2} wins!")
            break
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
snake_and_ladder_game()