# типы данных и переменная
# int, float, boolean, str, list, None
value = None
print(type(value))
a = 123
b = 1.23
print(type(a))
print(type(b))
value = 12334
print(type(value))

s = 'qwerty time'
print(s)
print(a, ' - ' ,b, ' - ',s)
print('{1} - {2} - {0}'.format(a, b, s)) # способы интерпритации 
print(f'{a} - {b} - {s}')

f = False
print(f)
list = ['1', '4', 323, 4, 'hey', True]
col = [323, 4, 'hey', True]
print(list)
print(col)

print('Введите a')
a = int(input())
print('Введите b')
b = int(input())
print(a, '+' , b, '=', a+b)

a = 1.3
b = 4
c= round(a * b)
print(c)

a = 3
a += 5
print(a)

# Логические операции 
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# Кое-что еще: is, is not, in, not in

func = 1
T = 4
x = 123
print(func<T>(x))

#if-else
a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print (a)
else:
    print (b)

#while
original = 66
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)

#For
for i in 'qwerty':
    print(i)

#Строки
text = 'съешь ещё этих мягких французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('ещё','ЕЩЁ')) #
for c in text:
 print(c)

text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...

# Списки
numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]
for i in numbers:
 i *= 2
 print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]

colors = ['red', 'green', 'blue']
for e in colors:
 print(e) # red green blue
for e in colors:
 print(e*2) # redred greengreen blueblue
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # удалить элемент

# Функции 
def f(x):
 if x == 1:
    return 'Целое'
 elif x == 2.3:
    return 23
 else:
    return

arg = 1
print(f(arg))