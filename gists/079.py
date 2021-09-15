# Add any number of ingredients
def add_ingredients(**kwargs):    
  result = 0
  for key in kwargs:
    result += kwargs[key]
  return result

print(add_ingredients(eggs=3, spam=5, cheese=2)) # Will print 100
