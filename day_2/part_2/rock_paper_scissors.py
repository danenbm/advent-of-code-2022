choice = {
   'A': 'rock',
   'B': 'paper',
   'C': 'scissors',
}

player_outcome = {
   'X': 'lose',
   'Y': 'draw',
   'Z': 'win'
}

score = {
    'rock':     1,
    'paper':    2,
    'scissors': 3,
    'lose':     0,
    'draw':     3,
    'win':      6
}


def play_game(opponent_choice, player_outcome):
    if player_outcome == 'draw':
        player_choice = opponent_choice
    elif opponent_choice == 'rock':
        if player_outcome == 'lose':
            player_choice = 'scissors'
        else:
            player_choice = 'paper'
    elif opponent_choice == 'paper':
        if player_outcome == 'lose':
            player_choice = 'rock'
        else:
            player_choice = 'scissors'       
    elif opponent_choice == 'scissors':
        if player_outcome == 'lose':
            player_choice = 'paper'
        else:
            player_choice = 'rock'

    return score[player_outcome] + score[player_choice]


with open("../input.txt") as file:
    total = 0
    for line in file:
        words = line.split()
        total += play_game(choice[words[0]], player_outcome[words[1]])

    print("\nTotal score:", total)
