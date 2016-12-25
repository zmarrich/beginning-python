
###SLIDE ONE
print("She said, '"'I dont like to wear a helmet it messes up my hair'"',which is really silly")
print("Yes\\No?")
print("April\nMay\nJune\n")
#####SLide TWO
message= 'I like Python.'
print(message.lower())
print(message.upper())
print(message.replace('Python','Pasta',1))
#slide 3
##statement='I like to go shopping for clothes'
##print(statement.split(" ")) 
##
##list="pants, shirts, dresses, socks, skirt, tie"
##print(list.split(","))
###SLIDE 4
##statement="I like to go \nshopping for clothes"
##print(statement.strip())
##
##months="\t\t\njan\nfeb\nmar\napr\nmay\njun\njul\naug\nsep\noct\nnov\ndec\n\t\t"
##print(months.strip())
##print()
###slide5
##statement="I like to go shopping for new tech toys."
##print(statement[30:39])
##print(statement[-9:-1])
##
###slide 6
###word triangle
message=input('Please enter a message:')
count=1
for i in range(len(message)):
    print(message[:count])
    count+=1
#NEGITIVE INDEX 
for i in range(len(message)):
    print(message[:i+1])
for i in range(len(message)):
    print(message[:-i-1])
