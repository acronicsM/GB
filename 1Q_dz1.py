# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах.
print('\nЗадание №1 ' + '<<'*20+'\n')

duration = 86400*10 + 60*60*10 + 72*60 + 5

day = duration//86400
hour = duration%86400//3600
minute = duration%86400%3600//60
sek = duration%86400%3600%60

print(f'{day} дн {hour} час {minute} мин {sek} сек.')

#2. Для кубов нечётных чисел от 1 до 1000. Вычислить сумму чисел, сумма цифр кубов которых делится нацело на 7.
print('\nЗадание №2 ' + '<<'*20+'\n')

number = 0
cumul = 0
while number < 1000:
    number +=1

    if number%2 == 0:
        continue

    cube = number**3

    sum = 0
    delet = 1
    while cube != cube % delet:
        # sum_number = cube % delet // (delet / 10)
        delet *= 10
        sum += cube % delet // (delet / 10)

    if sum%7 == 0:
        cumul += number
        print(f'{number}^3: {cube}; sum:{cumul} [ {sum} ]')

# 3. Реализовать склонение слова «процент» для чисел до 234. Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента». Вывести все склонения для проверки.

print('\nЗадание №3 ' + '<<'*20+'\n')

i = 0
percent = 'процент'
while i <= 234:
    if i == 1:
        print(str(i) + ' ' + percent)
    elif i < 5 and i > 0:
        print(str(i) + ' ' + percent + 'а')
    else:
        print(str(i) + ' ' + percent + 'ов')
    i +=1