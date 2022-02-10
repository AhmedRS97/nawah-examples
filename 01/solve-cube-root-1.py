## In session first solution

num=8
cube=0
while cube ** 3 < num:
    # if cube ** 3 == 9:
    #     print (cube)
    cube +=1
if (cube ** 3 == num):
    print (cube)
else:
    print ("This Num: "+ str(cube) +" ha no cube")

