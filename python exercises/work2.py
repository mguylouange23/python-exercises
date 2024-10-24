ads = print("We sell coke here for 50 cents!")
coin = int(input("Enter a coin: "))
cion = [5,10,25]
amount = 0
def buy(coin,cion,amount):
    if coin in cion:
        amount+=coin
        remain = 50 - amount
        print("you have entered a",amount,"cents")
        print("Remaining amount equals",remain, "cents")
    else:
        print("Ënter a coin among", cion)
    
    while amount<50:
        ret = int(input("Enter a coin: "))
        if ret in cion:
            amount+=ret
            remain = 50 - amount
            print("you have entered a",amount,"cents")
            print("Remaining amount equals",remain, "cents")
        else:
            print("Ënter a coin among", cion)
            quit()
    if amount == 50:
        print("You have paid!")
    elif amount > 50:
        get = amount - 50
        print("You have paid!")
        print("You will get in return",get,"cents")


buy(coin,cion,amount)