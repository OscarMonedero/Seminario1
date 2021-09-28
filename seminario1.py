import sys

def primos():
    p = 2
    while True:
        if es_primo(p):
            yield p
        p += 1

def es_primo(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def take(n, it):
    for i in range(n):
        yield next(it)

def squares1():
    n = 1
    while True:
        yield n*n +1
        n += 1

def almost_square():
    p = primos()
    s = squares1()
    p1 = next(p)
    s1 = next(s)

    while True:
        if p1 == s1:
            yield p1
            p1 = next(p)
            s1 = next(s)
        elif p1 < s1:
            p1 = next(p)
        else:
            s1 = next(s)

def read_data(n):
    lines = n.readlines()
    return [int(line) for line in lines]

def process(n):
    return take(n[0], almost_square())

def show_results(l):
    for n in l:
        print (n)

if __name__ == "__main__":
    n = read_data(sys.stdin)
    l = process(n)
    show_results(l)