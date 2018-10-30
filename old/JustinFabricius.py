phrase = "Go spartans!"
ct = 0
while ct < 233:
    print(ct)
    ct = ct+3


for letter in phrase: print(letter)

for a in range(10,21):
    print(a)

surnames = ['Rivest', 'Shamir', 'Adleman']
for position, surname in enumerate(surnames):
    print(position, surname)

items = ['Chair', 'Laptop', 'Sweatshirt', 'Socks']
prices = [100, 1000, 40, 10]

def runthroughLists(list1: list, list2:list):
    for elList1,elList2 in zip(list1,list2):
        print(elList1,elList2)

runthroughLists(items,prices)

def taxCalculator():
    income = float(input("What is your income?"))
    if income <= 10000:
        taxrate = 0.0
    elif income <= 30000:
        taxrate = 0.2
    elif income <= 60000:
        taxrate = 0.25
    elif income <= 100000:
        taxrate = 0.35
    else:
        taxrate = 0.45
    taxrate = income*taxrate

    outputstringDollar = '${:.2f}'
    outputstringpct = '{:.0f}%'
    print('Your income is',outputstringDollar.format(income),'please pay',outputstringDollar.format(taxrate)) \
        if income >= 10000 else print("You owe no taxes")

taxCalculator()

print(type(b) == str) # Type checking

a = 5
b = '6'
print(str(a)+b)
print(a+int(b))
try: print(a+b)
except: ValueError("Integer error")
print("The number entered is:",a," and is an integer")

# I believe this is what you wanted, I never got to control because I was helping the people around me.
outputFormat = '{:.2f}'
def bmiCalculate(height: int,weight: int):
    print("Your BMI is: ",outputFormat.format(703 * (weight / height ** 2)))


weight = input('What is your weight? ')
try:weightnum = float(weight)
except: ValueError("Not a valid number")  # Notice how it is intelligent enough to keep the 5 as input
height = input('What is your height? ')
try:heightnum = float(height)
except:print("Not a valid number")

bmiCalculate(heightnum,weightnum)

