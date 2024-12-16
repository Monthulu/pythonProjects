#This program will give the user an estimated
#price for a paint job with given information
#Lamont Redd

#import math module
import math
#define functions and check err
def getFloatInput(promptMessage):
    try:
        while True:
            fValue = float(input(promptMessage))
            if fValue > 0:
                break
            else:
                print("Input must be a positive numeric value")
        return fValue
    except Exception as e:
        print(f"Error: {e}")

def getGallonsOfPaint(squareFeetWall, feetPerGallon):
    try:
        while True:
            result = math.ceil(squareFeetWall / feetPerGallon)
            if squareFeetWall > 0 and feetPerGallon > 0:
                break
            else:
                print("Input must be a positive numeric value")
        return result
    except Exception as e:
        print(f"Error: {e}")

def getLaborHours(laborHours, totalGallons):
    try:
        while True:
            result = laborHours * totalGallons
            if laborHours > 0 and totalGallons > 0:
                break
            else:
                print("Input must be a positive numeric value")
        return result
    except Exception as e:
        print(f"Error: {e}")

def getLaborCost(laborHours, paintingCharge):
    try:
        while True:
            result = laborHours * paintingCharge
            if laborHours > 0 and paintingCharge > 0:
                break
            else:
                print("Input must be a positive numeric value")
        return result
    except Exception as e:
        print(f"Error: {e}")

def getPaintCost(totalGallons, paintPrice):
    try:
        while True:
            result = totalGallons * paintPrice
            if totalGallons > 0 and paintPrice > 0:
                break
            else:
                print("Input must be a positive numeric value")
        return result
    except Exception as e:
        print(f"Error: {e}")

def getSalesTax(state):
    try:
        if state == 'CT':
            return .06
        elif state == 'MA':
            return .0625
        elif state == 'ME':
            return .085
        elif state == 'NH':
            return 0.0
        elif state == 'RI':
            return .07
        elif state == 'VT':
            return .06
        else:
            return 0.0
    except Exception as e:
        print(f"Error: {e}")

def showCostEstimate(sqrFeetWall, paintPrice, ftPerGallon, hoursPerGallon, paintLaborPerHour, state, customerLastName):
    try:
        name_file = open(f"{customerLastName}_PaintJobOutput.txt", "w")

        nGallonsNeeded = getGallonsOfPaint(sqrFeetWall, ftPerGallon)
        fHoursOfLabor = getLaborHours(nGallonsNeeded, hoursPerGallon)
        fPaintCost = getPaintCost(nGallonsNeeded, paintPrice)
        fLaborCost = getLaborCost(paintLaborPerHour, fHoursOfLabor)
        fTax = (fLaborCost + fPaintCost) * getSalesTax(state)
        fTotalCost = (fLaborCost + fPaintCost) + fTax

        print(f"Gallons of paint: {nGallonsNeeded}")
        print(f"Hours of labor: {fHoursOfLabor}")
        print(f"Paint charges: ${fPaintCost:,.2f}")
        print(f"labor charges: ${fLaborCost:,.2f}")
        print(f"Tax: ${fTax:,.2f}")
        print(f"Total Cost: ${fTotalCost:,.2f}")

        name_file.write(f"Gallons of paint: {nGallonsNeeded} \n")
        name_file.write(f"Hours of labor: {fHoursOfLabor} \n")
        name_file.write(f"Paint charges: ${fPaintCost:,.2f} \n")
        name_file.write(f"labor charges: ${fLaborCost:,.2f} \n")
        name_file.write(f"Tax: ${fTax:,.2f} \n")
        name_file.write(f"Total Cost: ${fTotalCost:,.2f} \n")
        name_file.close()
        print(f"File: {customerLastName}_PaintJobOutput.txt was created.")
    except Exception as e:
        print(f"Error: {e}")

#Main function
def main():
    try:
        fSqrFeetWall = getFloatInput("Enter wall space in square feet: ")
        fPaintPrice = getFloatInput("Enter paint price per gallon: ")
        fFtPerGallon = getFloatInput("Enter feet per gallon: ")
        fHoursPerGallon = getFloatInput("How many labor hours per gallon: ")
        fPaintLaborPerHour = getFloatInput("Labor charge per hour: ")
        sState = input("State job is in: ")
        sCustomerLastName = input("Customer Last Name: ")

        showCostEstimate(fSqrFeetWall, fPaintPrice, fFtPerGallon, fHoursPerGallon, fPaintLaborPerHour, sState, sCustomerLastName)
    except Exception as e:
        print(f"Error: {e}")

#Call main function
main()
