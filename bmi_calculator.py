def bmi_calculator(weight, height):
    bmi = weight / (height / 100) ** 2
    return round(bmi, 2)
