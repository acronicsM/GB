# Закодируйте любую строку по алгоритму Хаффмана.

import collections


class Sheet:
    def __init__(self, char='', weight=0, left=None, right=None):
        self.left = left
        self.right = right
        self.char = char
        self.weight = (left.weight + right.weight) if not char else weight


def huffman_tree(counter_str):
    # Получаем список элементов для создания дерева
    deque_h = counter_str.most_common()

    while len(deque_h) > 1:
        deque_h.sort(key=lambda i: -i[1])

        left, right = deque_h.pop(), deque_h.pop()

        left_sheet = left[0] if isinstance(left[0], Sheet) else Sheet(char=left[0], weight=left[1])
        right_sheet = right[0] if isinstance(right[0], Sheet) else Sheet(char=right[0], weight=right[1])

        top_sheet = Sheet(left=left_sheet, right=right_sheet)

        deque_h.append((top_sheet, top_sheet.weight))

    return deque_h[0][0]


def huffman_walk(root_haf, code_str):
    dict_huff = dict(code_str)
    l, r = '0', '1'

    def tree_recursion(level, ch):
        if isinstance(level.left, Sheet):
            tree_recursion(level.left, ''.join([ch, l]))
        else:
            dict_huff[level.char] = ch

        if isinstance(level.right, Sheet):
            tree_recursion(level.right, ''.join([ch, r]))
        else:
            dict_huff[level.char] = ch

    tree_recursion(root_haf.left, l)
    tree_recursion(root_haf.right, r)

    return dict_huff


def huffman_encode(input_str):
    code_str = collections.Counter(input_str)
    tree = huffman_tree(code_str)
    dict_huff = huffman_walk(tree, code_str)

    return " ".join(dict_huff[ch] for ch in input_str)


str1 = 'beep boop beer!'

print(str1)
print(huffman_encode(str1))
