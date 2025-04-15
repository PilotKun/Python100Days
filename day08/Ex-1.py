import math

def paint_clac(height, width, cover):
    area = height*width
    num_of_cans = math.ceil(area/cover)
    print(f"you will need {num_of_cans} cans of paint")

test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5
paint_clac(height=test_h, width=test_w, cover=coverage)