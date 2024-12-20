#This program will analyze real estate sales.
#Lamont Redd

#define functions and check err
def getFloatInput(promptMessage):
    try:
        nCount = 0
        while True:
            fValue = input(promptMessage)

            if fValue.isdigit():
                fValue = float(fValue)
                if fValue > 0:
                    break
                else:
                    if nCount == 0:
                        print("Input a number that is greater than 0.")
                    nCount += 1
            else:
                if nCount == 0:
                    print("Input a number that is greater than 0.")
                nCount += 1
        return fValue
    except Exception as e:
        print(f"Error: {e}")
#Median
def getMedian(listOfNumbers):
    try:
        nListCount = len(listOfNumbers)
        if nListCount % 2 == 0:
            nMidPoint = int(nListCount / 2)
            nMedian = (listOfNumbers[nMidPoint-1] + listOfNumbers[nMidPoint]) / 2
        else:
            nMidPoint = int((nListCount // 2) + 1)
            nMedian = listOfNumbers[nMidPoint - 1]

        return nMedian

    except Exception as e:
        print(f"Error: {e}")

#Main function and output
def main():
    try:
        nlistPropertyValue = []

        while True:
            nPropertyValue = getFloatInput("Enter property sales value: ")
            nlistPropertyValue.append(nPropertyValue)
            while True:
                inputResponse = input("Enter another property value Y or N: ")
                if inputResponse.lower() == 'n' or inputResponse.lower() == 'y':
                    break
                else:
                    pass

            if inputResponse.lower() == 'n':
                break
            else:
                pass

        nlistPropertyValue.sort()

        nCount = 1
        nPropertyTotal = 0
        for propertyValue in nlistPropertyValue:
            print(f"Property {nCount} $ {propertyValue:,.2f}")
            nCount += 1
            nPropertyTotal += propertyValue

        print(f"Minimum: $ {nlistPropertyValue[0]:,.2f}")
        print(f"Maximum: $ {nlistPropertyValue[-1]:,.2f}")
        print(f"Total: $ {nPropertyTotal:,.2f}")
        print(f"Average: $ {(nPropertyTotal / len(nlistPropertyValue)):,.2f}")
        print(f"Median: $ {getMedian(nlistPropertyValue):,.2f}")
        print(f"Commission: $ {(nPropertyTotal * .03):,.2f}")

    except Exception as e:
        print(f"Error: {e}")

#Call main function
main()