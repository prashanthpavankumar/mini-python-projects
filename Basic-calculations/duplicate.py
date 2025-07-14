print("Enter the number of elements in the list:")
a = []
n = int(input())
for i in range(0, n):
    num = int(input(f"Enter element {i+1}: "))
    a.append(num)
duplicate = set()
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i]==a[j]:
         duplicate.add(a[i])   
print("The duplicate elements in the list are:", duplicate)