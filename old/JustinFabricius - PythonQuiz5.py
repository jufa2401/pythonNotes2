



items = ['Chair', 'Laptop', 'Sweathirt', 'Socks']
prices = [100, 1000, 40, 10]

def runthroughLists(list1: list, list2:list):
    for elList1,elList2 in zip(list1,list2):
        print(elList1,elList2)

runthroughLists(items,prices)

