data_file=open("professions.txt","r")
data=data_file.readlines()
data_file.close()

clean_data=[]
for person in data:
    clean_data.append(person.strip().split(", "))
print(clean_data)
print("'p1"*20)
sorteddata=[clean_data.pop()]
print(sorteddata)
print("p2"*20)
while clean_data:
    current=clean_data.pop()
    
    for i in range(len(sorteddata)):
        if int(current[1]) < int(sorteddata[i][1]):
            sorteddata.insert(i,current)
            current=""
            print("p3"*20)
            print(sorteddata)
            break
    print("p4"*20)
    print(sorteddata)
    if current:
        sorteddata.append(current)
        print("p5"*20)
        print(sorteddata.append(current))

for entry in sorteddata:
    print("p6"*20)
    print(entry)
    
