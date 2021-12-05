nbre_dices = 8
from collections import Counter

nber_dices = 8
dices = [1, 2, 3, 4, 5, 5]
res_dices = []
for dice in dices:
    for dice2 in dices:
        for dice3 in dices:
            for dice4 in dices:
                for dice5 in dices:
                    for dice6 in dices:
                        for dice7 in dices:
                            for dice8 in dices:    
                                res_dices.append(sum([dice,dice2,dice3,dice4,dice5,dice6,dice7,dice8]))

occurs = Counter(res_dices).most_common()
occurs_sorted = sorted(occurs, key=lambda x: x[0],reverse=True)
for nber in occurs_sorted:
    print(f'{nber[0]} : {round(nber[1]/(6**nber_dices)*100,2)} %')