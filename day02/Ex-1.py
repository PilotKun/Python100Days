two_digit_number = input("Type a two digit number:")

# first_digit = ("two_digit_number"[0]) here this is a string not a vatiable
# second_digit = ("two_digit_number"[1]) here this is a string not a vatiable

first_digit = two_digit_number[0] # now this a variable 
second_digit = two_digit_number[1] 

result = int(first_digit) + int(second_digit)

print(result)