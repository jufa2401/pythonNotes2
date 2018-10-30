
# Justin Fabricius
grade = 90
if(grade < 60): print("f")
elif grade <65: print("d")
elif grade <72: print("c")
elif grade <84: print("b")
else: print("a")



Green = False
print("go")\
if(Green) else print("stop")


def cheerWhile(n):
    phrase = input("Give me a cheer! ")
    count = n
    while count > 0:
        print(count)
        count = count-1

    print()
    length = len(phrase)
    ltrcount = 0
    while ltrcount < length:
        print(phrase[ltrcount])
        ltrcount = ltrcount+1


def cheerFor(n):
    phrase = input("Give me a cheer! ")
    for number in range(n,0,-1):
        print(number)
    print()
    for letter in phrase:
        print(letter)



people = ['Contrad', 'Deepak','Heinrich','Tom']
ages = [29,30,34,36]

def runthroughLists(list1: list, list2:list):
    for elList1,elList2 in zip(list1,list2):
        print(elList1,elList2)

runthroughLists(people,ages)

twodimen = ['Contrad', 'Deepak','Heinrich','Tom'],[29,30,34,36]
def runthroughTwoDimensionalList(twodimensionallist: list):
    for elList in twodimensionallist:
        print(elList)

# This will only print symmetrical
runthroughLists(people,ages)

# This will print asymmetrically
runthroughTwoDimensionalList(twodimen)









