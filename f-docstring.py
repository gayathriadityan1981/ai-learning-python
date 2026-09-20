# fstring basics
name = "Gayathri"
age = 28
print(f"My name is {name} and I am {age} years old.")


# fstring with expression
a = 7
b = 3
print(f"{a} x {b} = {a * b}")
print(f"{a} + {b} = {a + b}")
# fstring with formatting
price = 49.5678
print(f"Price: ₹{price:.2f}")  # ₹49.57

price1 = 12.345
print(f"Price 1 val:{price1:.2f}")
# Function with docstring
def square(n):
    """Returns the square of a number."""
    return n * n

print(square(4))           # 16
print(square.__doc__)      # Shows docstring


# using help with docstring
def greet(name):
    """Greets the person with the provided name."""
    print(f"Hello, {name}!")

help(greet)
