#loop executes a block of code repeatedly as long as a specified condition is true. There are two main types of loops in Python: for loops and while loops.

students = ["Alice", "Bob", "Charlie", "David"]

print(students)
for student in students:
    print(f"Hello, {student}!") 
#loop through a string
for y in "Javascript":
    print(y)

#loop through a range of numbers range(start, stop, step) is a built-in function that generates a sequence of numbers. It can take one, two, or three arguments:
for i in range(5):
    print(i)  # This will print numbers from 0 to 4  
print("Now printing numbers using range with start and stop:")
for m in range(1, 6):
    print(m) 

print("Now printing numbers using range with step:")
for n in range(0, 10, 2):
    print(n)  # This will print even numbers from 0 to 8

print("using break statement in a loop:")
#break statement is used to exit a loop prematurely when a certain condition is met. When the break statement is executed, the loop terminates immediately, and the program continues with the next statement after the loop.

for i in range(10):
    if i == 5:
        break  # Exit the loop when i is equal to 5 
    print(i)  # This will print numbers from 0 to 4, but stop before printing 5     

print("using continue statement in a loop:")
#continue statement is used to skip the rest of the code inside a loop for the current iteration and move to the next iteration.

for i in range(10):
    if i == 5:
        continue  # Skip the rest of the code when i is equal to 5
    print(i)  # This will print numbers from 0 to 9, but skip printing 5