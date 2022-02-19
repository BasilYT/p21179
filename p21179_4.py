import random
times = 0
W_1 = 0  # 1st player's wins
W_2 = 0  # 2nd player's wins
D = 0  # Draws
print("Round 1, BEGIN!")
while times < 100:
    times += 1
    xartia = []
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    color = ["H", "S", "C", "D"]
    for i in xarti:
        for j in color:
            xartia.append([i, j])
    random.shuffle(xartia)
    player1 = []
    sum1 = 0
    while sum1 < 16:
        sum1 = 0
        player1.append(xartia.pop())
        print(player1)
        for card in player1:
            if card[0] in figures:
                sum1 = sum1+10
            else:
                sum1 = sum1+card[0]
        print(sum1)
    if sum1 > 21:
        print("P2 wins!")
        W_2 += 1
    else:
        print("P2 joins the game")
        player2 = []
        sum2 = 0
        while sum2 < 16:
            sum2 = 0
            player2.append(xartia.pop())
            print(player2)
            for card in player2:
                if card[0] in figures:
                    sum2 = sum2+10
                else:
                    sum2 = sum2+card[0]
            print(sum2)
        if sum2 > 21:
            sum2 = 0
        if sum1 > sum2:
            print("P1 wins!")
            W_1 += 1
        elif sum2 > sum1:
            print("P2 wins!")
            W_2 += 1
        else:
            print("draw!")
            D += 1
print("Game over!")
print("Player 1 won", W_1, "times")
print("Player 2 won", W_2, "times")
print("There were", D, "draws")
times = 0
W_1 = 0
W_2 = 0
D = 0
print("Round 2, BEGIN!")
while times < 100:
    times += 1
    xartia = []
    xartia1 = []
    xartia2 = []
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    xarti1 = [10] + figures
    xarti2 = [i for i in range(1, 10)]
    color = ["H", "S", "C", "D"]
    for i in xarti:
        for j in color:
            xartia.append([i, j])
    random.shuffle(xartia)
    for i in xarti1:
        for j in color:
            xartia1.append([i, j])
    random.shuffle(xartia1)
    for i in xarti2:
        for j in color:
            xartia2.append([i, j])
    random.shuffle(xartia2)
    player1 = []
    sum1 = 0
    i = 0
    while sum1 < 16:
        sum1 = 0
        if i == 0:
            k = 0
            player1.append(xartia1.pop())
            print("first card is", player1)
            for j in range(len(xartia)):
                if player1[0] == xartia[j]:
                    xartia.pop(j)
                    break
            i += 1
        player1.append(xartia.pop())
        for card in player1:
            if card[0] in figures:
                sum1 = sum1+10
            else:
                sum1 = sum1+card[0]
        print(sum1)
    if sum1 > 21:
        print("P2 wins!")
        W_2 += 1
    else:
        print("P2 joins the game")
        player2 = []
        sum2 = 0
        i = 0
        while sum2 < 16:
            sum2 = 0
            if i == 0:
                k = 0
                print(k)
                player2.append(xartia2.pop())
                print("first card is", player2)
                for j in range(len(xartia)):
                    if player2[0] == xartia[j]:
                        xartia.pop(j)
                        break
            i += 1
            player2.append(xartia.pop())
            print(player2)
            for card in player2:
                if card[0] in figures:
                    sum2 = sum2+10
                else:
                    sum2 = sum2+card[0]
            print(sum2)
        if sum2 > 21:
            sum2 = 0
        if sum1 > sum2:
            print("P1 wins!")
            W_1 += 1
        elif sum2 > sum1:
            print("P2 wins!")
            W_2 += 1
        else:
            print("draw!")
            D += 1
print("Game over!")
print("Player 1 won", W_1, "times")
print("Player 2 won", W_2, "times")
print("There were", D, "draws")
