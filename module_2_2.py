
first = int(input("Введите ваше число: "))
second = int(input("Введите ваше число: "))
third = int(input("Введите ваше число: "))
if first == second == third:
    print("3")
elif first == second or second == third or first == third:
    print("2")
else:
    print("0")