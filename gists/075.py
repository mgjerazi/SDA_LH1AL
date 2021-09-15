# The definition of the function greet_by_name (name) with the default value of name
def greet_by_name(name="World!"):
  print(f"Hello, {name}")
  
# Calling the function greet_by_name (name) without an argument
greet_by_name()  # Prints "Hello, World!"

# Calling the function greet_by_name (name) with "John" as the name argument
greet_by_name("John")  # Prints 'Hello, John'
greet_by_name(name="John")  # Prints 'Hello, John‘
