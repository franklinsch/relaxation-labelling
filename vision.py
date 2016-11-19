import numpy as np

m = np.matrix([[0.0, 0.0, 0.0, 0.0, 0.0],
               [0.0, 0.1, 0.1, 0.1, 0.0],
               [0.0, 0.1, 1.0, 0.1, 0.0],
               [0.0, 0.1, 0.1, 0.1, 0.0],
               [0.0, 0.0, 0.0, 0.0, 0.0]]).T;

def r(i,l,j,k):
    if (l == k and l == 0):
        return 2
    return 1

def adjacent(a,b):
    if (a == b):
        return False
    return np.linalg.norm(np.subtract(a,b)) < 2

def coeff(a, b):
    if adjacent(a,b):
        return 1
    return 0

def prob(i, l):
    v = m[i]
    if l == 0:
        return v
    else:
        return 1 - v

def getq(j, i, l):
    acc = 0
    for k in range(2):
        rv = r(i,l,j,k)
        p = prob(j,k)
        acc += rv * p
    return acc

def getQ(i, l):
    acc = 0
    for j, value in np.ndenumerate(m):
        co = coeff(i,j)
        q = getq(j, i, l)
        acc += co * q
    return acc

def getNewP(i, l):
    p = prob(i,l)
    q = getQ(i,l)

    num = p * q
    den = 0

    for k in range(2):
        p1 = prob(i,k)
        q1 = getQ(i,k)
        den += p1 * q1

    return num / den

for _ in range(2):
    newMat = np.zeros(shape=m.shape)
    for i, value in np.ndenumerate(m):
        for l in range(1):
            newP = getNewP(i, l)
            newMat[i] = newP
    m = newMat
    print(newMat)
