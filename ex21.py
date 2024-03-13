def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(20, 6)
height = subtract(78, 10)
weight = multiply(92.5, 2)
iq = divide(100, 10)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# a puzzle for the extra credit, type it anyway
print("Here is a puzzle")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")