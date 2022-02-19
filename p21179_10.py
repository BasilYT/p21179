def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(7) for x in s]  # Μετατρέπει ASCII σε 7 bit


def last_2_digits(n):
    return float(str(n)[-3:]) if '.' in str(n)[-2:] else int(str(n)[-2:])
# Παίρνει τα 2 τελευταία ψηφία των 7 bit


def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])  # Μετατρέπει bits σε string


def convert_back(bin_num):
    # Μετατρέπει 16 bit σε δεκαδικό αριθμό
    value = 0
    n = list(bin_num)

    if n[0] == '1':
        value = value + (2 ** 15)
    if n[1] == '1':
        value = value + (2 ** 14)
    if n[2] == '1':
        value = value + (2 ** 13)
    if n[3] == '1':
        value = value + (2 ** 12)
    if n[4] == '1':
        value = value + (2 ** 11)
    if n[5] == '1':
        value = value + (2 ** 10)
    if n[6] == '1':
        value = value + (2 ** 9)
    if n[7] == '1':
        value = value + (2 ** 8)
    if n[8] == '1':
        value = value + (2 ** 7)
    if n[9] == '1':
        value = value + (2 ** 6)
    if n[10] == '1':
        value = value + (2 ** 5)
    if n[11] == '1':
        value = value + (2 ** 4)
    if n[12] == '1':
        value = value + (2 ** 3)
    if n[13] == '1':
        value = value + (2 ** 2)
    if n[14] == '1':
        value = value + (2 ** 1)
    if n[15] == '1':
        value = value + (2 ** 0)

    return value


s = open("two_cities_ascii.txt", "r")
b = string2bits(s)
s2 = bits2string(b)
f2 = []
l2 = []
bnr_4 = []  # Πίνακας με ζευγάρια 2 πρώτων και 2 τελευταίων bit
bnr_8 = []  # Πίνακας με 8bit
bnr_16 = []  # Πίνακας με 16bit
sum_zug = 0  # πλήθος ζυγών
sum_3 = 0  # πλήθος που διαιρούνται με 3
sum_5 = 0  # πλήθος που διαιρούνται με 5
sum_7 = 0  # πλήθος που διαιρούνται με 7
for x in b:
    help = int(str(x)[:2])
    f_2 = str(help)
    if len(f_2) == 1:
        f2.append("0" + f_2)
    else:
        f2.append(f_2)
    l_2 = str(last_2_digits(x))
    if len(l_2) == 1:
        # Αν το τελευταία ψηφία είναι 01 τότε, αφού κανονικά θα επέστρεφε μόνο 1, προσθέτω ένα 0 μπροστά από το 1
        l2.append("0" + l_2)
    else:
        l2.append(l_2)
bnr_4 = list(map(str.__add__, f2, l2))
# print(bnr_4)
for i in range(0, len(bnr_4) - 1, 2):
    bnr_8.append(bnr_4[i] + bnr_4[i+1])
# print(bnr_8)
for i in range(0, len(bnr_8)-1, 2):
    bnr_16.append(bnr_8[i] + bnr_8[i+1])
if len(bnr_8) % 2 == 1:
    # Αν ξεμείνει κάποιος αριθμός τον μετατρέπω σε 16 bits binary βάζοντας 8 μηδενικά μπροστά
    bnr_16.append("00000000" + bnr_8[len(bnr_8) - 1])
# print(bnr_16)
for i in bnr_16:
    x = convert_back(i)
    # print(x) έβαλα αυτά τα 4 print ως σχόλια για να δείτε την μετατροπή, αλλά θα πάρει πολύ ώρα να τελειώσει λόγο του μεγέθους του αρχείου
    if x % 2 == 0:
        sum_zug += 1
    if x % 3 == 0:
        sum_3 += 1
    if x % 5 == 0:
        sum_5 += 1
    if x % 7 == 0:
        sum_7 += 1

per_zug = (sum_zug/len(bnr_16)) * 100
per_3 = (sum_3/len(bnr_16)) * 100
per_5 = (sum_5/len(bnr_16)) * 100
per_7 = (sum_7/len(bnr_16)) * 100
print(per_zug, per_3, per_5, per_7)
