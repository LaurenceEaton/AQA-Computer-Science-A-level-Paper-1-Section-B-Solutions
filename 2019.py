# June 2019 Section B AQA Computer Science A-Level Paper 1

# Write a program that gets two words from the user and then displays a message
# saying if the first word can be created using the letters from the second word or not.

firstword = input("Enter a word: ")
secondword = input("Enter another word: ")
count = 0

for i in range(len(secondword)):
    if secondword[i] in firstword:
        count += 1
        
if count >= len(firstword):
    print("works")
else:
    print("doesn't work")