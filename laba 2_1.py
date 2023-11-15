from  math import sqrt

b = float(input("Введите значение b \n"))
z1 = (sqrt(2*b + 2*sqrt(b**2 - 4))/(sqrt(b**2 - 4))+ b + 2)
z2 = 1/sqrt(b+2)
print( "z1 = ", z1 )
print( "z2 = ", z2 )
