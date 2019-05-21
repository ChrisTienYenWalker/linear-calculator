import formula as form 
import points as points
x1 = input('Enter X1: ')
y1 = input('Enter Y1: ')
x2 = input('Enter X2: ')
y2 = input('Enter X2: ')
points.rate(0, y1, y2, x1, x2)
print('welcome to the linear calculator')
linearQues = input('Would you like to find [slope, x-int, y-int, formula, descprition, prediction] ')
linedec = input(str("Do you know the [points or the formula]: "))
if linedec == 'points' or linedec == 'Points' or linedec == 'point' or linedec == 'Point':
    x1 = input('Enter X1: ')
    y1 = input('Enter Y1: ')
    x2 = input('Enter X2: ')
    y2 = input('Enter X2: ')
    if linearQues == 'slope' or linearQues == 'Slope' or linearQues == 's':
        points.rate(0, y1, y2, x1, x2)
    if linearQues == 'x-int' or linearQues == 'X-int' or linearQues == 'x':
        points.x_int(0, y1, y2, x1, x2)
    if linearQues == 'y-int' or linearQues == 'y' or linearQues == 'Y-int':
        points.y_int(0, y1, y2,  x1, x2)
    if linearQues == 'formula' or linearQues == 'Formula' or linearQues == 'f':
        points.formula(0, y1, y2, x1, x2)
    if linearQues == 'prediction' or linearQues == 'p' or linearQues == 'Prediction':
        predict = input(str('Would you like to predict [X or Y]: '))
        if predict == 'X' or predict == 'x':
            y3 = input(int('Enter the Y your corrident to find the X: '))
            points.predictionX(0, y1, y2, x1, x2, y3)
        if predict == 'Y' or predict == 'y':
            x3 = input(int('Enter the X your corrident to find the Y: '))
            points.predictionY(0, y1, y2, x1, x2, x3)
        if linearQues == 'descprition' or linearQues == 'Descprition' or linearQues == 'd':
            des = (points.description.origin(0, y1, y2, x1, x2), points.description.steep(0, y1, y2, x1, x2), points.description.inc(0, y1, y2, x1, x2))
            desit = iter(des)
            print(next(desit))
            print(next(desit))
            print(next(desit))
if linedec is 'formula' or linedec is 'Formula' or linedec is 'f':
    print('')


                    
                

