def squaresum(value):
    squareSum = 0
    count = 0
    
    while count < value:
        square = count * count
        if(square % 2 == 1):
            squareSum = squareSum + square
        count = count + 1
    return squareSum


print("The answer of odd squares up to 928,000 is: ", squaresum(928000))
