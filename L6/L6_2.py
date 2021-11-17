from os.path import join

ip_dict = dict()
spammers = list()
path = join('.', 'data', 'L61', 'nginx_logs.txt')

file = open(path, encoding='utf-8', mode='tr')

line = file.readline()

while line:
    remote_addr = line[:line.find(' - -')]
    current_element = ip_dict.get(remote_addr)
    ip_dict[remote_addr] = current_element + 1 if current_element is not None else 1
    line = file.readline()

file.close()

for i in range(3):
    max_id = max(ip_dict, key=ip_dict.get)
    elem = ip_dict.pop(max_id)
    spammers.append({max_id:elem})

print(f'топ 3 спамеров \n{spammers}')
