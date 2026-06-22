Avg=0
El = 0
NEL = 0

for i in range(1, 11):
    attendance = int(input("Enter the attendance for student {}: ".format(i)))
    if attendance >= 75:
        El = El + 1
    else:
        NEL = NEL + 1   

print("Number of eligible students: ", El)
print("Number of not-eligible students: ", NEL)
Avg = attendance/10
print("Average attendance: ", Avg)