##numbers=[1,2,3,4,5,63,2,4,5,47,9,0,1,3,1,22,3,42,3,45,54442,3,3443,34]
##unique=set(numbers)
##print("this is the list of all the numbers",numbers)
##print("these are the unique numbers",unique)
#######boolen and length
##print("is there a 4 in unique set of values:", 4 in unique)
##print("number of items in set",len(numbers))
##
##
##set1={2,3,4,5,3,6,7,4}
##set2={2,3,5,6,7,4,8,0}
##print (set1, "\n", set2)
##print('are the sets equal?',set1==set2)
##print("is set 2 contained in set 1?", set1>set2)
##print("is set one contained in set 2?", set1<set2)
##
set3={1,2,3,4}
print(set3)
for i in range(5,11):
    set3.add(i)
print(set3)
set3.remove(3)
print("set without number 3:",set3)

##odd_numbers = [1,3,5,7,9]
##if 1 or 4 in odd_numbers:
##    print('true')
