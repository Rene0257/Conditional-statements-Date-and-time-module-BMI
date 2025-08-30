h = float(input("Enter your height in centimeters: "))
w = float(input("Enter your weight in kilograms: "))

BMI = w/(h/100)**2
print("Your BMI is: " , BMI)

if BMI<=18.5:
    print("Underweight")
elif BMI<=24.9:
    print("Perfect")
elif BMI<=29.9:
    print("Slightly overweight")
else:
    print("Overweight")