import os
import subprocess
import struct
import sys
from random import randint
inf = 1<<20
os.system("g++ hillClimb.cpp -o test")

def neighbors(node, r):
    nb = [node]
    for i in range(10):
        newNode = []
        for j in range(6):
            newNode += [(node[j] + randint(-r, r) + 360) % 360]
        nb += [newNode]
    return(nb)

def evaluate(x):
    x = list(map(str, x))
    result = subprocess.check_output(["./test", *x])
    s = str(result)[2:len(result) - 3]
    f = float(s)
    return(f)

def hillClimb(startNode, r):
    currNode = startNode
    while (True):
        nb = neighbors(currNode, r)
        nextEval, nextNode = -inf, 0
        for x in nb:
            result = evaluate(x)
            if (result > nextEval):
                nextNode = x
                nextEval = result
        print("Best so far:", nextNode, nextEval)
        if (nextEval <= evaluate(currNode)):
            return(currNode)
        currNode = nextNode

arguments = sys.argv
r = int(arguments[1])
startNode = [90, 90, 90, 90, 90, 90]
print(startNode, evaluate(startNode))
bestNode = hillClimb(startNode, r)
print(bestNode, evaluate(bestNode))