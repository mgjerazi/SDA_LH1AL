# Declaration and init list variable
alphabet = []
print(f"Actual length of alphabet: {len(alphabet)}")

# Appending few letters to variable
alphabet.append("a")
alphabet.append("b")
alphabet.append("c")
print(f"Alphabet: {alphabet} (length: {len(alphabet)})")

# Indexing
print(f"First alphabet letter is '{alphabet[0]}'.")

# Extend with multiple elements
alphabet.extend(["f", "d", "g", "e"])
print(f"Alphabet (unordered): {alphabet} (length: {len(alphabet)})")

# Sorting - still we working on alphabet variable
alphabet.sort()
print(f"Alphabet (ordered): {alphabet} (length: {len(alphabet)})")

# Ordering - create new list
sorted_alphabet = sorted(alphabet)
print(f"Alphabet (sorted): {sorted_alphabet}, alphabet(unsorted): {alphabet})")
