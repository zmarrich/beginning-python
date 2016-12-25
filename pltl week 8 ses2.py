##sum = 0
##num = input("Please enter a number or STOP: ")
##
##while num.upper() != "STOP":
##    sum+=int(num)
##    num=input("Please enter a number or STOP: ")
##print("The total sum is", sum)


lookfor=input("Would you want a STORY before bed or type STOP: ")
fileContent=""
while lookfor.upper() !="STOP":
    file=open("quote.txt","r")
    fileContent=file.readlines() #line in file newlines stuck together!
    file.close()
    print (fileContent)
    lookfor=input("Would you want a STORY before bed or type STOP: ")    
