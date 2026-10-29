#while loop used to execute a block of code repeatedly as long as a specified condition is true
x = 0
while x <= 5:
    print(x)
    x += 1  # Increment x by 1 to avoid an infinite loop
y = 6

while y <= 16:
     if y == 12:
         break  # Exit the loop when y is equal to 5    
     print(y)  # This will print numbers from 0 to 4, but stop before printing 5
     y += 1  # Increment y by 1 to avoid an infinite loop