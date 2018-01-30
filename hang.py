import sys
x = input("Please input your word: ")
y = input("Please input letters to substittute: ")

def hangman(word, letters):
    l = []
    for i in word:
        if i in letters:
            l.append('_')
        else:
            l.append(i)
    s = ''.join(l)
    return(s)
print(hangman(x, y))
