# Create and print dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Change value based on key
thisdict["year"] = 2018

# Update value
thisdict.update({"year": 2020})

# Add value (create new key and value)
thisdict["color"] = "red"

# Removing item with specified key name
thisdict.pop("model")

# Removing item with specified key name, also possible to remove whole dict!
del thisdict["model"]

# Make dictionary empty
thisdict.clear()
