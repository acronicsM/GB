def thesaurus(*args):
    name_dict = dict()
    for name in args:
        f_letter = name[0]
        elem_dict = name_dict.get(f_letter)
        if elem_dict is None:
            name_dict[f_letter] = [name]
        else:
            elem_dict.append(name)
    return name_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
