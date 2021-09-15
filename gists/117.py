class Animal:
  ...
  puppy = Animal()
  dog = Animal()  # Creates a second Animal class object
  puppy.age = 1
  puppy.name = "Rex Junior"
  dog.age = 10
  dog.name = "Rex Senior"
  print(f"My dog: {puppy.name}, {puppy.age} and the older dog: {dog.name}, {dog.age}")
