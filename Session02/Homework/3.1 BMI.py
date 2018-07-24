height = int(input("Height: "))
weight = int(input("Weight: "))
BMI = weight/((height/100)**2)
if BMI < 16:
    print("Severely underweight")
elif BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal")
elif BMI <30:
    print("Overweight")
else:
    print("Obese")