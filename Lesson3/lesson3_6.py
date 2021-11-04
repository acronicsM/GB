from random import randint as rnd


def get_jokes(number_jokes, nouns_n, adverbs_n, adjectives_n, flag=True):
    jokes = []
    nouns_n_sh = list(range(0, len(nouns_n)))
    adverbs_n_sh = list(range(0, len(adverbs_n)))
    adjectives_n_sh = list(range(0, len(adjectives_n)))

    for i in range(number_jokes):
        len_nouns = len(nouns_n_sh)
        len_adverbs = len(adverbs_n_sh)
        len_adjectives = len(adjectives_n_sh)

        if len_nouns > 0:
            index_nouns = rnd(0, len_nouns-1)
            jokes_nouns = nouns_n[nouns_n_sh[index_nouns]]
            if flag:
                nouns_n_sh.pop(index_nouns)
        else:
            jokes_nouns = ''

        if len_adverbs > 0:
            index_adverbs = rnd(0, len_adverbs - 1)
            jokes_adverbs = adverbs_n[adverbs_n_sh[index_adverbs]]
            if flag:
                adverbs_n_sh.pop(index_adverbs)
        else:
            jokes_adverbs = ''

        if len_nouns > 0:
            index_adjectives = rnd(0, len_adjectives - 1)
            jokes_adjectives = adjectives_n[adjectives_n_sh[index_adjectives]]
            if flag:
                adjectives_n_sh.pop(index_adjectives)
        else:
            jokes_adjectives = ''

        jokes.append(f'{jokes_nouns} {jokes_adverbs} {jokes_adjectives}')

    return jokes


print(get_jokes(7, ["автомобиль", "лес", "огонь", "город", "дом"], ["сегодня", "вчера", "завтра", "позавчера", "ночью"],
                ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]))
print(get_jokes(7, ["автомобиль", "лес", "огонь", "город", "дом"], ["сегодня", "вчера", "завтра", "позавчера", "ночью"],
                ["веселый", "яркий", "зеленый", "утопичный", "мягкий"], False))
