# June 2020 Section B AQA Computer Science A-Level Paper 1

inputs = int(input("Input how many digits you would like to enter: "))
numbers = []
max_count = 0
most = None
multimodal = False

for i in range(0, inputs):
    digit = input("Enter a digit: ")
    numbers.append(digit)

for digit in numbers:
    count = numbers.count(digit)
    if count > max_count:
        most = digit
        max_count = count
        multimodal = False
    elif count < max_count:
        multimodal = False

if max_count > 1 and not multimodal:
    print(most)
else:
    print("Multimodal")




