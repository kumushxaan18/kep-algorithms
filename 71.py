s = input()
k = sum(map(int, s[:3]))
m = sum(map(int, s[3:]))

if k == m:
    print(True)
else:
    print(False)