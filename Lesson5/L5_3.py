print('Учеников больше классов')

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

max_k = len(klasses)
gen = ((name, klasses[idx] if idx < max_k else None) for idx, name in enumerate(tutors))

print(type(gen))
for i in gen:
    print(i)

print('Учеников меньше классов')

klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
max_k = len(klasses)

gen = ((name, klasses[idx] if idx < max_k else None) for idx, name in enumerate(tutors))

print(type(gen))
for i in gen:
    print(i)
