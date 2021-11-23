from os.path import join

list_return = list()
path = join('.', 'data', 'L61', 'nginx_logs.txt')

file = open(path, encoding='utf-8', mode='tr')

for line_id, line in enumerate(file):
    # ('141.138.90.60', 'GET', '/downloads/product_2'),
    # `(< remote_addr >, < request_type >, < requested_resource >)
    minus_idx = line.find(' - -')
    square_idx = line.find(']', minus_idx) + 3
    type_idx = line.find(' ', square_idx)

    if minus_idx == -1 or square_idx == -1 or type_idx == -1:
        print(f'строка {line_id} не соотвествует шаблону')
        continue

    remote_addr = line[:minus_idx]
    request_type = line[square_idx:type_idx]
    requested_resource = line[type_idx+1:line.find(' ', type_idx+1)]

    list_return.append((remote_addr, request_type, requested_resource))

    if line_id == 3: break # для удобства чтение первый 3 строк

file.close()

print(list_return)
