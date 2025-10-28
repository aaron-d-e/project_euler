# double loop 999 and 999 finding the product and check if it is palindrome, keep track of current max, return absolute max

def isPalindrome(n):
    reverse = 0

    # Copy of the original number so that the original
    # number remains unchanged while finding the reverse
    temp = abs(n)
    while temp != 0:
        reverse = (reverse * 10) + (temp % 10)
        temp = temp // 10

    # If reverse is equal to the original number, the
    # number is palindrome
    return (reverse == abs(n))

def largest_palindrome():
    maxNum = -1 

    for x in range (900, 999, 1): #using 'magic' numbers isnt great but works
        for y in range (900, 999, 1):
            product = x * y

            if(isPalindrome(product)):
                if product > maxNum:
                    maxNum = product
    return maxNum


x = largest_palindrome() 

print(x)
