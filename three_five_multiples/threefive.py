def threefive(value):
    count = 0
    ans = 0
    while count < value:
        if count % 3 == 0 or count % 5 == 0:
            ans = ans + count

        count = count + 1

    return ans


x = threefive(1000)
print(x)


