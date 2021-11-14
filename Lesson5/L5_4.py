src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [x for idx, x in enumerate(src) if idx > 0 and src[idx-1] < x]

print(result)
