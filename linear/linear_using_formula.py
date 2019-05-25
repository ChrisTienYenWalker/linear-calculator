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
