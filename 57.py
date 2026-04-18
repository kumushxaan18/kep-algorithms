def sum_digits(n):
    n = abs(n)
    yigindi = 0
    while n > 0:
        yigindi += n % 10
        n //= 10
    return yigindi 