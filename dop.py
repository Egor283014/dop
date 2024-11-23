grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = sorted( {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})
print(students)
# студенты среднее орифметическое
students_0 =sum(grades[0])/len(grades[0])
students_1 =sum(grades[1])/len(grades[1])
students_2 =sum(grades[2])/len(grades[2])
students_3 =sum(grades[3])/len(grades[3])
students_4=sum(grades[4])/len(grades[4])
print(students[0])
students_list ={students[0]:students_0 , students[1]:students_2 , students[2]:students_2 , students[3]:students_3 , students[4]:students_4}
print(students_list)







