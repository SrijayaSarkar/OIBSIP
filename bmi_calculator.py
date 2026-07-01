print("=" * 40)
print("      BMI CALCULATOR")
print("=" * 40)

try:
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    if weight <= 0 or height <= 0:
        print("Weight and height must be greater than zero.")
    else:
        bmi = weight / (height ** 2)

        print("\nYour BMI is:", round(bmi, 2))

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal Weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print("Category:", category)

except ValueError:
    print("Please enter valid numeric values.")