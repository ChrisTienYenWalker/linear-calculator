def x_int(self, m, b):
    s = 0 - b
    x = s / m
    return x

def predictionY(self, m, b, x):
    s = m*x
    y = s + b
    return y

def predictionX(self, m, b, y):
    s = y - b
    x = s / m
    return x


#intersections

def intersectingX(self, m1, m2, b1, b2):
    m = m1 - m2
    b = b1 - b2
    x = b / m
    return x
def intersectingY(self, m1, m2, b1, b2, B1):
    x = intersectingX(0, m1, m2 , b1, b2)
    s = m1 * x
    y = s + B1
    return y