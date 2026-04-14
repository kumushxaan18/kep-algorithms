result = []

for m in range(1000, 10000):
    digits_sum = sum(int(k) for k in str(m))
    if digits_sum % 2 == 0:
        result.append(m)

print(*result)