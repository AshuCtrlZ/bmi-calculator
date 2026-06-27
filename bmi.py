
#making a bmi calculator
weight = float(input("What is your weight (kg)? "))
height = float(input("What is your height (m)? "))

bmi = weight/(height ** 2)

print(f" BMI = {round(bmi, 2)}")