#2.i

print("Перша константа", False)
print("Друга константа", True)
print("Третя константа", None)

#2.ii

print(pow(7,6))
print(abs(-76))
print("---------")

#2.iii

words=["blue","red","yellow", "orange"]
for word in words:
    print(word)

for number in range(10):
    if number % 3 == 0:
        print(number)

print("  ")

a = 3
while a < 20:
	print(a)
	a= a + 5

print("   ")

#2.iv


numberone = 0
numbertwo=20
try:
    print("Поділимо 20 на 0",numbertwo/numberone)
except ZeroDivisionError:
    print("Помилка")
finally:
    print("На нуль не можна")

 # 2.v
    # Робота контекст-менеджера with. Код з ним:

    with open("README.md", "r") as test:
        for str in test:
            print(str)

#2.vi
#Робота з Python lambdas

x=lambda a,b : a/b
print(x(30,15))

