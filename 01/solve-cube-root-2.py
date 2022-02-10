## In session first solution

num=12345678912345678956
cube=0
while cube ** 3 < num:
    if cube ** 3 == num:
        print (cube)
    cube +=1

print ("This Num: "+ str(cube) +" ha no cube")