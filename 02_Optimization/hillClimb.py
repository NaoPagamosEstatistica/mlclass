import os
import subprocess
from math import randint
os.system("g++ hillClimb.cpp -o test")

phi, theta = [], []
subprocess.check_output(["./test", phi, theta])