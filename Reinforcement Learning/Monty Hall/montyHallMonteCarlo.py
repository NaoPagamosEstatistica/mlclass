from random import randint, shuffle
doorsQuantity = 3
montyChooses = 1
episodes = 10000
CHANGE = 1
KEEP = 0
WINNER_DOOR = 1

def genDoor(doorsQuantity):
    door = [0] * doorsQuantity
    door[randint(0, doorsQuantity - 1)] = WINNER_DOOR
    return(door)

def argMax(Q):
    best = [-1, -1]
    for i in range(len(Q)):
        if (Q[i] > best[1]):
            best = [i, Q[i]]
    return(best[0])

def learnBestPolicy():
    global doorsQuantity, montyChooses, episodes
    pi = randint(KEEP, CHANGE) # policy start randomly
    Q = [0, 0] # there's only one state, which has two actions: change or not

    ee = episodes
    while (ee):
        if (pi == CHANGE):
            print("Policy: change")
        else:
            print("Policy: keep")

        door = genDoor(doorsQuantity) # generating episode
        print("Doors:", door)

        available = list(range(doorsQuantity))
        chosen = randint(0, doorsQuantity - 1)
        available.remove(chosen) # choosing a door

        aux = montyChooses
        while (aux):
            while (door[available[0]]): # monty can't choose the winner door
                shuffle(available)
            available.remove(available[0]) # monty chooses a goat
            aux -= 1

        final = chosen
        if (pi == CHANGE): # if policy says to change
            shuffle(available)
            final = available[0]

        if (door[final]):
            print("Winner")
        else:
            print("Loser")

        Q[KEEP], Q[CHANGE] = Q[KEEP] + door[chosen] / episodes, Q[CHANGE] + door[available[0]] / episodes # saving ""mean"" of returns

        pi = argMax(Q) # getting new policy through argMax; since there's only one state, it will just choose between action of that single state

        print("Q: [keep: %lf, change: %lf]" % (Q[KEEP], Q[CHANGE]), end='\n\n')
        ee -= 1

    if (pi):
        print("Best policy: Change")
    else:
        print("Best policy: Keep")
    return(pi)

def evaluatePolicy(pi):
    global doorsQuantity, montyChooses, episodes
    won = 0

    ee = episodes
    while (ee):
        door = genDoor(doorsQuantity) # generating episode

        available = list(range(doorsQuantity))
        chosen = randint(0, doorsQuantity - 1)
        available.remove(chosen) # choosing a door

        aux = montyChooses
        while (aux):
            while (door[available[0]]): # monty can't choose the winner door
                shuffle(available)
            available.remove(available[0]) # monty chooses a goat
            aux -= 1

        final = chosen
        if (pi): # if policy says to change
            shuffle(available)
            final = available[0]

        if (door[final]):
            won += 1

        ee -= 1
    return(won / episodes)

learnBestPolicy()
print("Change Theoretical Expectation:", (doorsQuantity - 1) / (doorsQuantity * (doorsQuantity - montyChooses - 1)))
print("Keep-policy Expectation       :", evaluatePolicy(KEEP))
print("Change-policy Expectation     :", evaluatePolicy(CHANGE))