class Animal:    
  NAME = ""  # class variable
  AGE = 0  # class variable
  
  def __init__(self):
    self.name = "John"  # set the default value for the name field of the Animal class object        
    self.age = 2   
    
  def print_details(self):  # method for printing the state of an object
    print(f"Name: {self.name}, age: {self.age}.")
