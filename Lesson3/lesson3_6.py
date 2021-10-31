from random import randint as rnd

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(number_jokes, nouns_n, adverbs_n, adjectives_n, flag=True):
    jokes = []
    for i in range(number_jokes):
        len_nouns = len(nouns_n) - 1
        len_adverbs = len(adverbs_n) - 1
        len_adjectives = len(adjectives_n) - 1

        if len_nouns > 0:
            index_nouns = rnd(0, len_nouns-1)
            jokes_nouns = nouns_n[index_nouns]
            if flag:
                nouns_n.pop(index_nouns)
        else:
            jokes_nouns = ''

        if len_adverbs > 0:
            index_adverbs = rnd(0, len_adverbs - 1)
            jokes_adverbs = adverbs_n[index_adverbs]
            if flag:
                adverbs_n.pop(index_adverbs)
        else:
            jokes_adverbs = ''

        if len_nouns > 0:
            index_adjectives = rnd(0, len_adjectives - 1)
            jokes_adjectives = adjectives_n[index_adjectives]
            if flag:
                adjectives_n.pop(index_adjectives)
        else:
            jokes_adjectives = ''

        jokes.append(f'{jokes_nouns} {jokes_adverbs} {jokes_adjectives}')

    return jokes


print(get_jokes(7, nouns, adverbs, adjectives))

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
print(get_jokes(7, nouns, adverbs, adjectives, False))
