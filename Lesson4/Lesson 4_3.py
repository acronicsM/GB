from requests import get, utils as ut
from datetime import datetime


def url_content(url_course):
    """
    Функция возвращает текст файла с курсами
    :param url_course: url на файл с курсами
    :return: строка с текстом файлов с курсами
    """
    response = get(url_course)
    encodings = ut.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    return content


def currency_rates(content, currency):
    """
    Функция возвращает курс из текст
    :param content: стрка с курсами
    :param currency: Код валюты
    :return: Число(float)
    """
    char_code = content.find(currency.upper())

    if char_code == -1:
        return

    start = content.find('<Value>', char_code) + 7
    end = content.find('</Value>', start)

    value = float(content[start:end].replace(',', '.'))

    return value


def currency_rates_advanced(url_course, currency):
    """
    Функция возвращает дату и курс валюты
    :param url_course: url на файл с курсами
    :param currency: Код валюты
    :return: кортеж из даты и курса
    """
    content = url_content(url_course)

    value = currency_rates(content, currency)
    if value is None:
        return

    start_date = content.find('Date="')+6
    date = content[start_date:start_date+10].split('.')
    dt = datetime(int(date[2]), int(date[1]), int(date[0]))

    value = currency_rates(content, currency)

    return dt, value


if __name__ == '__main__':
    print(currency_rates_advanced('http://www.cbr.ru/scripts/XML_daily.asp', 'usD1'))
    print(currency_rates_advanced('http://www.cbr.ru/scripts/XML_daily.asp', 'EUR'))
    print(currency_rates_advanced('http://www.cbr.ru/scripts/XML_daily.asp', 'GBP'))
