print("Hey there!  I am here to help you calculate tips for your bill")

input("Press Enter to continue...")

bill = float(input("First, enter the amount of the bill: "))

tip = float(input("Now, enter the tip percentage: "))

overall = bill + bill * tip / 100

print(f"The total is ${bill} | the tip amount is ${overall - bill} | The total amount with tip is ${overall}")

