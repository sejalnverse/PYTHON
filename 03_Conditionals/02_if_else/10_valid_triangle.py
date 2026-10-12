first_side = int(input("Enter the length of the first side of the triangle: "))
second_side = int(input("Enter the length of the second side of the triangle: "))
third_side = int(input("Enter the length of the third side of the triangle: "))
if first_side and second_side and third_side > 0:
    if (first_side + second_side > third_side) and (first_side + third_side > second_side) and (second_side + third_side > first_side):
        print("The triangle is valid.")
    else:
        print("The triangle is not valid.")