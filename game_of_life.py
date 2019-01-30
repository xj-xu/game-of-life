import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

N = int(input("Please enter a positive integer N to create an N by N grid"))
p_born = float(input("Please enter the probability, between 0 and 1, of a cell initialized as alive")

def iterate(X):
    X1 = np.zeros((N, N))
    X1[:,:]=X[:,:]    

    for i in range(N):
        for j in range(N):
            nb=0
            for k in range(8):
                ik=i+nx[k]
                jk=j+ny[k]
                nb = nb+ X[ik%N,jk%N]
            if X[i,j]==red:
                if (nb < 2) or (nb>3): 
                    X1[i,j]=blue
            else:
                if nb==3: X1[i,j]=red
    return X1
        
# neighbor pixel directions
nx = [-1, -1, 0, 1, 1, 1, 0, -1]
ny = [0, 1, 1, 1, 0, -1, -1, -1]
blue=0
red=1
X = np.zeros((N, N),dtype=int)
for i in range(N):
    for j in range(N):
        if np.random.random()>p_born : X[i,j]=red

pause = False

def onClick(event):
    global pause
    pause ^= True

fig = plt.figure(figsize=(25/3, 6.25))
ax = fig.add_subplot(111)
ax.set_axis_off()
im = ax.imshow(X, cmap=plt.cm.jet)

# The animation function: called to produce a frame for each generation.
def animate(i):
    im.set_data(animate.X)
    animate.X = iterate(animate.X)
# Bind our grid to the identifier X in the animate function's namespace.
animate.X = X

# Interval between frames (ms).
interval = 100
fig.canvas.mpl_connect('button_press_event', onClick)
anim = animation.FuncAnimation(fig, animate, interval=interval)
plt.show()
