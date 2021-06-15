import random , sys #imports random.randint() and sys.exit() functions

print('ROCK, PAPER, SCISSORS')

#these variables keep track of wins, losses and ties
wins = 0
losses = 0
ties = 0

#this is the main game loop
while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    #this is the player input loop
    while True:
        print('Enter your move. (r)ock, (p)aper, (s)cissors or (q)')
        playerMove = input() #takes player input
        if playerMove == 'q':
            sys.exit() #quits the program
        if playerMove == 'x':
            print('You "Win" ;-)')
            sys.exit()  # "Cheat mode", quits the program
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break #break out of player input loop
        print ('Type one of r, p, s or q')

    #display what the player choses
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    #display computer choice, using dictionary
    computerMove = random.sample(['r', 'p', 's'], 1)[0]
    choices = {'r': 'ROCK',
               'p': 'PAPER',
               's': 'SCISSORS'
               }
    print(choices[computerMove])


    #display and record the win/loss/tie
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You Win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You Win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You Win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You Lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You Lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You Lose!')
        losses = losses + 1


