# Justin Fabricius



def askForPrice1020discount(price: int):
    while(test):
        test = True
        usertxt =input("What is your order price?")
        order = int(usertxt)
        if(order != None): test = False
    pct = ('10%'if order < price else "20%")
    if(order<price):
        order*=0.9
    else:
        order*=0.8

    outputstring = '{:.2f}'
    print("Discounted to:", outputstring.format(order),"which is equal to:",pct)

askForPrice1020discount(100)


# li = [False, True,False]
#
#
# if(li[1]):
#     print(li[1])
# else: print("gal en taber")