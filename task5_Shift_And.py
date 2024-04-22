def shift_and(p, text):
    b = {}
    l = len(p)
    tl = len(text)

    for i in range(l):
        b[p[i]] = 0

    for i in range(l):
        b[p[i]] |= (1 << i)

    d = 0
    match_mask = 1 << (l - 1)
    for i in range(tl):
        d = ((d << 1) | 1) & (b.get(text[i], 0))
        matched = (d & match_mask)
        if matched != 0:
            return i - l + 1
    return -1


pattern = "abra"
text = "adracadabra"
print("Позиция образца в строке:", shift_and(pattern, text))
