# Trim spaces
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

# Remove the leading and trailing characters:
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)
