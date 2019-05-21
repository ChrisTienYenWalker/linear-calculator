def rate(self, Y1, Y2, X1, X2):
    y = Y1 - Y2
    x = X1 - X2
    return y / x

class points:
    def slope(self, Y1, Y2, X1, X2):    
        return rate(0, Y1, Y2, X1, X2)
    def y_int(self, Y1, Y2, X1, X2):
        s1 = X1*rate(0, Y1, Y2, X1, X2)
        b = Y1 - s1
        return b
    def x_int(self, yaxis1, yaxis2, xaxis1, xaxis2):
        yaxis = yaxis1 - yaxis2
        xaxis = xaxis1 - xaxis2
        m = yaxis / xaxis
        if yaxis1 > 0 and m > 0:
            while yaxis1 > 0: 
                yaxis1 -= 1
                xaxis1 -= xaxis
                return xaxis1 + xaxis
        if yaxis1 > 0  and m < 0:
            while yaxis1 > 0: 
                yaxis1 -= 1
                xaxis1 += xaxis
                return xaxis1 +xaxis
        if yaxis1 < 0 and m > 0:
            while yaxis1 < 0:
                yaxis1 += 1
                xaxis1 += xaxis
                return xaxis1 + xaxis
        if yaxis1 < 0 and m < 0:
            while yaxis1 < 0:
                yaxis1 += 1
                xaxis1 -= xaxis
                return xaxis1 + xaxis
    def formula(self, Y1, Y2, X1, X2):
        s1 = X1*rate(0, Y1, Y2, X1, X2)
        b = Y1 - s1
        if b is 0:
            return 'Y=' + rate(0, Y1, Y2, X1, X2) + 'X'
        else:
            return 'Y=' + rate(0, Y1, Y2 , X1, X2) + 'X' + b
    class description:
        def origin(self, Y1, Y2, X1, X2):
            s1 = X1*rate(0, Y1, Y2, X1, X2)
            b = Y1- s1
            if b is 0: 
                print('it pass through the origin')
            else:
                print('it does not pass through the origin')
        def formula(self, Y1, Y2, X1, X2):
            s1 = X1*rate(0, Y1, Y2, X1, X2)
            b = Y1 - s1
            if b is 0:
                return 'Y=' + rate(0, Y1, Y2, X1, X2) + 'X'
            else:
                return 'Y=' + rate(0, Y1, Y2 , X1, X2) + 'X' + b
        def steep(self, Y1, Y2, X1, X2):
            if 1 >= rate(Y1, Y2, X1, X2) >= -1:
                return 'not very steep'
            else:
                return 'steep'
        def inc(self, Y1, Y2, X1, X2):
            if rate(Y1, Y2, X1, X2) < 0:
                return "The line is decreasing at a rate of " + rate(Y1, Y2, X1, X2)
            if rate(Y1, Y2, X1, X2) > 0:
                return 'The line is increasing at a rate of ' + rate(Y1, Y2, X1, X2)
            elif rate(Y1, Y2, X1, X2) is 0:
                return 'The line horizantal and increases at a rate of 0'
            else:
                return 'The line is vertical and does not increase'
    def prediction(self, Y1, Y2, X1, X2):
        
def question(self):
    lineQuest = input('What type of line are you looking for [linear] ')
    if lineQuest == 'linear' or lineQuest =='Linear' or lineQuest == 'linear relations' or lineQuest == 'linear relation':
        linearQues = input('Would you like to find [slope, x-int, y-int, formula, descprition, prediction] ')
        linedec = input("Do you know the [points or the formula]: ")
        if linedec is 'points' or linedec is 'Points' or linedec is 'point' or linedec is 'Point':
                x1 = input(int('Enter X1: '))
                y1 = input(int('Enter Y1: '))
                x2 = input(int('Enter X2: '))
                y2 = input(int('Enter X2: '))
                if linearQues is 'slope' or linearQues is 'Slope' or linearQues is 's':
                        point.slope(y1, y2, x1, x2)
                if linearQues is 'x-int' or linearQues is 'X-int' or linearQues is 'x':
                        point.x_int(y1, y2, x1, x2)
