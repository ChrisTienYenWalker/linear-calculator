import linear_using_points as points
import linear_using_formula as formula 


print('welcome to the linear calculator')

while  2 > 1:
    linearQues = input('Would you like to find [slope, rate, x-int, y-int, formula, descprition, prediction, intersecting lines] ')
    linearQues.lower()
    linearQues.strip()
    if linearQues == 'exit':
        break
    elif linearQues != 'intersection':
        print('To exit type exit at the end')
        linedec = input(str('Do you know the [points or the formula]: '))
        linedec.lower()
        linedec.strip()
        if linedec == 'exit':
            break
        if linedec == 'points':
            x1 = int(input('Enter X1: '))
            y1 = int(input('Enter Y1: '))
            x2 = int(input('Enter X2: '))
            y2 = int(input('Enter Y2: '))
            if linearQues == 'slope' or linearQues == 'rate':
                print(points.rate(0, y1, y2, x1, x2))
            if linearQues == 'x-int':
                print(points.x_int(0, y1, y2, x1, x2))
            if linearQues == 'y-int':
                print(points.y_int(0, y1, y2,  x1, x2))
            if linearQues =='formula':
                print(points.formula(0, y1, y2, x1, x2))
            if linearQues == 'perdiction':
                predict = input(str('Would you like to predict [X or Y]: '))
                predict.lower()
                predict.strip()
                if predict == 'x':
                    y3 = input(int('Enter the Y your corrident to find the X: '))
                    print(points.predictionX(0, y1, y2, x1, x2, y3))
                if predict =='y':
                    x3 = input(int('Enter the X your corrident to find the Y: '))
                    print(points.predictionY(0, y1, y2, x1, x2, x3))
            if linearQues == 'desprition':
                des = (points.description.origin(0, y1, y2, x1, x2), points.description.steep(0, y1, y2, x1, x2), points.description.inc(0, y1, y2, x1, x2))
                desit = iter(des)
                print(next(desit))
                print(next(desit))
                print(next(desit))
        if linedec == 'formula':
            print('If value unknow type 0')
            input('The formula is y=mx+b or y=mx or y=b')
            m = int(input('Enter m value: '))
            b = int(input('Enter b value: '))
            if linearQues == 'slope' or linearQues == 'rate':
                print('The slope is ' + m)
            if linearQues == 'y-int':
                print('The y-int is ' + b)
            if linearQues == 'x-int':
                print('The x-int is ' + formula.x_int(0, m, b))
            if linearQues == 'prediction':
                predict == str(input('What would you like to find [X/Y]: '))
                predict.lower()
                predict.strip()
                if predict == 'x':
                    y = int(input('What is the value of Y: '))
                    print('X is ' + formula.predictionX(0, m, b, y))
                if predict == 'y':
                    x = int(input('What is the value of X: '))
                    print('Y is ' + formula.predictionY(0, m, b, x))
            if linearQues == 'descprition':
                if 1 >= m >= -1:
                    print("not very steep")
                else:
                    print("Steep")
                if b == 0:
                    print('Goes through the origin')
                else:
                    print('Does not go through the origin')
    if linearQues == 'intersection':
        m1 = int(input('what is the slope for the first line: '))
        m2 = int(input('what is the slope for the second line: '))
        B1 = int(input('what is the y-int for the second line: '))
        B2 = int(input('what is the y-int for the second line: '))
        b1 = 0 - B1
        b2 = 0 - B2
        print('The points are (' + formula.intersectingX(0, m1 , m2, b1, b2) + ',' + formula.intersectingY(0, m1, m2, b1, b2, B1) + ')')
        
                