def rate(self, y1, y2, x1, x2):
    y = y2 - y1
    x = x2 - x1
    if x == 0:
        return 0
    else:
        m = y/x
        return m 

def y_int(self, Y1, Y2, X1, X2):
    s1 = X1 * rate(0, Y1, Y2, X1, X2)
    b = Y1 - s1
    return b
def x_int(self, y1, y2, x1, x2):
    m = rate(0, y1, y2, x1, x2)
    b = y_int(0, y1, y2, x1, x2)
    s = 0 - b
    x = s / m
    return x 
def formula(self, Y1, Y2, X1, X2):
    s1 = X1*rate(0, Y1, Y2, X1, X2)
    b = Y1 - s1
    if b is 0:
        return print("Y=" + rate(0, Y1, Y2, X1, X2) + "X")
    else:
        return print("Y=" + rate(0, Y1, Y2 , X1, X2) + "X" + b)
def predictionX(self, Y1, Y2, X1, X2, Y3):
    s = Y3 / rate(0, Y1, Y2, X1, X2)
    X = s - formula(0, Y1, Y2, X1, X2)
    return X
def predictionY(self, Y1, Y2, X1, X2, X3):
    y = rate(0, Y1, Y2, X1, X2) * X3 + formula(0, Y1, Y2, X1, X2)
    return y

class description:
    def origin(self, Y1, Y2, X1, X2):
        s1 = X1*rate(0, Y1, Y2, X1, X2)
        b = Y1- s1
        if b is 0: 
            print('it pass through the origin')
        else:
            print('it does not pass through the origin')
    def formula(self, Y1, Y2, X1, X2):
        s1 = X1 * rate(0, Y1, Y2, X1, X2)
        b = Y1 - s1
        if b is 0:
            return ("Y=" + rate(0, Y1, Y2, X1, X2) + "X")
        else:
            return ("Y=" + rate(0, Y1, Y2 , X1, X2) + "X" + b)
    def steep(self, Y1, Y2, X1, X2):
        if 1 >= rate(0, Y1, Y2, X1, X2) >= -1:
            return print("not very steep")
        else:
            return print("steep")
    def inc(self, Y1, Y2, X1, X2):
        if rate(0, Y1, Y2, X1, X2) < 0:
            return print("The line is decreasing at a rate of " + rate(0, Y1, Y2, X1, X2))
        if rate(0, Y1, Y2, X1, X2) > 0:
            return print("The line is increasing at a rate of " + rate(0, Y1, Y2, X1, X2))
        elif rate(0, Y1, Y2, X1, X2) is 0:
            return print("The line horizantal and increases at a rate of 0")
        else:
            return print("The line is vertical and does not increase")