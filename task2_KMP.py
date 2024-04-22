from task1_Border_array import prefix_border_array

a = "лилилась лилилось"
t = "лилила"

prefix_array = prefix_border_array(t)


def kmp(a, t):
    m = len(t)
    n = len(a)
    p = prefix_border_array(t)
    i = 0
    j = 0

    while i < n:
        if a[i] == t[j]:
            i += 1
            j += 1
            if j == m:
                return True
        else:
            if j > 0:
                j = p[j - 1]
            else:
                i += 1

    if i == n:
        return False


print(list(a))
print(list(t))
print(prefix_array)
print("Образ найден" if kmp(a, t) else "Не найден")
