import math


def paint_calc(height, width, cover):
    cans_decimal = round((height * width) / cover)
    cans_round = math.ceil(cans_decimal)
    print(f"You need {cans_round} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
