import random
def dice_game(rounds):
    p1avgs=[]
    p2avgs=[]
    p1wins=0
    p2wins=0
    for j in range(rounds):    
        player1score=0
        player2score=0
        for j in range(5):
            player1rolls =  random.randint(1, 6)
            #    print(player1rolls)
            player1score = player1score+player1rolls
            player2rolls =  random.randint(1, 6)
            #    print(player2rolls)
            player2score = player2score+player2rolls
        player1score = player1score/5
        player2score = player2score/5
        p1avgs.append(player1score)
        p2avgs.append(player2score)
        if player2score>player1score:
            p2wins=p2wins+1
        else:
            p1wins=p1wins+1
    print('Player 1 wins: ', p1wins)
    print('Player 1 round averages: ', p1avgs)
    print('Player 2 wins: ', p2wins)
    print('Player 2 round averages: ', p2avgs)

dice_game(4)
