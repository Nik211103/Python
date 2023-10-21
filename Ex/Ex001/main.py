#коментарий
"""
co
me
nts 

a = 5 #int
b = 5.89 #float
c = 'helo' #str
print(f"{a} - {b} - {c}")

list_1 = []
list_1 = list()
list_1 = [1, 2, 3, 8]
print(list_1[-2])#вызов попорядку с конца 
print (*list_1)#без скобочек 
for i in list_1:
    print(i)#цикл


    print(len(list_1))#длина 


list_1.append(10)#добаление в список
print(list_1)

list_1 = []
for i in range(5):
    list_1.append(i)#создание списка
    print(list_1)

list_1 = [12, 7, -1, 21, 0]
print(list_1.pop()) #0 последнее
print(list_1)
print(list_1.pop()) #21
print(list_1)
print(list_1.pop(0)) #12 по индексу можно выбрать
print(list_1)
print(list_1.insert(2, 11))# 2 индекс 11 число
print(list_1)
print(list_1.insert(0, 10))
print(list_1)
print(list_1[0 : 2])#от и до по индексу
print(list_1[::3])#начала и 3 элемент


t = ()#кортеж
print(type(t))

t = (1, )
v = [1, 8 , 9]
print(v)
print(type(v))

v = tuple(v)
print(v)
print(type(v))

#a, b = 1, 2
#a = b = 1
a, b, c, = v

d = {}#словарь
d = dict()
d['q'] = 'qwerty'
print(d['q'])

colors = {'red' , 'green', 'blue'}#множества
print(colors)
colors.add('gray')
print(colors)
colors.remove('red')
print(colors)
colors.discard('red')#проверка
q = set()#добавление
"""
a = {1, 8, 6}

b= frozenset(a)#заморозка

print(b)