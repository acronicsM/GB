def thesaurus_adv(*args):
    surname_dict = dict()
    for elem in sorted(args):
        name, surname = elem.split()
        letter_surname = surname[0]
        letter_name = name[0]

        elem_dict_s = surname_dict.get(letter_surname)
        if elem_dict_s is None:
            surname_dict[letter_surname] = {letter_name: [elem]}
        else:
            elem_dict_n = elem_dict_s.get(letter_name)
            if elem_dict_n is None:
                elem_dict_s[letter_name] = [elem]
            else:
                elem_dict_n.append(elem)

    new_dict = dict()
    for key_surname in sorted(surname_dict.keys()):
        new_dict[key_surname] = surname_dict[key_surname]

    return new_dict


print(thesaurus_adv("Иван Сергеев", "Алла Сидорова", "Инна Серова",
                    "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Василий Суриков"))
