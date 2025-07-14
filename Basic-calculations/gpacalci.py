print("Enter your marks : \n")
marks = []
for i in range(0,5):
    mark = int(input("Enter marks of subject {} : ".format(i+1)))
    marks.append(mark)
print(f"your highest marks are {max(marks)}")
print(f"your lowest marks are : {min(marks)}")
print(f"your average is : {sum(marks)/len(marks)}")