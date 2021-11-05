num = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
       'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate_adv(eng_num):
    if eng_num[0].isupper():
        return num.get(eng_num[0].lower() + eng_num[1:]).title()
    else:
        return num.get(eng_num)


print(num_translate_adv('two'))
print(num_translate_adv('Two'))
print(num_translate_adv('six'))
print(num_translate_adv('3354545'))
