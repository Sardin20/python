import sys

def calculate_bmi(weight, height):
    """
    Calculate BMI using the formula:
    BMI = weight (kg) / (height (m))^2
    """
    return weight / (height ** 2)


def main():
    print("Welcome to the BMI Calculator!")

    if len(sys.argv) != 3:
        print("Usage: python3 app.py <weight> <height>")
        sys.exit(1)

    try:
        # Get weight and height from command-line arguments
        weight = float(sys.argv[1])
        height = float(sys.argv[2])

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values.")
            return

        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        # Display the result
        print(f"Your BMI is {bmi:.2f}. You are classified as: {category}")
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")


if __name__ == "__main__":
    main()
