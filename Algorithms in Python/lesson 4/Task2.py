def sieve_(n):
    size = 1000
    sieve = [i for i in range(size)]
    HOLE = 0
    sieve[1] = HOLE

    for i in range(2, size):
        if sieve[i] != HOLE:
            j = i + i
            while j < size:
                sieve[j] = HOLE
                j += i

    res = [item for item in sieve if item != HOLE]
    return res[n-1]


def prime(n):
    lst = []
    i = 2

    while len(lst) != n:
        if len(lst) == n:
            return i-1

        if (i > 10) and (i % 10 == 5):
            continue

        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break

            if i % j == 0:
                break
        else:
            lst.append(i)

        i += 1

    return i - 1


print(f'{prime(2)} - {sieve_(2)}')
print(f'{prime(4)} - {sieve_(4)}')
print(f'{prime(5)} - {sieve_(5)}')
print(f'{prime(1)} - {sieve_(1)}')
