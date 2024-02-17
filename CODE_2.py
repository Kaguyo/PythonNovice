# We'll cover conditional statements (if, elif, else) and loops (for and while loops).
# 1. Conditional Statements:
    #Conditional statements allow you to execute different blocks of code based on certain conditions.
#1.1 'if' Statement:
     #The 'if' statement checks a condition, and if it's true, executes a block of code.

x = 20
if x > 5: 
     print("x eh maior do que 5")

#1.2 'if-else' Statement:
#The 'if-else' statement executes one block of code if the condition is true, and another block if it's false.
x = 19
   
if x > 5:
     print("x eh maior do que 5")
else:
     print("x é menor ou igual a 5")

#1.3 'if-elif-else' Statement:
#The 'if-elif-else' statement allows you to check multiple conditions.
x = 10
   
if x > 10:
    print("x is greater than 10")
elif x < 10:
    print("x is less than 10")
else:
    print("x is equal to 10") 

#2. Loops:
#Loops are used to iterate over a sequence (like a list) or execute a block of code repeatedly.

#2.1 'for' Loop:
#The 'for' loop is used to iterate over a sequence (e.g., list, tuple, string) or other iterable objects.
fruits = ["maca", "banana", "abacaxi"]

#2.2 'while' Loop:
#The 'while' loop executes a block of code as long as a condition is true.
i = 1
while i <= 5:
    print(i)
    i += 1

#3. Loop Control Statements:
#Python provides loop control statements like 'break', 'continue', and 'pass' to control the flow of loops.
    
    # Break statement
fruits = ["apple", "banana", "pineapple"]
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break

# Continue statement
for i in range(2, 6):
    if i == 3:
        continue
    print(i)

# Pass statement (used as a placeholder). Empty Code Blocks:
#it's often used in situations where a code block is syntactically necessary 
#but you don't want to perform any action inside it.
for i in range(5):    
    pass

# Other example: 
# 'if' "condition":
    pass  # Placeholder for future code