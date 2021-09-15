class Animal:
  def __init__(self, name="Rex", age=2):
    self.name = name
    self.age = age

my_cat = Animal("Kitty", 5)
my_parrot = Animal("Ara")  # age set to 2 by default
my_turtle = Animal()  # Set default values for name and age
