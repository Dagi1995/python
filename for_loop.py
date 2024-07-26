student_heights = input("Enter the students height...: ").split()
for n in range (0 , len (student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0    
for height in student_heights:
    total_height += height
    
total_number =0    
for student in student_heights:
    total_number +=1

average_number = round(total_height/total_number)
print(total_height)
print(total_number)
print(average_number)