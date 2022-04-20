import re


def email_parse(email_address):
    reg_pattern = r'''
       (?P<adress>              # Начало группы адресс
       ([a-zA-Z0-9\.\_\+\-]+)   # Все латинские буквы со спецсимволами
       )                        # Окончание группы адресс
       \@                       # Символ @ разделяющий адресс и домен
       (?P<domain>              # Начало группы домен
       ([a-zA-Z0-9\.\-]+)       # Все латинские буквы со спецсимволами 
       \.                       # Обязательный символ точка
       [a-zA-Z]+)               # Все латинские буквы
    '''

    data = re.match(reg_pattern, email_address, re.X)

    if data is None:
        raise ValueError(f'wrong email: {email_address}')
    else:
        return data.groupdict()


address1 = 'someone@geekbrains.ru'      # ВЕРНО
address2 = 'someone1@geekbrains.ru'     # ВЕРНО с цифрой в username
address3 = 'someone+-_0@geekbrains.ru'  # ВЕРНО с цифрой и подчеркиванием в username
address4 = 'чтото@geekbrains.ru'        # НЕ ВЕРНО username на кирилице
address5 = 'someone@geek-brains.ru'     # ВЕРНО domain с тире
address6 = 'someone@geekbrains1.ru'     # ВЕРНО domain с цифрой
address7 = 'someone@geekbrainsru'       # ВЕРНО domain без точки
address8 = 'someone@гикbrains.ru'       # НЕ ВЕРНО domain с кирилицей

address = (address1, address2, address3, address4, address5, address6, address7, address8)

for i in address:
    try:
        print(email_parse(i))
    except ValueError:
        print(f'wrong email: {i}')
