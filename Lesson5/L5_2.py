
def iterator_without_yield(n):
    y = 0
    for x in range(1, n, 2):
        if x ** 2 < 200:
            yield x, y+x
            y += x


gen = iterator_without_yield(100)
while True:
    print(next(gen))
