def even_fibonacci(value):
    n_2 = 0
    n_1 = 1
    ans = 0
    new = 1

    while new < value:
        new = n_1 + n_2
        n_2 = n_1
        n_1 = new

        if new % 2 == 0 and new < value:
            ans = ans + new

    return ans


x = even_fibonacci(4000000)
print(x)

