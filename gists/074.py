# Function for printing name and surname
def print_full_name(name, surname):
  print(f"{name} {surname}")
  
# Calling a function without specifying parameter names
print_full_name("Jon", "Snow")

# Function call with names of all parameters
print_full_name(name="Jon", surname="Snow")

# Calling the function with the names of the last parameter
print_full_name("Jon", surname="Snow")
