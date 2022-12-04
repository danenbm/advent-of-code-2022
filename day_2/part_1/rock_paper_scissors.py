choice = {
   'A': 'rock',
   'B': 'paper',
   'C': 'scissors',
   'X': 'rock',
   'Y': 'paper',
   'Z': 'scissors'
}

score = {
    'rock':     1,
    'paper':    2,
    'scissors': 3,
    'lose':     0,
    'draw':     3,
    'win':      6
}


def play_game(opponent, player):
    if opponent == player:
        outcome = 'draw'
    elif opponent == 'rock':
        if player == 'paper':
            outcome = 'win'
        else:
            outcome = 'lose'
    elif opponent == 'paper':
        if player == 'scissors':
            outcome = 'win'
        else:
            outcome = 'lose'
    elif opponent == 'scissors':
        if player == 'rock':
            outcome = 'win'
        else:
            outcome = 'lose'

    return score[outcome] + score[player]


with open("../input.txt") as file:
    total = 0
    for line in file:
        words = line.split()
        total += play_game(choice[words[0]], choice[words[1]])

    print("\nTotal score:", total)
