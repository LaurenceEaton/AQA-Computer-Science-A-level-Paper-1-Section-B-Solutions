#  June 2018 Section B AQA Computer Science A-Level Paper 1


def june2018():
    prime = True
    number = int(input("enter a number: "))

    if number <= 1:
        print("Not Greater than 1")
        june2018()

    elif number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                prime = False

    if prime == True:
        print("Is a prime number")
        june2018()

    elif prime == False:
        print("Is not a prime number")
        june2018()
        
june2018()
