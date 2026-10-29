# getting input from user The input function returns the input as a string.

input_data = input("Enter your name: ")
input_age = input("Enter your age: ")

print("Welcome " + input_data)
print("You are " + input_age + " years old.")


user_input = input("Enter a number: ")
user_second_input = input("Enter another number: ")

print("The sum of the two numbers is: " + str(int(user_input) + int(user_second_input)))