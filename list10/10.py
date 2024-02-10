# Szymon Fica 337307
# Lista 10 Zadanie 3

import matplotlib.pyplot as plt
import matplotlib.animation as animation

ants, h, w = 2, 20, 40
ant_x = [int(w/3), int(2*w/3)]
ant_y = [int(h/2), int(h/2)]
board = [[0]*h for _ in range(w)]
colors = {0: 'white', 1: 'blue', 2: 'red'}
turns = [0, 0]
#    0
#  3   1
#    2

fig, ax = plt.subplots(1, 1)
ax.set_xlim(0, w)
ax.set_ylim(0, h)
ax.set_aspect('equal', adjustable='box')

def paint(x, y, z):
    board[x][y] = z
    ax.add_patch(plt.Rectangle((x, y), 1, 1, fc=colors[z]))

X = [0, 1, 0, -1]
Y = [1, 0, -1, 0]
def f(q):
    for i in range(0, ants):
        if board[ant_x[i]][ant_y[i]] == 0:
            paint(ant_x[i], ant_y[i], i+1)
            turns[i] = (turns[i]+1)%4
        else:
            paint(ant_x[i], ant_y[i], 0)
            turns[i] = (turns[i]-1+4)%4
        ant_x[i] = (ant_x[i] + X[turns[i]])%w
        ant_y[i] = (ant_y[i] + Y[turns[i]])%h
    
paint(ant_x[0], ant_y[0], 1)
paint(ant_x[1], ant_y[1], 2)

a = animation.FuncAnimation(fig, f, interval=10, repeat=True)

plt.show()

