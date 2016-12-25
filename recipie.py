def printRecipe():
    file=open("recepie.txt","r")
    fileContent=file.read() #chunk
    print(fileContent)
    file.close()

printRecipe()


def printRecipe():
    file=open("recepie.txt","r")
    fileContent=file.readlines() #newlines stuck together!


    print(fileContent)
    file.close()
printRecipe()

def printRecipe():
    file=open("recepie.txt","r")
    fileContent=file.readlines() #line in file newlines stuck together!
    for line in fileContent:
        print(line)
    file.close()
printRecipe()


lookfor=input("what word do you want to look for?")
def printRecipe():
    file=open("recepie.txt","r")
    fileContent=file.readlines(" ") #line in file newlines stuck together!
    for line in fileContent:
        for word in line:
        print(word)
    file.close()
printRecipe()

lookfor=input("what word do you want to look for?")
def printRecipe():
    count=0
    file=open("recepie.txt","r")
    fileContent=file.readlines(" ") #line in file newlines stuck together!
    for line in fileContent:
        line=line.split()
        for word in line:
            if word.lower() == lookfor.lower():
                count+=1
    print(word, "occurs", count)
    file.close()
printRecipe()


