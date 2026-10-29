def ascii(L):
    ascii_list = []
    for ch in L:
        ascii_list.append(ord(ch))
    ascii_tuple = tuple(ascii_list)
    print("List of ASCII codes:", ascii_list)
    print("Tuple of ASCII codes:", ascii_tuple)
L = ['a', 'N', 'b', 'G', 'p', 'V', 't', 'Q', 'f', 'M']

ascii(L)



