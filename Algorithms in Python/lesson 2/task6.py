# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться,
# больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести правильный ответ.

from random import randint

min_i = 0
max_i = 100
rnd_n = randint(min_i, max_i)
otvet = -1
ch = 10

while otvet != rnd_n and ch > 0:
    ch -= 1
    otvet = int(input(f'Введите число c {min_i} по {max_i} включительно: '))

    if otvet > rnd_n:
        print('Введеное число больше')
    elif otvet < rnd_n:
        print('Введеное число меньше')

if otvet == rnd_n:
    print('Вы отгадали')
else:
    print('Вы не отгадали')