mozi = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
mozi = mozi.replace(",","")
mozi = mozi.rstrip(".")
pi1 = mozi.split()

pi2 = list()

for s in pi1:
    pi2.append(len(s))

    

print(pi2)