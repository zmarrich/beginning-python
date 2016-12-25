###Loop slide 
##
##letters=["a","e","i","o","u"]
##
##for vowel in letters:
##    #print(vowel)
##    print(vowel, end = " ")



###range slide
##
##print("range way one")
##print("the integers from 0 to 9 are:")
##for i in range (10):
##    print (i, end= " ")
####
##print("\nrange way two")
##print("the integers from 3 to 8 are:")
##for i in range(3,9,):
##    print(i, end= " ")
####
##print("\nrange way three")
##print("the even integers from 0 to 11 are:")
##for i in range(0,11,2):
##    print(i,end= " ")

###all together
numbers = [1,2,3,4]
print(numbers, end= " ")

for i in range(len(numbers)):
    numbers[i]*=2
print("\n")
print(numbers,end= " ")
