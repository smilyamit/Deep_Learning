'''n = int(input().strip())
a = list(map(int, input().strip().split()))
i = 0
for i in range((10**10+1),(10**10+6),10**10):
    a.append(i)
print(a)'''

'''n = int(input())
a = list(map(int, input().split()))
print(a)'''

'''n = int(input().strip())
ListOfUser = map(int, input().strip().split())
bigsum = 0
for each_element in ListOfUser:
    bigsum = bigsum + int(each_element)
print(bigsum)'''

n=int(input())
a=[]
for i in range(0,n):
    lists=[int(i) for i in input().split()]
    a.append(lists)
    
print(a)

import numpy as np
x = np.array([[2,3,4], [5,6,7]]) 
print(np.reshape(x, (6,-1)))     
print(np.reshape(x, (6,1)))

a = np.arange(24).reshape((2,2,2,3))
print(a)


a = np.arange(10)
print(a)
a = np.arange(1000).reshape((25,2,2,10))
print(a)

a = np.arange(81).reshape((3,3,3,3))
print(a)

a = np.arange(100).reshape((10,10,1))
print(a)


a = np.arange(6).reshape((3, 2), order = 'f')
print(np.reshape(a, (1,6)))

print(a)

a = np.array([[1,2,3], [4,5,6]])
#print(np.reshape(a,6))
print(np.reshape(a, (1,6)))


a = [2,5,9]
a.reverse()
for i in a:
    print(i)


n = int(input())
a = list(map(int, input().split()))


a.reverse()
print(a)



Student_Grades = ['56', '49', '63']
for i in range(len(Student_Grades)):
    Student_Grades[i] = int(Student_Grades[i])
    
print(Student_Grades)


n = int(input())
matrix = []
for i in range(0,n):
    list = [int(i) for i in input().split()]
    matrix.append(list)

print(matrix)

for i in range(3):
    print(i)



















