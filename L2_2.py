# 2. Дан список строк.

spis = ['dfdf', '7', 'в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', '-7', 'градусов', '9']
str_new = ''
maxlen = len(spis)-1
pred_isdigit = False

for i in range(maxlen, -1, -1):
    elem = spis[i]

    if pred_isdigit:
        spis.insert(i + 1, '"')
        pred_isdigit = False

    if elem.lstrip('-+').isdigit():
        spis.insert(i+1, '"')
        pred_isdigit = True

maxlen = len(spis)-1
for i, elem in enumerate(spis):
    if elem.lstrip('-+').isdigit():
        str_new = str_new + elem
    elif i < maxlen and elem == '"' and spis[i+1].lstrip('-+').isdigit():
        str_new = str_new + elem
    else:
        str_new = str_new + elem + ' '

str_new = str_new.strip()

print(spis)
print(str_new)
