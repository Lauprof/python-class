def show_menu():
    print("==" * 20)
    print("Welcome to the maths app. Select any of the following options 1, 2, 3, 4, or 5 to exit.")
    print("==" * 20)
    print("1. Area of rectangle")
    print("2. Area of circle")
    print("3. Check if odd or even")
    print("4. Product of 3 numbers")
    print("5. Exit")


def area_of_rectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is {area}")


def area_of_circle():
    radius = float(input("Enter the radius of the circle: "))
    pi = 3.142
    area = pi * radius * radius
    print(f"The area of the circle is {area}")


def check_odd_or_even():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")


def product_of_three_numbers():
    print("Enter three numbers to find their product")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    result = num1 * num2 * num3
    list_of_numbers = [num1, num2, num3]
    print(f"The product of {list_of_numbers} is: {result}")


def exit_app():
    print("Goodbye!")


def runprogram():
    choices = {
        "1": area_of_rectangle,
        "2": area_of_circle,
        "3": check_odd_or_even,
        "4": product_of_three_numbers,
        "5": exit_app,
        "exit": exit_app,
        "Exit": exit_app,
    }

    show_menu()
    while True:
        user_choice = input("Choose option: ")

        if user_choice not in choices:
            print("Invalid option. Please choose from 1 to 5.")
        else:
            choices[user_choice]()
            if user_choice in ("5", "exit", "Exit"):
                break

        show_menu()


runprogram()
