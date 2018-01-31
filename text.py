import sys
t = input("Input your text: ")
l = input("Choose limit: ")

def trimmed_text(text, limit):
    r = []
    i = 0
    for l in text:
        i += 1
        if i >= int(limit) and l == ' ':
            break
        r.append(l)

    r.append('...')
    return(''.join(r))
print(trimmed_text(t, l))
