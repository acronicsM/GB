
def iterator_without_yield(n):
    return (x for x in range(1, n, 2) if x**2 < 200)


gen = iterator_without_yield(100)
while True:
    print(next(gen))
