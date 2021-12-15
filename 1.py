from random import shuffle
import math


def bubble(sp, sr, per):
    for i in range(len(sp)-1):
        for j in range(len(sp)-i-1):
            sr+=1
            if sp[j] > sp[j+1]:
                sp[j], sp[j+1] = sp[j+1], sp[j]
                per+=1
    print (sr, per)
    return sp


def vstavki(s, sr, per):
   for i in range(1, len(s)):
       n = s[i]
       m = i - 1
       sr += 1
       while (m >= 0 and n < s[m]):
           per += 1
           sr += 1
           s[m + 1] = s[m]
           m -= 1
       s[m + 1] = n
   print (sr, per)
   return s


def vibor(sp, sr, per):
   for i in range(len(sp) - 1):
       L = i
       for j in range(i + 1, len(sp)):
           sr += 1
           if sp[j] < sp[L]:
               L = j
               per += 1
       sp[i], sp[L] = sp[L], sp[i]
   print (sr, per)
   return sp


def shell(s, sr, per):
    n = len(s)
    k = int(math.log2(n))
    r = 2**k -1
    while r > 0:
        for i in range(r, n):
            t= s[i]
            j = i
            sr+=1
            while (j >= r) and (s[j - r] > t):
                s[j] = s[j - r]
                j -= r
                per+=1
                sr+=1
            s[j] = t  
        k -= 1
        r = 2**k -1
    print (sr, per)
    return s


def part(a, men, bol):
    global sr
    global per
    p = a[(men + bol) // 2]
    i = men - 1
    j = bol + 1
    while True:
        i += 1
        while a[i] < p:
            sr+=1
            i += 1
        j -= 1
        while a[j] > p:
            sr+=1
            j -= 1
        sr+=1
        if i >= j:
            per+=1
            return j
        a[i], a[j] = a[j], a[i]

def quick_sort(it, men, bol):
    if (men < bol):
        spl = part(it, men, bol)
        quick_sort(it, men, spl)
        quick_sort(it, spl + 1, bol)

def Q_sort(a): 
    quick_sort(a, 0, len(a) - 1)


n = int(input('Количество элементов списка - 10/100/1000  '))
a = [i for i in range(n, 0, -1)]
r=tuple(a)

print ('Не отсортированный список')

print ('Метод пузырька')
bubble(a, 0, 0)

a=list(r)
print ('Метод выбора')
vibor(a, 0, 0)

a=list(r)
print ('Метод вставок')
vstavki(a, 0, 0)

a=list(r)
print ('Метод Шелла')
shell(a, 0, 0)

a=list(r)
sr, per = 0, 0
print ('Q_Sort')
print(Q_sort(a), sr, per)


b = [i+1  for i in range(n)]
b1 = []
for j in range(n//2):
    b1.append(b[j])
shuffle(b1)
for j in range(n//2):
    b[j]=b1[j]

r=tuple(b)
print ('Частично отсортированный список')

print ('Метод пузырька')
bubble(b, 0, 0)

b=list(r)
print ('Метод выбора')
vibor(b, 0, 0)

b=list(r)
print ('Метод вставок')
vstavki(b, 0, 0)

b=list(r)
print ('Метод Шелла')
shell(b, 0, 0)

b=list(r)
sr, per = 0, 0
print ('Q_Sort')
print(Q_sort(b), sr, per)


c = [i+1 for i in range(n)] 
print ('Полностью отсортированный список')

print ('Метод пузырькa')
bubble(c, 0, 0)

print ('Метод выборa')
vibor(c, 0, 0)

print ('Метод вставок')
vstavki(c, 0,0)

print ('Метод Шелла')
shell(c, 0, 0)

sr, per = 0, 0
print ('Q_Sort')
print(Q_sort(c), sr, per)
