print("Welcome to the Car Sales Tracking System!")
carQuantity = 100

while carQuantity > 0:
    salesQuantity = int(input("Please enter today's sales quantity: "))

    # Check if the sales quantity is a positive number
    if salesQuantity < 0:
        print("Please enter a sales quantity greater than zero.")
    else:
        # Check if sales quantity is within available stock
        if carQuantity >= salesQuantity:
            carQuantity -= salesQuantity
            print("Remaining car quantity: ", carQuantity)
        else:
            print("Sales quantity exceeds available stock.\nCurrent stock: ", carQuantity)

print("Car stock is depleted. Thank you for using the system!")
             