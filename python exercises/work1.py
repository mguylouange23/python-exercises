camel = input("Enter a camel case word:")
def change(camel):
    camele = list(camel)
    hen = []
    for char in camele:
        if char.isupper():
            hen.append("_")
            hen.append(char.lower())
        else:
            hen.append(char)
    cm = ''.join(hen)
    print(cm)

change(camel)