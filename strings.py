
# Strings in Python

my_str = "Hello Python"
print(my_str)

# String length
print(len(my_str))

# Uppercase and lowercase
print(my_str.upper())
print(my_str.lower())

# Access characters
print(my_str[0])
print(my_str[-1])

# String slicing
print(my_str[0:5])

# String concatenation
first_name = "Hello"
second_name = "World"
print(first_name + " " + second_name)

# String formatting
name = "Chaitanya"
age = 25
print(f"My name is {name} and my age is {age}")

# Replace a string
print(my_str.replace("Python", "World"))

# Check substring
print("Python" in my_str)

# Remove extra spaces
sample = "  Python  "
print(sample.strip())