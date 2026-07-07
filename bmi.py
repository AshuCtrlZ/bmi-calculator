
#making a bmi calculator
weight = float(input("What is your weight (kg)? ")).strip()
height = float(input("What is your height (m)? ")).strip()

bmi = weight/(height ** 2)

print(f"BMI = {round(bmi, 2)}")

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal weight")
elif 25 <= bmi < 30:
    print("Class I Obesity")
elif 30 <= bmi < 40:
    print("Class II Obesity")
else:
    print("Class III Obesity") 