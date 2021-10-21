import numpy as np
a = np.random.randint(10, 50, size=(12, 10))
print(a)
x = int(input('Nhap so nguyen trong khoang (0-100): '))
bang = 0
lonhon = 0
nhohon = 0
n=12
m=10
for i in range(0, n):
    for j in range(0, m):
        if (a[i][j] == x):
            bang += 1
        elif (a[i][j] > x):
            lonhon += 1
        else:
            nhohon += 1
print('Số phần tử có giá trị bằng x trong ma trận: ', bang)
print('Số phần tử nhỏ hơn giá trị x trong ma trận: ', nhohon)
print('Số phần tử lớn hơn giá trị x trong ma trận: ', lonhon)