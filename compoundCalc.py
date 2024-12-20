# Compound interest Calculator
# Lamont Redd
# This program will calculate the compound interest gained over the entered time.

# Input and Conversions
fPrincipalInvestment = float(input("Enter the starting principal: "))
fInterestRate = float(input("Enter the annual interest rate: "))
fTimesPerYear = float(input("How many times per year is the interest compounded?: "))
fCompoundingTime = float(input("For how many years will the account earn interest?: "))

# Calculations
nFutureValue = fPrincipalInvestment * (1 + (fInterestRate / 100) / fCompoundingTime ) ** (fCompoundingTime * fTimesPerYear)

# Output and Formating
print(f"At the end of 2 years you will have ${nFutureValue:0,.2f}")
