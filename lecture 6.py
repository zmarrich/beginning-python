message=input("Please enter a string in lowercase: ")
letter=input("what letter are you looking for? ")
count = 0
for char in message:
    if char == letter:
        count +=1

print("I found ",letter,count," times")


