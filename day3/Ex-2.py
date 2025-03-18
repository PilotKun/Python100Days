height = float(input("enter ur height in m: "))
weight = float(input("enter ur weught in kg: "))

bmi = weight/(height*height)
rounded_bmi = round(bmi, 2)

if rounded_bmi <= 18.5:
    print(f"you r underwieght with a bmi of {rounded_bmi}")
elif rounded_bmi <= 25:
    print(f"you are normal with a bmi of {rounded_bmi}")
elif rounded_bmi <= 30:
    print(f"you r overweight with a bmi of {rounded_bmi}")
elif rounded_bmi <= 35:
    print(f"you r obese with a bmi of {rounded_bmi}")
else:
    print(f"you r clinically obese with a bmi of {rounded_bmi}")

