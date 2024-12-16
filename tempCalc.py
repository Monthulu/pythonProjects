# This program will convert temps between degrees Celsius and Fahrenheit
#Lamont Redd

#Input
print("This is Lamont's Temperature Converter:")
fTemp = float(input("Enter a temperature: "))
sTempType = input("Is the temp F for Fahrenheit or C for Celsius? ")

#Calculations / Constants
fCELSIUS = (5.0 / 9) * (fTemp - 32)
fFAHRENHEIT = (((9.0 / 5.0) * fTemp) + 32)

#Output
if fTemp > 100 and (sTempType == "C" or sTempType == "c"): #Determine if C Temp exceeds 101
    print(f"Temp can not be >100")
elif sTempType == "C" or sTempType == "c":
    print(f"The Fahrenheit equivalent is: {fFAHRENHEIT:0.1f}")
elif fTemp > 212 and (sTempType == "F" or sTempType == "f"): #Detemine if F Temp exceeds 212
    print(f"Temp can not be >212")
elif sTempType == "F" or sTempType == "f":
    print(f"The Celsius equivalent is: {fCELSIUS:0.1f}")
else:
    print(f"You must enter a F or C")



Input
print("This is Lamont's Temperature Converter:")
fTemp = float(input("Enter a temperature: "))
sTempType = input("Is the temp F for Fahrenheit or C for Celsius? ").lower()

def mycelsius_converter(myTemperature):
    return (5.0 / 9) * (myTemperature - 32)

def my_fahrenheit_converter(myTemperature):
    return (((9.0 / 5.0) * myTemperature) + 32)

Output
match sTempType:
    case 'c':
        if fTemp > 100:
            print(f"Temp can not be >100")
        else:
            print(f"The Fahrenheit equivalent is: {my_celsius_converter(fTemp):0.1f}")
    case 'f':
        if fTemp > 212:
            print(f"Temp can not be >212")
        else:
            print(f"The Fahrenheit equivalent is: {my_fahrenheit_converter(fTemp):0.1f}")
    case :
        print(f"You must enter a F or C")


Input
print("This is Lamont's Temperature Converter:")
fTemp = float(input("Enter a temperature: "))
sTempType = input("Is the temp F for Fahrenheit or C for Celsius? ").lower()

def my_celsius_converter(myTemperature):
    return (5.0 / 9) * (myTemperature - 32)

def my_fahrenheit_converter(myTemperature):
    return (((9.0 / 5.0) * myTemperature) + 32)

Output
if sTempType.lower() == 'c' or sTempType.lower() == 'f':
    if sTempType == 'c' and fTemp > 100:
        print(f"Temp can not be >100")
    elif sTempType == 'c':
        print(f"The Fahrenheit equivalent is: {my_celsius_converter(fTemp):0.1f}")
    elif sTempType == 'f' and fTemp < 212:
        print(f"Temp can not be >212")
    elif sTempType == 'f':
        print(f"The Fahrenheit equivalent is: {my_fahrenheit_converter(fTemp):0.1f}")
    else:
       print("how'd you get here")
else:
    print(f"You must enter a F or C")



