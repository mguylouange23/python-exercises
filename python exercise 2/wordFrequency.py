word = input("Enter a sentence: ")

def change(word):
    b = {}
    ts = word.split()
    for t in ts:
        if t in b:
            b[t] += 1
        else:
            b[t] = 1
    print(b)

change(word)