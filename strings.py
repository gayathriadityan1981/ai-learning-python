# String Indexing and Slicing

text = "Programming"

print(text[0])
print(text[-1])
print(text[3:8])
print(text[::-1])

# String Operations

a = "Hello"
b = "World"

print(a + " " + b)       # Concatenation
print(a * 3)             # Repetition
print("o" in a)          # Membership
print("h" in a)          # Membership
print(len(b))            # Length

# String Methods

message = "  Learn Python!  "

print(message.lower())       # '  learn python!  '
print(message.strip())       # 'Learn Python!'
print(message.replace("Python", "Coding"))  # '  Learn Coding!  '
print(message.find("n"))     # Index of first 'n'
print(message.count("n"))    # Count of 'n'
print(message.startswith(" "))  # True
print(message.startswith("A "))  # False
print(message.endswith("!  "))  # True
print(message.endswith("1"))  # True

# Split and Join

csv_data = "apple,banana,cherry"
fruits = csv_data.split(",")     # ['apple', 'banana', 'cherry']
print(fruits)
sentence = "|".join(fruits)      # 'apple banana cherry'
print(sentence)

# 🆚 Before Slicing vs After Slicing

# ❌ Without slicing (manual character access):
word = "Python"
# print first 3 letters
print(word[0] + word[1] + word[2])  # 'Pyt'

# ✅ With slicing:
print(word[:3])  # 'Pyt'
print(word[:5])

# 1. String slicing and reverse
text = "machinelearning"
print("First 5 characters:", text[:5])
print("Last 3 characters:", text[-3:])
print("String in reverse:", text[::-1])

# 2. Full name operations
full_name = input("Enter your full name: ")
print("Uppercase:", full_name.upper())

# Extract first name (before first space)
first_space_index = full_name.find(" ")
if first_space_index != -1:
    first_name = full_name[:first_space_index]
else:
    first_name = full_name  # If no space is found
print("First name:", first_name)

# Count 'a' occurrences
print("Number of 'a's:", full_name.lower().count('a'))

# 3. Sentence word split
sentence = input("Enter a sentence: ")
print("Words in sentence:")
for word in sentence.split():
    print(word)

# 4. Replace spaces with dashes
print("With dashes:", sentence.replace(" ", "-"))

# 5. Challenge - Check Python file extension
filename = input("Enter a filename: ")
if filename.endswith(".py"):
    print("Python file detected")
else:
    print("Not a Python file")