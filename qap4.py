# Author: Jeff Woolridge
# Date: 22/03/2025
# Description: Information receipt for Insurance Policy

# Importing libraries
import datetime as dt

# Constants
CUR_DATE = dt.datetime.now()
POLICY_NUM = 1944
BASIC_PREM = 869.00
MULTI_VEHICLE_DISCOUNT = 0.25
LIABILTY_COVERAGE = 130.00
GLASS_COVERAGE = 86.00
LOAN_COVERAGE = 58.00
HST = 0.15
PROCESS__FEE = 39.99
ALLOWED_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ -'abcdefghijklmnopqrstuvwxyz"
PROVINCES = ["AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE", "QC", "SK", "YT"]

# Functions
# Formats the postal code to X#X #X#
def formatPostalCode(postalCode):
    postalCode = postalCode.replace(" ", "").upper()
    if len(postalCode) == 6:
        return postalCode[:3] + " " + postalCode[3:]
    return postalCode

# Validates the postal code to X#X #X#
def validatePostalCode(postalCode):
    if len(postalCode) != 7:
        return False
    if postalCode[0].isalpha() == False or postalCode[2].isalpha() == False or postalCode[5].isalpha() == False:
        return False
    if postalCode[1].isdigit() == False or postalCode[4].isdigit() == False or postalCode[6].isdigit() == False:
        return False
    return True
    
# Validate user input for Y/N
def getUserInput(prompt):
    while True:
        userInput = input(prompt).upper()
        if userInput in ["Y","N"]:
            return userInput
        else:
            print("Invalid input. Please enter a valid response.")

          
# Calculate the premium based on the user's input
def calculatePremium(numVehicles, extraLiability, glassCoverage, loanCoverage):
    premium = BASIC_PREM
    if numVehicles > 1:
        premium = premium - (premium * MULTI_VEHICLE_DISCOUNT)
    if extraLiability == "Y":
        premium += LIABILTY_COVERAGE
    if glassCoverage == "Y":
        premium += GLASS_COVERAGE
    if loanCoverage == "Y":
        premium += LOAN_COVERAGE
    return premium

def FDollar2(DollarValue):    # Function will accept a value and format it to $#,###.##.
    DollarValueStr = "${:,.2f}".format(DollarValue)
    return DollarValueStr

def FDateS(DateValue):    # Function will accept a value and format it to yyyy-mm-dd.
    DateValueStr = DateValue.strftime("%Y-%m-%d")
    return DateValueStr

# Function to save policy to file
def savePolicyToFile(policyData):
    with open("Policies.dat", "a") as file:
        file.write(policyData + "\n")
    
# Main Program
while True:    
    
    print()
    print("Enter the following information:") 
    print()

    # Input validation for first name
    while True: 
        firstName = input("Enter first name: ").title()
        if set(firstName).issubset(ALLOWED_CHARS) == False or firstName == "":
            print("Invalid input. Try again.")
        else:
            break
    
    # Input validation for last name
    while True:
        lastName = input("Enter last name: ").title()
        if set(lastName).issubset(ALLOWED_CHARS) == False or lastName == "":
            print("Invalid input. Try again.")
        else:
            break
    
    # Input validation for address
    while True:
        addr = input("Enter address: ").title()
        if addr == "": 
            print("Invalid input. Try again.")
        else:
            break
    
    # City input validation
    while True:
        city = input("Enter city: ").title()
        if city == "": 
            print("Invalid input. Try again.")
        else:
            break

    # Province input validation
    while True:
        province = input("Enter province (XX): ").upper()
        if province in PROVINCES:
            break
        else:                               
            print("Invalid province. Try again.")

    # Input validation for postal code, phone number, and number of vehicles
    while True:
        postalCode = formatPostalCode(input("Enter postal code (X#X #X#): ")).upper()
        if validatePostalCode(postalCode) == False:
            print("Invalid postal code. Try again.")
        else:
            break

    # Phone number input validation
    while True: 
        phoneNum = input("Enter phone number (##########): ")
        if phoneNum.isdigit() and len(phoneNum) == 10:
            break
        else:
            print("Invalid phone number. Try again.")
    
    # Number of vehicles input validation    
    while True:
        numVehicles = input("Enter the number of vehicles: ")
        if  numVehicles.isdigit() == False or numVehicles == "":
            print("Invalid input. Please enter a valid number of vehicles.")
        else:
            numVehicles = int(numVehicles)
            break
    
    # Coverage input validation        
    extraLiability = getUserInput("Do you want extra liability coverage up to $1,000,000? (Y/N): ")
    glassCoverage = getUserInput("Do you want glass coverage? (Y/N):  ")
    loanCoverage = getUserInput("Do you want loan coverage? (Y/N): ")

    # Payment type input validation
    while True:
        paymentType = input("Please enter your payment type ('F' for  Full, 'M' for Monthly, 'D' for Downpay): ").upper()
        if paymentType in ["F","M","D"]:
            break
        else:
            print("Invalid input. Please enter a valid payment type.")
    
    # Initialize downPayment to 0
    downPayment = 0

    # Down payment input validation
    if paymentType == "D":
        while True:
            downPayment = input("Enter down payment: ")
            try:
                downPayment = float(downPayment)
                if downPayment < 0:
                    print("Down payment cannot be negative. Try again.")
                else:
                    downPayment = float(downPayment)
                    break
            except:
                print("Invalid input. Please enter a valid number.")

    # Input Claim Information
    claims = []
    while True:
        
        # Claim number input validation
        claimNum = input("Enter claim number (or 'q' to finish): ").lower()
        if claimNum == "q": # Exit loop if user enters 'q'
            break
        
        # Claim date input validation
        while True:
            claimDate = input("Enter claim date (YYYY-MM-DD): ")
            try:
                claimDate = dt.datetime.strptime(claimDate, "%Y-%m-%d")
                break
            except:
                print("Invalid date format. Please use YYYY-MM-DD.")
        
        while True:
            try:
                claimAmount = float(input("Enter claim amount: "))
                if claimAmount < 0:
                    print("Claim amount cannot be negative. Try again.")
                else:
                    break
            except:
                print("Invalid input. Please enter a valid number.")
             
        # Append claim information to list
        claims.append((claimNum, claimDate, claimAmount))
    
    # Calculate the premium
    premium = calculatePremium(numVehicles, extraLiability, glassCoverage, loanCoverage)
    subtotal = premium + PROCESS__FEE
    downTotal = subtotal
    if paymentType == "D":
       downTotal = subtotal - downPayment
    finalTotal = downTotal * HST
    
    
    ## Display input information
    print()
    print("=" * 37)
    print()
    print("Policy Information")
    print("-"* 37)
    print()
    print("Date:                     ", FDateS(CUR_DATE))
    print("Policy Numer:             ", POLICY_NUM)
    print("Policy Holder:            ", firstName, lastName)
    print("Address:                  ", addr)
    print("City:                     ", city)
    print("Province:                 ", province)
    print("Postal Code:              ", postalCode)
    print("Phone Number:             ", phoneNum)
    print("Number of Vehicles:       ", numVehicles)

    if extraLiability == "Y":
        print("Extra Liability Coverage:  Yes")
    else:
        print("Extra Liability Coverage:  No")

    if glassCoverage == "Y":
        print("Glass Coverage:            Yes")
    elif glassCoverage == "N":
        print("Glass Coverage:            No")   

    if loanCoverage == "Y":   
        print("Loan Coverage:             Yes")
    elif loanCoverage == "N":
     print("Loan Coverage:             No")   
    
    if paymentType == "D":
        print("Payment Type:              Down Pay")
        print("Down Payment:             ", FDollar2(downPayment))
    elif paymentType == "F":
        print("Payment Type:              Full Payment")
    elif paymentType == "M":
        print("Payment Type:              Monthly Payment")

    print()
    print("-" * 37)
    print()
    print("Premium:                  ", FDollar2(premium))
    print("Process Fee:              ", FDollar2(PROCESS__FEE))
    print("subtotal:                 ", FDollar2(subtotal))
    print("Downpayment:              ", FDollar2(downPayment))
    print("After Downpayment:        ", FDollar2(downTotal))                                       
    print("HST:                      ", FDollar2(downTotal * HST))
    print("Total:                    ", FDollar2(downTotal * 1.15))

    print()
    print("=" * 37)
    print()

    # Display claim information
    print()
    print(f"{'Claim #':<12}{' Claim Date':<14}{'    Amount':<10}")
    print("-" * 38)
    for claim in claims:
        print(f"{claim[0]:<7}      {FDateS(claim[1]):<10}       {FDollar2(claim[2]):<5}")
    print("\n\n\n\n")

     # Save policy to file
    policyData = (  
        f"Policy Number: {POLICY_NUM}, Customer: {firstName} {lastName}, \n"
        f"Address: {addr}, City: {city}, Province: {province}, Postal Code: {postalCode}, \n"
        f"Total Cost: {FDollar2(finalTotal)}, Claims: {claims}"
    )

    # Save policy to file
    savePolicyToFile(policyData)

    print("\nPolicy saved to Policies.dat")

    break
 