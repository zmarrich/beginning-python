def vowel_count(string):
    count = 0
    y_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']

    for letter in string:
        if letter in vowels:
            count += 1
        elif letter == "y":
            y_count += 1

    return count , y_count

#main
message = ("This is a test message. This is only a test. Only!")

###output=vowel_count(message)
total, ys=vowel_count(message)

print(message)
print("The message has",total, "vowels in it.")
print("It also has", ys, "y's in it.")

######PART 2

with open("professions.txt", "r") as F:
    data = []
    for lines in F:
        data.append(lines.split())
        print(lines)

print()
print("All the data: \n", data)


for lines in data:
    print(lines[1])
    

