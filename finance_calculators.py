# We import the module math, which provides access to the mathematical functions defined by the C standard.
import math
# We define the variable menu selection to take the input from the user, who must indicate what kind of financial operation they want to perform. To reflect the exact
menu_selection = input("investment - to calculate the amount of interest you'll earn on your investment \nbond - to calculate the amount you'll have to pay on a home loan \nEnter either 'investment' or 'bond' from the menu above to proceed: ").lower()
print(menu_selection)

valid_selections = ["investment", "bond"]

while menu_selection not in valid_selections:
    print("Invalid answer, please try again")
    menu_selection = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if menu_selection == "investment":
    amount = int(input("Please enter the amount of money you want to deposit: "))
    rate = int(input("Please enter the interest rate as percentage (%): "))
    period = int(input("Please enter the number of years you plan to invest: "))
    interest = input("Please enter if you want simple or compound interest: ").lower()
    
    if interest == "simple":
        final_amount = amount * ( 1 + rate * 0.01 * period)
        print(f"The final amount for simple interest is: {final_amount}")
    elif interest == "compound" or interest == "Compound" or interest == "COMPOUND":
        final_amount = amount * (1 + rate * 0.01) ** period
        print(f"The final amount for compound interest is: {final_amount}")
    else: print("Invalid answer, please try again")
    interest = input("Please enter if you want simple or compound interest: ")

elif menu_selection == "bond":
    present_value = int(input("Please enter the present value of the house: "))
    rate = int(input("Please enter the interest rate as percentage (%): "))
    period = int(input("Please enter the number of months for repayment: "))
    interest = rate / 1200
    repayment = (interest * present_value)/(1 - (1 + interest) ** (-period))
    print(f"The monthly repayment is: {repayment}")





        

