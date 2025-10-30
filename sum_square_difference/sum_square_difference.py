def square_difference(value):
    squareOfSum = 0
    sumOfSquare = 0
    for i in range (1,value + 1):
        squareOfSum = squareOfSum + i
        temp = i * i
        sumOfSquare = sumOfSquare + temp
    squareOfSum = squareOfSum ** 2

    return squareOfSum - sumOfSquare



x = square_difference(100) 
print(x)

