import matplotlib.pyplot as plt
from random import randint

#original article https://www.geeksforgeeks.org/barnsley-fern-in-python/
#I made lists of a,b,c,d,e,f to make it easier to modify fenr

a = [0,0.85,0.2,-0.15]
b = [0,0.04,-0.26,0.28]
c = [0,-0.04,0.23,0.26]
d = [0.16,0.85,0.22,0.24]
e = [0,0,0,0]
f = [0,1.6,1.6,0.44]
p = [0.1,0.85,0.7,0.7]

a = [0,0.85,0.2,-0.15]

j = 0
x = [0]
y = [0]

def x_n_plus_1_calculation(x, y, j, x_n_plus_1=0):
    x_n_plus_1 = a[j] * x[-1] + b[j] * y[-1] + e[j]
    return x_n_plus_1

def y_n_plus_1_calculation(x, y, j, y_n_plus_1=0):
    y_n_plus_1 = c[j] * x[-1] + d[j] * y[-1] + f[j]
    return y_n_plus_1

for point_number in range(100000):
    z = randint(1,100)

    if z == 1:
        j = 0
    elif z >= 2 and z <= 86:
        j = 1
    elif z >=87 and z <= 93:
        j = 2
    elif z >=94 and z <= 100:
        j = 3
    x.append(x_n_plus_1_calculation(x,y,j))
    y.append(y_n_plus_1_calculation(x,y,j))

#plt.scatter(x,y, s = 0.05, cmap = 'black')

color = [i**0.3 for i in y]

plt.scatter(x,y, s = 0.05, c = color)
plt.show()
