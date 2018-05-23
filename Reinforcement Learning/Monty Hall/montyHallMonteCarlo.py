from random import randint, shuffle

def genDoor(doorsQuantity):
    door = [0] * doorsQuantity
    door[randint(0, doorsQuantity - 1)] = 1
    return(door)

def argMax(Q):
    best = [-1, -1]
    for i in range(len(Q)):
        if (Q[i] > best[1]):
            best = [i, Q[i]]
    return(best[0])

pi = randint(0, 1) # policy start randomly
doorsQuantity = 100
montyChooses = 98
e = 0.8 # learning rate
Q = [0, 0] # there's only one state, which has two actions: change or not
episodes = 10000

ee = episodes
while (ee):
    if (pi):
        print("Policy: change")
    else:
        print("Policy: keep")

    door = genDoor(doorsQuantity) # generating episode
    print("Doors:", door)

    available = list(range(doorsQuantity))
    chosen = randint(0, doorsQuantity - 1)
    available.remove(chosen) # choosing a door
    print(chosen, available)

    aux = montyChooses
    while (aux):
        monty = randint(0, doorsQuantity - 1)
        while (door[monty] or monty == chosen or monty not in available): # can't choose winner door or chosen door
            monty = randint(0, doorsQuantity - 1)
        available.remove(monty) # monty chooses a goat
        aux -= 1
    print(available)

    final = chosen
    if (pi): # if policy says to change
        shuffle(available)
        final = available[0]

    won = 0
    if (door[final]):
        print("Winner")
        won = 1
    else:
        print("Loser")

    Q[0], Q[1] = Q[0] + door[chosen] / episodes, Q[1] + door[available[0]] / episodes # saving ""mean"" of returns

    pi = argMax(Q) # getting new policy through argMax; since there's only one state, it will just choose between action of that single state

    ee -= 1
    print("Q: [keep: %lf, change: %lf]" % (Q[0], Q[1]), end='\n\n')

print("Q: [keep: %lf, change: %lf]" % (Q[0], Q[1]))
print("Expected probability:", (doorsQuantity - 1) / (doorsQuantity * (doorsQuantity - montyChooses - 1)))