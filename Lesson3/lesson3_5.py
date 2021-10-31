from random import randint as rnd

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(number_jokes, nouns_n, adverbs_n, adjectives_n):
    """
    Функция создает список шуток
    :param number_jokes: Количество шуток
    :param nouns_n: список существительных
    :param adverbs_n: списк наречий
    :param adjectives_n: список прилагательных
    :return: список шуток
    """
    jokes = []
    len_nouns = len(nouns_n)-1
    len_adverbs = len(adverbs_n)-1
    len_adjectives = len(adjectives_n)-1
    for i in range(number_jokes):
        jokes_nouns = nouns[rnd(0, len_nouns)]
        jokes_adverbs = adverbs[rnd(0, len_adverbs)]
        jokes_adjectives = adjectives[rnd(0, len_adjectives)]
        jokes.append(f'{jokes_nouns} {jokes_adverbs} {jokes_adjectives}')

    return jokes


print(get_jokes(5, nouns, adverbs, adjectives))
print(get_jokes(3, adjectives_n=adjectives, adverbs_n=adverbs, nouns_n=nouns))
