import os
import subprocess
from random import randint
os.system("g++ hillClimb.cpp -o test -std=c++11")
inf = 1<<20
radious = [90, 45, 30, 360, 10]

best = []
for i in range(len(radious)):
    f = open("%d" % (radious[i]), "w")
    b = open("best%d" % (radious[i]), "w")
    best += [[-inf]]
    f.close()
    b.close()

def treatRes(res):
    res = str(res)
    s = res[2:len(res) - 3]
    return(str(s))

def runHill(args, radio):
    result = subprocess.check_output(["./test", *args, "0", "1000000", str(radio), "20"])
    result = treatRes(result)
    lol = result.split(' ')
    #print(lol)
    print(result)
    return(result, lol)

while (True):
    f = []
    b = []
    for i in range(len(radious)):
        f += [open("%d" % (radious[i]), "a")]
        b += [open("best%d" % (radious[i]), "r")]
        lines = b[i].readlines()
        if (len(lines)):
            best[i] = lines[0].split()
        else:
            best[i] = [-inf]

    args = []
    for i in range(6):
        args += [randint(0, 359)]
    args = list(map(str, args))
    for i in range(len(radious)):
        result, ans = runHill(args, radious[i])
        print(result, file=f[i])
        if (float(ans[0]) > float(best[i][0])):
            b[i].close()
            b[i] = open("best%d" % (radious[i]), "w")
            print(result, file=b[i])

    for i in range(len(radious)):
        f[i].close()
        b[i].close()