import numpy as np
import matplotlib.pyplot as plt

nn = []
with open('../secret_image.dat', 'r') as solving:
    lines = solving.readlines()
for l in lines:
    if l[0] != '#':
        nn.append([float(b) for b in l.splitlines()[0].split(',')])

aal = np.array(nn).reshape((10,25,25))
plt.imshow(aal)
plt.show()
