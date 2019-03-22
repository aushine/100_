score = int(input(r"plz input score:"))
rank = {'A': 90, 'B': 60, 'C': 0}
for k, v in rank.items():
    if score >= v:
        print("u rank is: ", k)
        break