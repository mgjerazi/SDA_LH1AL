class Animal:
  def __init__(self, name="Rex", age=2):
    self.__name = name        
    self.__age = age
    
my_dog = Animal()
print(my_dog.__name)  # Python will throw an error !!!
