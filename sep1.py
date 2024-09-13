def getTicketPrice(age):
    if age <= 3:
        return 0
    elif age <= 11:
        return 7
    elif age <= 65:
        return 10
    else:
        return 8




name = input("Please enter your name: ")
for age in range(1,26):
    print("My name is",name,"and I am",age,"years old")
    price = getTicketPrice(age)
    print("And I pay ",price,"dollars to watch movies.")
    #if age < 20:
    #    print("...I'm so young!")
    #else:
    #    print("...I'm so old!")
    
friends = ["Dain", "Moana", "Donovan", "Hikaru"]
for f in friends:
    print("My name is",f,"and my favorite class is CIS 205.")

