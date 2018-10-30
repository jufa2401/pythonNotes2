phrase = 'python!'
ct = len(phrase)-1
while ct > 0:
    print(phrase[ct])
    ct=ct-1

def taxCalculator():
    income = float(input("What is your income?"))
    if income <= 10000:
        taxrate = 0.0
    elif income <= 30000:
        taxrate = 0.2
    elif income <= 100000:
        taxrate = 0.35
    elif income <= 60000: # Take notice of order, this condition will never happen
        taxrate = 0.25

    else:
        taxrate = 0.45
    taxed = income*taxrate

    outputstringDollar = '${:.2f}'
    outputstringpct = '{:.0f}%'
    print('Your income is',outputstringDollar.format(income),'please pay',outputstringDollar.format(taxed), 'equal to',outputstringpct.format(taxrate*100)) \
    if income >= 10000 else print("You owe no taxes")


taxCalculator()
