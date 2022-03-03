import sys
from utils import currency_rates_advanced

url_cbr = 'http://www.cbr.ru/scripts/XML_daily.asp'

if len(sys.argv) < 2:
    print('Не указан код валюты')
    print(f'Для получения помощи укажите параметр "help"')
else:
    param1 = sys.argv[1]

    if param1.lower() == 'help':
        print('Передайте в параметре код валюты')
    else:
        if len(sys.argv) > 2:
            print(f'Указанно больше 2 валют, курс будет получен только для первой валюты {sys.argv[1]}')

        course = currency_rates_advanced(url_cbr, param1)

        if course is None:
            print(f'Валюта {param1} не найдена')
        else:
            print(f'{param1}: {course}')
