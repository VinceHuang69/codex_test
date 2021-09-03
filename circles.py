# draw two circles, the smaller one is inside the bigger one
# using python matplotlib library

import matplotlib.pyplot as plt
import numpy as np

# create a figure window
fig = plt.figure(figsize=(6,6))

# get the current axes, creating one if necessary.
ax = fig.gca()

# set x and y limits of the current axes
ax.set_xlim([0,10])
ax.set_ylim([0,10])

# draw a circle
circle1 = plt.Circle((5,5), 2, color='r', fill=False)
ax.add_artist(circle1)

# draw a smaller circle
circle2 = plt.Circle((5,5), 1, color='b', fill=False)
ax.add_artist(circle2)

# save the figure
fig.savefig('circle.png')