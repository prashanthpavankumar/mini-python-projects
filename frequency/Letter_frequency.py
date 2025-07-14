a = input("Enter a string: ")
a = a.lower()
frequency = {}
for char in a:
    if char.isalpha():
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
for char in sorted(frequency.keys()):
    print(f"{char}occurs: {frequency[char]}")