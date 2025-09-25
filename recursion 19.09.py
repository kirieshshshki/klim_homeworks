#Factorial f(n) = n*f(n-1)
#f(1) = 1
def fact(x):
    if x == 1:
        return 1
    return x * fact(x-1)
#или вариант через цикл (любую рекурсию можно чнаписать через цикл)
def fact_it(x):
    res = 1
    for i in range(2, x+1):
        res *= i
    return res

print("function fact(5):", fact(5))
print("function fact_it(5):", fact_it(5))

#Fibonacci
# f(n) = f(n-1) + f(n-2)
# f(0) = 0, f(1) = 1

import time
t = time.time()     #выдает время с какой-то древней точкой отсчета

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print("function fib(10):",fib(10))
t = time.time() - t   #нам нужен промежуток времени, то есть разность времен начального и конечного
print("time of fibonacci recursion:", t)

#рекурсия вызывает себя дважды, в итоге для N-ного количества чисел фибоначчи вызовов 2**n, а это чета как-то много
#поэтому нужен рекурсивный алгоритм, запоминающий, что он уже вызывал по значениям

#cache - массив посчитанных данных, состоящий первоначально из n нулей
#cache = [0] * n
def fib_memo(n, cache):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if cache[n] != 0:     #если элемент не равен нулю, значит он уже посчитан
        return cache[n]
    cache[n] = fib_memo(n-1, cache) + fib_memo(n-2, cache)
    return cache[n]

cache = [0] * 11
print("function fib_mem(10):", fib_memo(10, cache))

#ex4
# f(n) = ccc

def tri(num, symb):   #через цикл
    mas = [symb] * num
    for i in range(num // 2 + 1):
        mas[i-1] = i*symb
        mas[-i] = i*symb
    if num % 2 == 1:
        mas[num//2] = (i + 1)*symb
    return mas

print('\n'.join(map(str, tri(7, "c"))))

def tri_rec(x, symb):      #клим должен прислать


