def squaresum(value):
    squareSum = 0
    count = 0
    
    while count < value:
        square = count * count
        if(square % 2 == 1):
            squareSum = squareSum + square
        count = count + 1
    return squareSum


x = squaresum(928000)
print("The answer of odd sums up to 928,000 is: ")
print(x)
