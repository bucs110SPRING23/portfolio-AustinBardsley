amount = (int(input("Enter Upper Limit:")))
for num in range(amount+1):
    print("Number:", num)
    if (num%15 == 0):
        print ("fizzbuzz")
    elif ((num%3) == 0):
        print("fizz")
    elif (num%5 == 0):
        print ("buzz")