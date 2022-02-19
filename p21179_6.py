import random

p_white = 0
p_black = 0
games = 0
for times in range(100):
    board = ["" for i in range(1, 65)]  # Ο πίνακας συμβολίζει μια σκακιέρα 8x8
    board[0] = "Queen"
    board[1] = "Tower"
    board[2] = "Bishop"
    random.shuffle(board)
    # print(board)
    x1 = board.index("Queen")
    x2 = board.index("Tower")
    x3 = board.index("Bishop")
    #print(x1, x2, x3)
    ver = int(x1/8) + 1  # vertical θεση της βασιλισσας
    # print(ver)
    hor = (x1 % 8) + 1  # horizontal θεση της βασιλισσας
    # print(hor)
    if hor == 1 or ver == 1:
        # Το μικρότερο στοιχείο της διαγωνίου από την άνω αριστερή μεριά(πάνω και αριστερά από το x1)
        min1 = x1
    else:
        min1 = x1 - 9*(hor-1)
    while min1 < 0:
        min1 = min1 + 9  # Μια περίπτωση μου έβγαλε αρνητικό το min, δεν μου ξανά έτυχε από όταν το έβαλα αύτο οπότε το κρατάω. Ίσως είναι περιττό μετά τον πάνω έλεγχο
    # print(min1)
    if ver == 8 or hor == 8:
        # Το μεγαλύτερο στοιχείο της διαγωνίου από την άνω αριστερή μεριά(κάτω και δεξιά από το x1)
        max1 = x1
    else:
        max1 = x1 + 9*(8-hor)
    while max1 > 63:
        max1 = max1 - 9
    # print(max1)
    for i in range(min1, max1+1, 9):
        if x3 == i:
            p_white += 1
            p_black += 1
        elif x2 == i:
            p_black += 1
    if ver == 1 or hor == 8:
        # Το μικρότερο στοιχείο της διαγωνίου από την άνω δεξιά μεριά(πάνω και δεξιά από το x1)
        min2 = x1
    else:
        min2 = x1 - 7*(8-hor)
    while min2 < 0:
        min2 = min2 + 7
    # print(min2)
    if hor == 1 or ver == 8:
        # Το μεγαλύτερο στοιχείο της διαγωνίου από την άνω δεξιά μεριά(κάτω και αριστερά από το x1)
        max2 = x1
    else:
        max2 = x1 + 7*(hor - 1)
    while max2 > 63:
        max2 = max2 - 7
    # print(max2)
    for i in range(min2, max2+1, 7):
        if x3 == i:
            p_white += 1
            p_black += 1
        elif x2 == i:
            p_black += 1
    # Το μεγαλύτερο στοιχείο της κάθετης ευθείας πάνω στην οποία βρίσκετε η βασίλισσα
    max_ver = 8*8 - (8-hor) - 1
    # print(max_ver)
    while max_ver > 0:
        if x2 == max_ver:
            p_white += 1
            p_black += 1
        elif x3 == max_ver:
            p_black += 1
        max_ver = max_ver - 8
    # Το μεγαλύτερο στοιχείο της οριζόντιας ευθείας πάνω στην οποία βρίσκετε η βασίλισσα
    max_hor = 8*ver - 1
    # print(max_hor)
    for i in range(max_hor, max_hor - 8, -1):
        if x2 == i:
            p_white += 1
            p_black += 1
        elif x3 == i:
            p_black += 1
    # print(p_black)
    # print(p_white)
    games += 1
# Το είχα βάλει για να ελέγχω ότι είναι όντως 100 επαναλήψεις, αλλά το κρατάω για ομορφιά.
print("Συνολικά παιχνίδια: ", games)
print("Η άσπρη ομάδα έχει: ", p_white, "πόντους.")
print("Η μαύρη ομάδα έχει: ", p_black, "πόντους.")
if p_black == p_white:
    print("It's a draw!")
elif p_black > p_white:
    print("Black team wins!")
else:
    print("White team wins!")
# Γνωρίζω ότι υπάρχει μια περίπτωση που ο αξιωματικός
# (αντίστοιχα πύργος) βρίσκεται ανάμεσα στην βασίλισσα
# και στον πύργο (αντίστοιχα αξιωματικό) (τόσο στην
# περίπτωση των διαγωνίων όσο και στην περίπτωση των
# γραμμών/στηλών) αλλά δεν γνωρίζω πως να αποκλείσω
# αυτή την περίπτωση από το να μετρήσει επιπλέον πόντους.
# Γνωρίζω επίσης πως θα νικάει πάντα η μαύρη ομάδα(εφόσον
# όταν απειλείται η βασίλισσα από ένα πιόνι, ταυτόχρονα
# απειλεί και το αντίστοιχο πιόνι.), απλά έβαλα και την
# περίπτωση που νικάει και η άσπρη ομάδα για να φαίνεται πιο ολοκληρωμένο
