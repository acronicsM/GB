# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

RES_MIN = 2
RES_MAX = 9
MIN = 2
MAX = 99
res = {i: 0 for i in range(RES_MIN, RES_MAX + 1)}  # +1 что бы было включая

for i in range(MIN, MAX + 1):
    for key, d_i in res.items():
        if i % key == 0:
            res[key] += 1

print(res)
