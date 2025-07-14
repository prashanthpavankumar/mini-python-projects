num = input("Enter a series ofnumber: ")
digit_count = {}
for digit in num:
    if digit in digit_count:
       digit_count[digit] += 1
    else:
        digit_count[digit] = 1
for digit in sorted(digit_count.keys()):
    print(f"{digit} occurs {digit_count[digit]} times in the series")
    

