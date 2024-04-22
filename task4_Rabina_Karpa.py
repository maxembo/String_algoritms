Q = 256
B = 13


def get_hash(text: str) -> int:
    global B, Q
    n = len(text)
    result = 0
    for i in range(n):
        result = (B * result + ord(text[i])) % Q
    return result


def search_patterns_in_text(main_text: str, pattern: str) -> int:
    global B, Q
    main_text_len = len(main_text)
    pattern_len = len(pattern)

    multiplier = 1
    for i in range(1, pattern_len):
        multiplier = (multiplier * B) % Q

    pattern_hash = get_hash(pattern)
    text_hash = get_hash(main_text[:pattern_len])

    for index_symbol in range(main_text_len - pattern_len + 1):
        if pattern_hash == text_hash and main_text[index_symbol: index_symbol + pattern_len] == pattern:

            return True

        if index_symbol < main_text_len - pattern_len:
            text_hash = ((text_hash - ord(main_text[index_symbol]) * multiplier) * B + ord(main_text[index_symbol + pattern_len])) % Q

            if text_hash < 0:
                text_hash += Q

    return False


p = "mem"
text = "menlem"
print(search_patterns_in_text(text, p))

