# If example

x = 0
y = 3
if x > y:  # This will be translated to False because 0 is not greater than 3
  print(f"{x} is greater than {y}")  # Will not be displayed
  
if x < y:  # This will be translated to True because 3 is greater than 0
  print(f"{x} is less than {y}")  # Will be displayed
