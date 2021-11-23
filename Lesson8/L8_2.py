from pathlib import Path
import re


def parsing_log(str_log):
    # reg_pattern = r'(?<IP>([0-9a-fA-F]{0,4}((^|:)([0-9a-fA-F]{0,4})){1,8})|([0-9]{1,3}[\.]){3}[0-9]{1,3})(.+\[)(
    # ?P<date>[a-zA-z0-9\/\:\+\ ]+)(\].+?\")(?P<get>[A-Z]+)(.+?)(?P<adr>[\S]+)(.+)(?P<answ>\d{3})(\s)(?P<ping>\d+)'
    reg_pattern = r'''
        (?P<IP>                         #Группа IP
        ([0-9a-fA-F]{1,4}((^|:)([0-9a-fA-F]{0,4})){1,8})        #ipv6
        |                               #ИЛИ
        ([0-9]{1,3}[\.]){3}[0-9]{1,3}                           #ipv4
        )                               #Окончание группы IP
        (.+\[)                          #Пропускаем символы разделетели
        (?P<date>                       #Начало группы date
        [a-zA-z0-9\/\:\+\ ]+            #Все латинские буквы + цифры + обратный слеш, двоеточие, плюс, пробел
        )                               #Окончание группы date
        (\].+?\")                       #Пропускаем символы разделетели
        (?P<get>                        #Начало группы get
        [A-Z]+                          #Заглавные латинские символы
        )                               #Окончание группы get
        (.+?)                           #Пропускаем символы разделетели
        (?P<adr>                        #Начало группы adr
        [\S]+                           #Все символы кроме пробела
        )                               #Окончание группы adr
        (.+)                            #Пропускаем символы разделетели
        (?P<answ>                       #Начало группы answ
        \d{3}                           #3 цифр подряд
        )                               #Окончание группы answ
        (\s)                            #Пропускаем символы разделетели
        (?P<ping>                       #Начало группы ping
        \d+                             #Цифры любое количество
        )                               #Окончание группы Цифры
    '''

    data = re.match(reg_pattern, str_log, re.X)
    if data is None:
        raise ValueError(f'wrong parsing: {str_log}')
    else:
        return tuple(data.groupdict().values())


list_IP = list()
path_log = Path.cwd() / 'task8_2' / 'nginx_logs.txt'

with path_log.open(encoding='utf-8', mode='tr') as file:
    for line in file:
        try:
            log = parsing_log(line)
            list_IP.append(log[0])
        except ValueError as er:
            print(er.args[0].rstrip())

print(list(set(list_IP)))
