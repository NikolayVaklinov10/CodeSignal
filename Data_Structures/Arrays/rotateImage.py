"""
The challenge: rotate 2 D matrix by 90 degrees (clockwise)

"""


def rotateImage(a):
    a.reverse()
    for i in range(len(a)):
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a


# solution 2

def rotateImage(a):
    return [[x[i] for x in a][::-1] for i in range(len(a))]

# solution 3
rotateImage = lambda a: zip(*a[::-1])


# solution 4
def rotateImage(a):
    return list(zip(*reversed(a)))