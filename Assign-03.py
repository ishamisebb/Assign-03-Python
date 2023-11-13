#!/usr/bin/env python3
# Created By: Ishami Sebgoya
# Date: November 6 2023
# This program identifies whether a shape is a square or a rectangle.


def main():
    options = input(
        "Would you like:\n[1]Identify what type of shape it is\n[2]Identify the area and perimeter of a square\n[3]Identify the area and perimeter of a rectangle\n[4]Run all of them\n"
    )
    length_str = input("Enter the length : ")
    width_str = input("Enter the width : ")

    def identify_shape():
        if length_float == width_float:
            print("This form a square")
        else:
            print("This form a rectangle")

    def area_peri_sqr():
        perimeter = 4 * (length_float + width_float)
        print("The perimeter equal {} ".format(round(perimeter, 2)))
        area = length_float * width_float
        print("The area equal {} ".format(round(area, 2)))

    def area_peri_rec():
        perimeter = 2 * (length_float + width_float)
        print("The perimeter equal {} ".format(round(perimeter, 2)))
        area = length_float * width_float
        print("The area equal {} ".format(round(area, 2)))

    try:
        options = int(options)
        length_float = float(length_str)
        width_float = float(width_str)
    except ValueError:
        print("Invalid input")

    else:
        if options == 1:
            identify_shape()
        elif options == 2:
            area_peri_sqr()
        elif options == 3:
            area_peri_rec()
        elif options == 4:
            identify_shape()
            area_peri_sqr()
            area_peri_rec()
        else:
            print("Please enter a valid option.")


if __name__ == "__main__":
    main()
