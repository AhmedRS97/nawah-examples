# Find the cube root of a perfect cube
x = int(input('Enter an integer: '))
ans = 0

while ans ** 3 < x:
    ans = ans + 1

if ans ** 3 != x:
    print(x, 'is not a perfect cube')
else:
    print('Cube root of ' + str(x) + ' is ' + str(ans))
