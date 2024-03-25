# June 2022 Section B AQA Computer Science A-Level Paper 1

vowels = "aeiou"
swapped_string = ""
userstring = input("Enter a string: ")

vowelsinstringlist = [char for char in userstring if char in vowels]
totalvowelscount = len(vowelsinstringlist)

# Swap the vowels in the input string
for character in userstring:
    if character in vowels:
        swapped_string += vowelsinstringlist[totalvowelscount - 1]
        totalvowelscount -= 1
    else:
        swapped_string += character

print(swapped_string)



