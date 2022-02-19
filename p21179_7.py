import collections
import json


def most_popular(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num


dicts = []

with open("File.txt") as inf:
    for index, line in enumerate(inf):
        try:
            dicts.append(json.loads(line))
        except Exception as e:
            print(f"line {index + 1}: {line!r} {e}")

result = collections.defaultdict(list)

for d in dicts:
    for k, v in d.items():
        result[k].append(v)

final = {k: ",".join(str(i) for i in v) for k, v in result.items()}
final = dict(result)
print(final)
print("Ποιο από αυτά τα keys θα θέλατε να ελέγξετε;")
for k in final:
    print(k)
f = True
while f:
    k = input("Εισάγεται το Key που θέλετε να ελέγξετε: ")
    for i in final:
        if k == i:
            f = False
            break


print("Η μεγαλύτερη τιμή του κλειδιού είναι: ", max(i for i in final[k]))
print("Η μικρότερη τιμή του κλειδιού είναι: ", min(i for i in final[k]))
print("Η δημοφιλέστερη τιμή του κλειδιού είναι:", most_popular(final[k]))
