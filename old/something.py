# Notice i made it strongly typed like i explained in class
import statistics
import calendar
def countdown(upper: int, lower: int):
    for ct in range(lower,upper,-1):
        print(ct)

def greeting(cheer:str):
    length = len(cheer)
    for letter in range(length):
        print(cheer[letter])

def greetCountdown(upper:int, lower:int, cheer:str):
    countdown(upper,lower)
    print()
    greeting(cheer)



greetCountdown(0,10,"hello")


# statistics.stdev()
# help(calendar)
print(calendar.weekday(1997,1,24))

