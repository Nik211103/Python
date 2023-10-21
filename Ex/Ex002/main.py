"""print("helo")

n = int(input("Enter number "))
a = 1
b = 0
i = 1
fib = 0
count = 0

while i <= n + 1:
    #print (fib, end=" ")записывает если добавить \n то будет на следющей если записать end = '___'будет разделение
    if fib == n:
        #print(f"\nЧисло {n} по счету на {i} месте")
        break
    fib = a + b
    a = b
    b = fib 
    i += 1
else:
    i = -1

print(i)

n = 'мама мыла раму'
print(n[10])#поиск элемента под номером индекса(с 1)
print(n.find('у'))#поиск буквы 

l = [5, 3, -1, 3]
print(l.count(7))#поиск количества элементов

n = int(input("Введите число дней "))
summ = 0
count = 0
listtemp = [-36, -45, -25, 11, 49, 49]
for t in listtemp:
    #t = random.randint (-50, 50)
    if t > 0:
        count+=1
    else:
        if count > summ:
            summ = count
        count = 0
    print(t, end=' ')
    summ += t
print()
if count > summ:
    summ = count
    print(t, end='')
print(sum)
print(count)
"""
