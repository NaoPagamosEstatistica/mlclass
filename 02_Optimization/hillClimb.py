import os
import subprocess
from random import randint
os.system("g++ hillClimb.cpp -o test")

args = [90, 90, 90, 90, 90, 90]
args = list(map(str, args))
result = subprocess.check_output(["./test", *args])
print(result)