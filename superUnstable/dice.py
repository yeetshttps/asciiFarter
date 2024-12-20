import random
import sys
from yeettools import numsplit

try:
    args = sys.argv[1]
    dice = numsplit(int(args))
    print(random.choice(dice))
except IndexError:
    dice = numsplit(6)
    print(random.choice(dice))
