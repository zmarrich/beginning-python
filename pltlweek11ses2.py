#try except
try:
    num=int(input("Enter integer"))
except:
    print('THAT WAS NOT A INTEGER.')
else:
    print("Integer entered")
    print("squared the int is",num*num)
    break
###VALIDATION
def open_file(filename):
    lines=[]
    while True:
        try:
            in_file=open(filename,"r")
        except:
            filename=input("that is not found enter a file name")
        else:
            break
    lines=in_file.readlines()

    for i in range(len(lines)):
        lines[i]=lines[i].strip()
    in_file.close()
    return lines

data=open_file("doesnotexist.txt")
print("The contents of the file")
print(data)




#####factorial 
def factorial(num):
    if (num==1):
        return 1
    else:
        return num*factorial(num-1)
print(factorial(5))

###SELCTION SORT

from tools import *
def selectionSort(items):
    ordered=items.copy()

    for i in range(len(ordered)):
        nextSmall=-1

        for j in range(i, len(ordered)):
            if ordered[j]<ordered[nextSmall]:
                nextSmall=j
        swap(ordered, nextSmall, i)
    return ordered
print(selectionSort([3,1,12,21,0,2,5]))

