word = input("Enter a tweet word:")
def remove(word):
    wrd = list(word)
    vowels = ["A","E","O","U","I","a","e","u","i","o"]
    index =[]
    for char in wrd:
        if char not in vowels:
            index.append(char)
    
    result =''.join(index)
    print(result)


remove(word)