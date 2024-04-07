# June 2023 Section B AQA Computer Science A-Level Paper 1

def unique(inputstring):
    seen = set()
    for character in inputstring:
        if character in seen:
            return False
        seen.add(character)
    return True

def asciivalues(inputstring):
    total = 0
    for character in inputstring:
        total += ord(character)
    return total

def validation():
    inputstring = input("Enter a string for validation: ")

    if len(inputstring) < 5 or len(inputstring) > 7:
        print("Invalid input: invalid length.")
        return validation()

    if not inputstring.isupper():  # Simplified check for uppercase
        print("Invalid input: not capitalised.")
        return validation()

    if not unique(inputstring):  # Directly use the result of unique function
        print("Invalid input: non-unique characters.")
        return validation()

    asciisum = asciivalues(inputstring)
    if asciisum < 420 or asciisum > 600:
        print("Invalid Input: ASCII codes sum")
        return validation()

    print("Valid string!")

validation()
