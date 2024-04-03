'''
Ques uses Queue concept
'''



def countStudents(students, sandwiches):
    unable_to_eat = 0
    while students:
        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
            unable_to_eat = 0
        else:
            students.append(students.pop(0))
            unable_to_eat += 1
        
        if unable_to_eat == len(students):
            break

    return unable_to_eat


input_line = input()
input_list = list(map(int, input_line.split()))

n = len(input_list) // 2
students = input_list[:n]
sandwiches = input_list[n:]


print(countStudents(students, sandwiches))