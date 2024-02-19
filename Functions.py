#Defining a Function: 
#You can define a function in Python using the def keyword
#followed by the function name and parentheses containing 
#any parameters the function takes.
#The function body is indented below the function definition.
def Write():
    print()

# Calling the function
Write()

#Function Parameters:
#You can pass values, known as arguments or parameters, into a function to customize its behavior.
def greet(name):
    print("Hello, " + name + "!")

# Calling the function with an argument
greet("Tommy")

#Default Parameters:
#You can provide default values for function parameters,
#which are used when the function is called without providing a value for those parameters.
def greet(name="World"):
    print("Hello, " + name + "!")

# Calling the function without providing a value for 'name'
greet()

# 1 Experimento 
def Crouch(Ctrl="Sneaking"):
    print("You're " + Ctrl + ".")

Crouch()



#Return Values:
#Functions can also return values using the return statement. 
#You can use this value in the rest of your code.
def add(a, b):
    return a + b

result = add(3, 5)
print("The sum is:", result)

# 2 Experimento
WallDistance = 2

NoWall = True
if WallDistance > 1 :

    def Status(Ctrl, W, A, S, D,):
        return Ctrl + W
if NoWall and Status("Ctrl", "W", "A", "S", "D") == "CtrlW":
    print("Laying Prone")
else: print("Taking Cover")

def Status(Ctrl, W, A, S, D,):
    return Ctrl + S
if Status("Ctrl", "W", "A", "S", "D") == "CtrlS":



# 2.1 "Interação com Objeto"
    WallDistance = 1

Wallnearby = True
if WallDistance <= 1 : 
    print("Take Cover")
else :
    print("There's no wall nearby.") 
    

def Status(Ctrl, W, A, S, D,):
    return Ctrl + W
if Wallnearby and Status("Ctrl", "W", "A", "S", "D") == "CtrlW":
    print("Taking cover")
else : print("Laying Prone")