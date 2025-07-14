a = []
n = int(input("Enter the number of elements in the list: "))
for i in range(0,n):
    num = int(input(f"Enter element {i+1}: "))
    a.append(num)
a.remove(max(a))
second_max = a[0]
for i in a:
    if i > second_max:
        second_max = i
print(f"The second largest element in the list is: {second_max}")

