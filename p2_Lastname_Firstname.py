
abc = [(a, b, c) for a in range(1, 101) for b in range(1, 101) for c in range(1, 101) if a**2 + b**2 == c**2]
numstrings=['one', 'seven', 'three', 'two', 'ten']
caps = [(len(num),num.upper()) for num in numstrings if len(num)>3]
print(caps)