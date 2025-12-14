
print("Welcome to the tip calculator ")
totalBill = int(input("What was the total bill?  "))
tipOnBill = int(input("How much tip/percentage would you like to give? 10, 12 or 15?   "))
noOfPeople = int(input("How many people to split the bill? "))
billOnEach = (totalBill + (totalBill*(tipOnBill/100)))/(noOfPeople)
print("Each person should pay:  "+str(billOnEach)+ " Naira")