b = input("Enter any string:")
def change(b):
    ts = b.split()
    dict = {}
    for t in ts:
        dict[t] = len(t)
    print(dict)

change(b)