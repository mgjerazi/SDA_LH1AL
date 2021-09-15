# Add any number of ingredients
def add_ingredients(*args, **kwargs):
  result = 0
  for arg in args:
    result += arg
  for key in kwargs:
    result += kwargs[key]
  return resultprint(add_ingredients(1, 2, 3, eggs=3, spam=5, cheese=2)) # Will print 16
