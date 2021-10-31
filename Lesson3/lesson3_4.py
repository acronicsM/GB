def thesaurus(surname_dict_elem, name, surname):
    letter_name = name[0]
    name_surname = f'{name} {surname}'
    elem_dict = surname_dict_elem.get(letter_name)
    if elem_dict is None:
        surname_dict_elem[letter_name] = [name_surname]
    else:
        elem_dict.append(name_surname)


def thesaurus_adv(*args):
    surname_dict = dict()
    for elem in args:
        name, surname = elem.split()
        letter_surname = surname[0]

        if surname_dict.get(letter_surname) is None:
            surname_dict[letter_surname] = {}

        thesaurus(surname_dict[letter_surname], name, surname)

    new_dict = dict()
    for key_surname in sorted(surname_dict.keys()):
        dict_name = dict()
        for key_name in sorted(surname_dict[key_surname].keys()):
            dict_name[key_name] = surname_dict[key_surname][key_name]

        new_dict[key_surname] = dict_name

    return new_dict


print(thesaurus_adv("Иван Сергеев", "Алла Сидорова", "Инна Серова",
                    "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Василий Суриков"))
