d = {}
n = int(input('enter number of students: '))
total = 0
highest = 0
for i in range(n):
    name = input(f"name of student {i+1}: ")
    marks = int(input('marks of him/her: '))
    d[name]=marks
    total+=marks
    if d[name]>highest:
        highest = marks
        topper = name
    if marks>90:
        d[f'{name}_grade']="A+"
    elif marks>80:
        d[f'{name}_grade']="A"
    elif marks>70:
        d[f'{name}_grade']="B"
    elif marks>55:
        d[f'{name}_grade']="c"
    elif marks>40:
        d[f'{name}_grade']="D"  
    else:
        d[f'{name}_grade']="F"  
print('average marks of class is: ', total/n)
print(f'highest scorer is {topper} with {d[topper]} marks')
print('here is the list of students, marks and their grade:')
print(d)