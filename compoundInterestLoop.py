#This program will compute the compound interest
#Telling the amount of months it will take to reach a specified goal
#Lamont Redd

#Input and testing to see if values greater than zero
while True:
    fDeposit = float(input("What is the Original Deposit (positive value):"))
    if fDeposit > 0:
        break  #exit loop
    else:
        print("Input must be a positive numeric value")
while True:
    fInterestRate = float(input("What is the Interest Rate (positive value:)"))
    if fInterestRate > 0:
        break
    else:
        print("Input must be a positive numeric value")
while True:
    nMonths = int(input("What is the number of Months:"))
    if nMonths > 0:
        break
    else:
        print("Input must be a positive numeric value")
while True:
    fGoalAmount = float(input("What is the Goal Amount (can enter 0 but not negative):"))
    if fGoalAmount >= 0:
        break
    else:
        print("Input must be a positive numeric value")

#Convertions
fAccountBalance = fDeposit
fFinalValue = fDeposit * (1 + (fInterestRate / 100) / nMonths) ** (nMonths * fGoalAmount)
fMonthlyInterestRate = (fInterestRate / 100) / 12

#Output
for Month in range(1,nMonths + 1): #Account Balance per month
    fAccountBalance += fDeposit * fMonthlyInterestRate
    print(f"Month: {Month} Account Balance is: $ {fAccountBalance:0,.2f} ")
nCount = 0
fAccountBalanceGoal = fDeposit
while fAccountBalanceGoal < fGoalAmount: #Amount of months to reach goal
    fAccountBalanceGoal += fDeposit * fMonthlyInterestRate
    nCount += 1
print(f"It will take: {nCount} months to reach the goal of $ {fGoalAmount:0,.2f} ")

