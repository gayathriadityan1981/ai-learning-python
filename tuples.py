# ✅ Creating and Accessing Tuples
colors = ("red", "green", "blue")

print(colors[0])        # 'red'
print(colors[-1])       # 'blue'
print(colors[1:3])      # ('green', 'blue')


# ✅ Tuple Methods
t = (1, 2, 3, 1, 5)

print(t.count(2))     # 1
print(t.count(1))     # 2
print(t.index(3))     # 4


# ✅ Tuple Concatenation and Repetition
a = (1, 2)
b = (3, 4)

print(a + b)     # (1, 2, 3, 4)
print(a * 2)     # (1, 2, 1, 2)


# ✅ Tuple Packing & Unpacking
student = ("Vikash", 22)
name, age = student
print(f"Name: {name}, Age: {age}")

employee = ("Gayathri","Bangalore")
name,city = employee
print(f"{name} is located in {city} ")

# 🆚 List vs Tuple (Why Immutability Matters)

# ❌ Using a List (can be changed accidentally)
config = ["localhost", 8080]
config[1] = 9090  # Oops! Changed the port

# ✅ Using a Tuple (safe)
config = ("localhost", 8080)
# config[1] = 9090  ❌ Error: 'tuple' object does not support item assignment

print(config)