from scipy import misc
import numpy as np
import random
from numpy.testing import assert_array_almost_equal

def break_into(value, steps=10):
    mean = value / float(steps)
    output = np.zeros(steps)
    rang = range(steps)
    random.shuffle(rang)
    for n in rang:
        rand = random.uniform(0, 2 * mean)
        if value - rand >= 0:
            output[n] = rand
        value -= output[n]
    if value > 0:
        output[n] += value
    return output


ok = misc.imread('ok.jpg')
final_array = np.zeros((10,25,25))
for i,row in enumerate(ok):
    for j,elem in enumerate(row):
        final_array[:,i,j] = break_into(elem, 10)

# compare image with numpy
# final_array.sum(axis = 0) == ok
assert_array_almost_equal(final_array.sum(axis = 0), ok, decimal = 6)
# write into file (25, 25) x 10
secret = open('secret_image.dat', 'w')
for slice in final_array:
    secret.write('#\n')
    for row in slice:
        secret.writelines(','.join('{:.6}'.format(str(val)) for val in row)+'\n')

secret.close()
