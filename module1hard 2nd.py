grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = ['Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron']
# Сортировка списка студенов
students=sorted(list(students))
print(students)
Itog = {'':0}
for i in range(len(students)):
    z = sum(grades[i])/len(grades[i])
    if i == 0:
            Itog= {students[i]:z}
    else:
            Itog.update({students[i]:z})
print(Itog)