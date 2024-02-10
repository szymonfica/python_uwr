# Szymon Fica
# list 1 task 4

import math
import random

cltwt = 500000
ltwo = 0

for i in range(cltwt):
    x, y = random.random(), random.random()
    if (x-0.5)*(x-0.5) + (y-0.5)*(y-0.5) <= 0.25:
        ltwo += 1

print(str(4*ltwo/cltwt) + " - approximate value of pi after " + str(cltwt) + " darts thrown")
print(str(math.pi) + " - pi")
