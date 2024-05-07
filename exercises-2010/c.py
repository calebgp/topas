def split_n(text, n):
    return [text[i: i + n] for i in range(len(text))]


p = input()
q = input()
q = split_n(q, len(p))
print(q.count(p))
