first_player = 'X'
second_player = 'O'

game_field = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# first player is first to make a move
current_player = first_player

row, column = input_move()
game_field[row][column] = current_player
print_field()
winner = check_winner()

if winner is not None:
    congratulate_player(winner)
    quit()

current_player = first_player if current_player == second_player else second_player