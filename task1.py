
def prefix_border_array(s: str) -> list:
    n: int = len(s)
    bp = [0] * n

    for i in range(1, n):
        bp_right = bp[i - 1]

        while bp_right > 0 and s[i] != s[bp_right]:
            bp_right = bp[bp_right - 1]

        if s[i] == s[bp_right]:
            bp[i] = bp_right + 1
        else:
            bp[i] = 0

    return bp


test_str = "ABCABABCAL"

border_array = prefix_border_array(test_str)

print([i for i in test_str])
print(border_array)

