from random import randint
n = int(input("Введите количество элементов массива: "))
L = [0]*n				# Оператор 0
for i in range(n):
    L[i] = randint(-10,10)	# Оператор 1
print(L)
S = 0
for i in range(0, n):		# Оператор 2
   if L[i]%3==0:
        S += L[i]			# Оператор 3
print('S = ',S)
