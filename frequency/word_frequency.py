a = input("Enter a string: ")
a = a.lower()
word=a.split()
a =a.replace(",","")
word_count = {}
for i in word:
    if i in word_count:
        word_count[i]+=1
    else:
        word_count[i]=1
for i in word_count:
    print(f"{i} occurs {word_count[i]} times")
    