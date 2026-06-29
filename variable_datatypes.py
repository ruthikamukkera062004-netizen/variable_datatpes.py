# Variables and Data Types in Python

# Integer
age = 21

# Float
height = 5.4

# String
name = "Ruthika"

# Boolean
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

# Reassign variables
age = 22
height = 5.5

print("\nUpdated Values")
print("Age:", age)
print("Height:", height)

# Arithmetic Operations
a = 10
b = 5

print("\nArithmetic Operations")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Memory Address using id()
x = 100
y = 100

print("\nMemory Address")
print("id(x):", id(x))
print("id(y):", id(y))

# Variable Scope
message = "Outside Block"

if True:
    inside = "Inside Block"
    print("\nInside Block:", inside)

print("Outside Block:", message)