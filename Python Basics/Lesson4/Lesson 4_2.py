from requests import get, utils as ut


def currency_rates(url_course, currency):
    response = get(url_course)
    encodings = ut.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    char_code = content.find(f'>{currency.upper()}<')

    if char_code == -1:
        return

    end = content.find('</Value>', char_code)
    start = content.find('<Value>', char_code, end) + 7

    value = float(content[start:end].replace(',', '.'))

    return value


if __name__ == '__main__':
    print(currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', 'usD1'))
    print(currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', 'EUR'))
    print(currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', 'GBP'))
