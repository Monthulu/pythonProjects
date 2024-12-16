
#This program will determine a letter grade
#After 4 test scores are entered and before the lowest is dropped.
#Lamont Redd

#Input
sName = input("Name of person that we are calculating the grades for: ")
nTestOne = int(input("Test 1: "))
nTestTwo = int(input("Test 2: "))
nTestThree = int(input("Test 3: "))
nTestFour = int(input("Test 4: "))
sGradeDrop = input("Do you wish to Drop the Lowest Grade Y or N? ")
sLetterGrade = ""
fAverageScore = 0.0

#Output
if nTestOne <= 0 or nTestTwo <= 0 or nTestThree <= 0 or nTestFour <= 0: #Make sure score is greater than 0
    print("The score must be greater than 0")
    exit()
else:
    if sGradeDrop == "N":
        fAverageScore = (nTestTwo + nTestThree + nTestOne + nTestFour) / 4
        print(f"{sName} test average is: {fAverageScore:0.1f}")
    elif sGradeDrop == "Y":
        if nTestOne <= nTestTwo and nTestOne <= nTestThree and nTestOne <= nTestFour:
            fAverageScore = (nTestTwo + nTestThree + nTestFour) / 3
            print(f"{sName} test average is: {fAverageScore:0.1f}")
        elif nTestTwo <= nTestOne and nTestTwo <= nTestThree and nTestTwo <= nTestFour:
            fAverageScore = (nTestOne + nTestThree + nTestFour) / 3
            print(f"{sName} test average is: {fAverageScore:0.1f}")
        elif nTestThree <= nTestOne and nTestThree <= nTestTwo and nTestThree <= nTestFour:
            fAverageScore = (nTestOne + nTestTwo + nTestFour) / 3
            print(f"{sName} test average is: {fAverageScore:0.1f}")
        elif nTestFour <= nTestOne and nTestFour <= nTestTwo and nTestFour <= nTestThree:
            fAverageScore = (nTestOne + nTestThree + nTestTwo) / 3
            print(f"{sName} test average is: {fAverageScore:0.1f}")
    else:
        print("Enter Y or N to Drop the Lowest Grade.")
        exit()
    if fAverageScore >= 97.0:  #Find the letter grade
        sLetterGrade = "A+"
    elif fAverageScore >= 94.0:
        sLetterGrade = "A"
    elif fAverageScore >= 90.0:
        sLetterGrade = "A-"
    elif fAverageScore >= 87.0:
        sLetterGrade = "B+"
    elif fAverageScore >= 84.0:
        sLetterGrade = "B"
    elif fAverageScore >= 80.0:
        sLetterGrade = "B-"
    elif fAverageScore >= 77.0:
        sLetterGrade = "C+"
    elif fAverageScore >= 74.0:
        sLetterGrade = "C"
    elif fAverageScore >= 70.0:
        sLetterGrade = "C-"
    elif fAverageScore >= 67.0:
        sLetterGrade = "D+"
    elif fAverageScore >= 64.0:
        sLetterGrade = "D"
    elif fAverageScore >= 60.0:
        sLetterGrade = "D-"
    elif fAverageScore <= 59.9:
        sLetterGrade = "F"
    print(f"Letter Grade for the test is: {sLetterGrade}")

