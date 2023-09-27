import math
from math import cos

a = float(input("Введите a= "))
z = cos(a) + cos(2*a) + cos(6*a) + cos(7*a)
y = (4*cos(a/2))*(cos((5/2)*a))*cos(4*a)

print('z1 =', z)
print('z2 =', y)
