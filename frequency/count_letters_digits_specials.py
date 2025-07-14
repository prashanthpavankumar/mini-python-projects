a = input("Enter a string:")
a = a.lower()
a = a.replace(",", "").replace(".", "").replace("!", "").replace("?", "")
count = {'letters': 0, 'digits': 0, 'specials': 0}
for char in a:
    if char.isalpha():
        count['letters']+=1
    elif char.isdigit():
        count['digits']+=1
    else:
        count['specials']+=1
print(f"Letters: {count['letters']}, Digits: {count['digits']}, Specials: {count['specials']}")
