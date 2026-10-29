#if statements are used to make decisions in Python. They allow you to execute certain blocks of code based on whether a condition is true or false. The basic syntax of an if statement is as follows:

input_value = int(input("Enter a number: "))


if input_value > 0:
        print("The number is positive.")
elif input_value < 0:
        print("The number is negative.")
else:
        print("The number is zero.")



#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

for i in range(5):
    print(i)  # This will print numbers from 0 to 4


print("Now printing numbers using range:")
for i in range(6):
    
    print(i)  # This will print numbers from 1 to 5
#A while loop is used to execute a block of code as long as a condition is true.


while input_value < 10:
    print(f"The number is {input_value}.")
    input_value += 1  # Increment the input_value to eventually break the loop



age_user = int(input("Enter your age: "))
can_drive= input("Do you have a driving license? (yes/no): ").strip().lower()

if age_user >= 18 and can_drive == "yes":
    print("You are eligible to vote and drive.")
elif age_user >= 18 and can_drive == "no":
    print("You are eligible to vote but not to drive.")
else:
    print("You are not eligible to vote and drive.")

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
