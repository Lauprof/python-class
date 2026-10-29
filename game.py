#game to check even or odd numbers. The game will prompt the user to enter a number, and then it will determine if the number is even or odd. If the user enters a non-integer value, the game will handle the error gracefully and prompt the user to enter a valid integer.



print(" ==" * 20)


print("Welcome to the Even or Odd Number Game!")

print(" ==" * 20)

while True:
    user_input = input("Please enter an integer (or type 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        print("Thank you for playing! Goodbye!")
        break
    
    try:
        number = int(user_input)
        
        if number % 2 == 0:
            print(f"The number {number} is even.\n")
            
        else:
            print(f"The number {number} is odd. ")
    
    except ValueError:
        print("That's not a valid integer. Please try again.")