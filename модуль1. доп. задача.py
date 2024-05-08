grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
a = students[0]
list_1 = grades[0]
mark_1 = sum(list_1)/len(list_1)
b = students[1]
list_2 = grades[1]
mark_2 = sum(list_2)/len(list_2)
j = students[2]
list_3 = grades[2]
mark_3 = sum(list_3)/len(list_3)
k = students[3]
list_4 = grades[3]
mark_4 = sum(list_4)/len(list_4)
s = students[4]
list_5 = grades[4]
mark_5 = sum(list_5)/len(list_5)
results = {a: mark_1, b: mark_2, j: mark_3, k: mark_4, s: mark_5}
print(results)

