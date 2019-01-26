#Python 3.7, Julian Piñeiro for Nikolai
#Shipping Calculator.
cont="y" #instantiate the continue (cont) value to enter the while below.
cost = 0.00 #Set up initial shipping cost.
print("========================================================\n")
print("SHIPPING CALCULATOR\n") #presentation.
print("========================================================\n")
while (cont!= "n"): #External while to control execution repetitions.
    #Get input number to "num" variable -> cast to float
    #This allows decimal number handling such as currencies.
    num = float(input("Cost of items ordered: "))

    while (num <= 0):
        #Exception if invalid number.
        print("You must enter a positive number. Please try again.\n")
        num = input("Cost of items ordered: ")

    #pricing conditions as marked in the table.
    if num<=30.00:
        cost=5.95
    elif num<=49.99:
        cost = 7.95
    elif num<=74.99: #if cost does not enter in any pricing category, it remains 0.00
        cost = 9.95

    #Data presentation
    print("Shipping cost:       $"+str(cost))
    print("Total cost:          $"+str(round(num+cost,2))+"\n") #Round result to two decimals
    #Prompt for control variable (cont) modification.
    cont = input("Continue? (y/n): ")
    cont.lower() #make it lowercase, so in case the user inserts a Y it gets caught below.
    if (cont=="y"):
        #Print a separator.
        print("========================================================\n")
