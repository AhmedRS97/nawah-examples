last_num = input("Enter a number:")
num = 0
even_nums = 0
while num < last_num:
    if num % 2:
        even_nums += 1
    num += 1

print(even_nums)

