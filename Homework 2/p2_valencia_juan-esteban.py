# a. Find all Pythagorean triples (a, b, c) where 1 <= a, b, c <= 100
abc = [(a, b, c) for a in range(1, 101) for b in range(1, 101) for c in range(1, 101) if a**2 + b**2 == c**2]

# b. Create a list of tuples (length, uppercase string) for strings longer than 3 characters
numstrings = ['one', 'seven', 'three', 'two', 'ten']
caps = [(len(num), num.upper()) for num in numstrings if len(num) > 3]
print(caps)

# c. Reverse first and last names in a list
names = ["Jules Verne", "Alexandre Dumas", "Maurice Druon"]
names_reversed = [' '.join(name.split()[::-1]) for name in names]

print(names)
print(names_reversed)

# d. Concatenate strings with a separator
def concatenate(separator, *strings): return str(separator).join(strings)

print(concatenate(": ", "one", "two", "three"))
