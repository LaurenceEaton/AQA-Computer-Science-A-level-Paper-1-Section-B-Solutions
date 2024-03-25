# June 2017 Section B AQA Computer Science A-Level Paper 1


s = input("Enter text to compress: ")


count = 0
lastChar = s[0]

for i in range(1,len(s)):
    count += 1
    thisChar = s[i]
			
    if (thisChar != lastChar):
        lastChar = str(lastChar)
        print(lastChar + " " + str(count) + " ")
        count = 0
        lastChar = thisChar


print(lastChar + " " + str(count + 1))