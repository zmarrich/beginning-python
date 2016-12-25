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



######SLIDE ONE
##shoeChoice=["Nike","NB","Boots","Flats","Stand Smith", "Sandel"]
##for shoe in shoeChoice:
##    print(shoe, end="|")
##print()
##for shoe in shoeChoice:
##    print(shoe, end="\t")
####SLIDE TWO
##tips=[("Monday", 30),("Friday", 23),("Sunday", 23)]
##for dollars in tips:
##    day, total= dollars
##    print(day, total, sep ="\t")


####SLIDE 3
def table_print(headers, data):
    for header in headers:
        print(header,end="\t")
    print()
    print("*"*25)
    
    for i in range(len(data)):
        print(i, data[i][0],data[i][1], sep="\t")
        

labels=["i","type","form",]
media=[("music","mp3"),("music","mp4"),("message","text"),("message","imessage")]
table_print(labels, media)
