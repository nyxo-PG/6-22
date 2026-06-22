total_marks = 0
highest_marks = -1
lowest_marks = 101

for i in range(0, 8):
    marks = int(input("Enter your marks: "))
    total_marks = total_marks + marks
    
    if marks > highest_marks:
        highest_marks = marks
    if marks < lowest_marks:
        lowest_marks = marks    

average_marks = total_marks / 8

print("Total marks:", total_marks)
print("Average marks:", average_marks)
print("Highest marks:", highest_marks)
print("Lowest marks:", lowest_marks)