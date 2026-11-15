def get_numeric_input(prompt, allow_zero=False):
    while True:
        try:
            # Try to convert the input to a valid float (non-zero, non-negative)
            # value is assigned to whatever input is received from the user
            # (input(prompt)) is is assigned to the 'get_numeric_input' function's 'value' variable, thus calling that function
            # The float(input(prompt)) tries to convert the input to a float before assigning it to 'value'
            value =  float(input(prompt))
            # If float can convert the input successfully, the value is returned
            if allow_zero and value < 0:
                print("Tip percentage cannot be negative. Please enter a non-negative number.")
                continue
            # Reject zero and negative numbers
            elif not allow_zero and value <= 0:
                print("Zero and negative numbers are not allowed. Please enter a positive number.")
                continue
            
            return value
        # If the input cannot be converted to a float, a ValueError is raised and caught here
        # The user is prompted to enter a valid number until a valid input is provided
        except ValueError:
            print("Please enter a valid number.")

def get_positive_int(prompt):
    while True:
        try:
            # Converts input into an integer for headcount
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")

def main():
    print("Hey there!  I am here to help you calculate tips for your bill")

    # Asking for user input, but this time using the get_numeric_input function to ensure valid numeric input
    # in the first input case, prompt from the function is "First, enter the amount of the bill: " which is set to the 'bill' variable
    bill = get_numeric_input("First, enter the amount of the bill: ")
    # Should be >= 0, so allow_zero=True is used here
    tip = get_numeric_input("Now, enter the tip percentage: ", allow_zero=True)

    split = get_positive_int("How many people are splitting the bill? ")

    # calculations
    tip_amount = bill * (tip / 100)
    overall = bill + tip_amount
    amount_per_person = overall / split

    print("\n--- The Breakdown ---")
    print(f"Original bill:  ${bill:.2f}")
    print(f"Tip amount:     ${tip_amount:.2f}")
    print(f"Total with tip: ${overall:.2f}")
    print(f"Amount per person (Split by {split}): ${amount_per_person:.2f}")

if __name__ == "__main__":
    main()





