# November 2021 Section B AQA Computer Science A-Level Paper 1

n = int(input("Enter the nth harshad number you want: "))

harshads = []


def harshad(i):
    digits = [int(digit) for digit in str(i)]
    if i % sum(digits) == 0:
        harshads.append(i)

for i in range(1,1000000):
    harshad(i)
    
print(harshads[n-1])