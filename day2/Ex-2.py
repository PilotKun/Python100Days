height = input("enter ur height in m: ")
weight = input("enter ur weight in kg: ")

height = float(height)
weight = float(weight)

BMI = weight/height ** 2 
BMI_as_int = int(BMI) # b4 adding this it was giving it in decimals but now in whole numbers
print(BMI_as_int)