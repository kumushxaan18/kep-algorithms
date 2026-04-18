def reverse_number(number):
    string=str(number)
    return string[::-1]
n=input()
count=0
for i in reverse_number(n):
    if i == '0':
        count += 1
    else:
        break
print(count)