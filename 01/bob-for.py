s = 'fobobobdrbondbob'
num_of_bobs = 0
for i in range(len(s)):
    if s[i:i+3] == 'bob':
        num_of_bobs += 1

print('bob appers {0} times'.format(num_of_bobs))

