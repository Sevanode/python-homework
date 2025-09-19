#a.
abc = [(a, b, c) for a in range(1, 101) for b in range(1, 101) for c in range(1, 101) if a**2 + b**2 == c**2]
#b.
numstrings=['one', 'seven', 'three', 'two', 'ten']
caps = [(len(num),num.upper()) for num in numstrings if len(num)>3]
print(caps)

#c.
names = ["Jules Verne", "Alexandre Dumas", "Maurice Druon"]
namesreversed = [' '.join(name.split()[::-1]) for name in names]


#d.

def concatenate(separator,*strings):
      return  str(separator).join(strings)


print(concatenate(": ", "one", "two", "three"))