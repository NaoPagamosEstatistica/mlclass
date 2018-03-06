import os
import subprocess
import struct
import sys
import numpy as np
from random import randint
from math import cos, sin, exp, sqrt
DEBUG = 0
kNeighbors, radious, kStuck = 0, 0, 0
inf = 1<<20
#print(os.system("g++ hillClimb.cpp -o test"))

def norm(x):
    return(x / (36.0) - 5.0)

def gain(param):
    x = norm(param[0])
    y = norm(param[1])
    gain1 = sin(x) + cos(y)

    x = norm(param[2])
    y = norm(param[3])
    gain2 = y * sin(x) - x * cos(y)

    x = norm(param[4])
    y = norm(param[5])
    r = sqrt(x * x + y * y)
    gain3 = sin(x * x + 3.0 * y * y) / (0.1 + r * r) + (x * x + 5.0 * y * y) * exp(1.0 - r * r) / 2.0

    return(4.0 * gain1 + gain2 + 4.0 * gain3)


def neighbors(node):
    nb = []
    for i in range(kNeighbors):
        newNode = []
        for j in range(6):
            newNode += [(node[j] + randint(-radious, radious) + 360) % 360]
        nb += [newNode]
    return(nb)

# def gain(x):
#     return(gain(x))
#     x = list(map(str, x))
#     result = subprocess.check_output(["./test", *x])
#     lol = result
#     s = lol[:len(lol) - 1]
#     f = np.float64(s)
#     #print(result, s, f, "%.20lf" % f)
#     return(f)

def hillClimb(startNode):
    currNode, stuck = startNode, 0
    while (True):
        nb = neighbors(currNode)
        nextEval, nextNode = -inf, 0
        for x in nb:
            result = gain(x)
            if (result > nextEval):
                nextNode = x
                nextEval = result
        if (DEBUG): print("Now:", nextNode, nextEval, "stuck:", stuck, "Best:", gain(currNode))
        if (nextEval <= gain(currNode)):
            stuck += 1
        else:
            stuck = 0
            currNode = nextNode
        if (stuck == kStuck):
            return(currNode)

arguments = sys.argv
DEBUG = int(arguments[1])
radious = int(arguments[2])
kNeighbors = int(arguments[3])
kStuck = int(arguments[4])
#startNode = [242, 180, 2, 334, 179, 156]
#startNode = [180, 180, 180, 180, 180, 180]
#startNode = [90, 90, 90, 90, 90, 90]
startNode = list(map(int, arguments[5:]))
print("Starting Hill Climb with:", startNode, gain(startNode), "radious =", radious, "kNeighbors =", kNeighbors, "kStuck =", kStuck)
bestNode = hillClimb(startNode)
print(bestNode, gain(bestNode))