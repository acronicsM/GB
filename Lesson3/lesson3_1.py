num = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь',
       'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(eng_num):
    """
    Функция переводит числительное
    :param eng_num: числительное на английском
    :return: числительное на русском
    """
    return num.get(eng_num)


print(num_translate('two'))
print(num_translate('six'))
print(num_translate('3354545'))
