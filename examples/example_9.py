world = "World"
print("Hello" + " " + world)

print("Hello {}".format(world))

# Format string with str.format() function
title = "General"
name = "Kenobi"
age = 100
print("Hello there, {} {}, age is {}".format(title, name, age))

# Format using variable names
title = "General"
name = "Kenobi"
age = 100
print("Hello there, {name} {title}, age is {age}".format(name=name, title=title, age=age))

# Format using variable order
title = "General"
name = "Kenobi"
age = 45
print("Hello there, {0} {0}, age is {0}".format(title, name, age))

# Format using the f-string approach
title = "General"
name = "Kenobi"
age = 666
print(f"Hello there, {title} {name} age is {age}")
