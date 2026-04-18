txt = "abcd"
print(txt[0:3])  # bc
print(txt[0: len(txt)]) # abcd
print(txt[0 :: -1]) # dcba
print(txt [0:: -1]) # dcba

def reverse_number(number):
    str_number = str(number)
    return int(str_number[::-1])

for num in range(1000, 10000):
   reversed_num = reverse_number(num)
   if reversed_num == 4 * num:
       print(num)
