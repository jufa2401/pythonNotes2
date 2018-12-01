import csv


def csvRead():
    with open('employee_birthday.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')


def csvReadDictionary():
    with open('employee_birthday.txt', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row[
                "birthday month"]}.')
            line_count += 1
        print(f'Processed {line_count} lines.')


# csvRead()
# csvReadDictionary()

def writeField():
    with open('employee_file.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        employee_writer.writerow(['John Smith', 'Accounting', 'November'])
        employee_writer.writerow(['Erica Meyers', 'IT', 'March'])


# csv in class
def writeInClassExercise():
    f = open("somecsv.csv", mode='a', newline='')
    csv.writer(f).writerow(["Storfedlort", "Jens"])
    f.close()


# csv in class
def writeInClassExercise3(infoList: list, filename: str = "default.csv"):
    f = open(filename, mode='a', newline='')
    csv.writer(f).writerow(infoList)
    f.close()


def readInClassExercise2(filename: str):
    try:
        starter = open(filename, mode='r', newline='')
        reader = csv.reader(starter)
        for row in reader:
            print(row)
        starter.close()
    except:
        print("Invalid filename")

    import random
    import math
    import statistics

    m = statistics.mean([10, 20, 30, 40, 40, 50, 60])
    s = statistics.stdev([10, 20, 30, 40, 40, 50, 60])
    r = random.choice([10, 20, 30, 40, 40, 50, 60])
    c = math.factorial(r)
    s = math.fsum([10, 20, 30, 40, 40, 50, 60])
    print('results:', m, s, r, c, s)


def evenTo100():
    for num in range(0, 101, 2):
        print(num)


def oddNumbersTo99():
    for num in range(1, 100, 2):
        print(num)


def allnumTo50():
    for num in range(51):
        print(num)


def allEvenNumDown():
    for num in range(100, -1, -1):
        print(num)


def midterm():
    import statistics, random
    data = []
    for cnt in range(10):
        data.insert(cnt, random.randint(0, 100))

    print("Generated the following list randomly:")
    print(data)
    return statistics.median(data)


# print(midterm())

def pendulumThings():
    import pendulum
    print(pendulum.now)


pendulumThings()

# writeInClassExercise3("bigboi.csv",["jens","ole","bob","ole","bob","ole","bob","ole","bob","ole","bob","ole","bob"])


# readInClassExercise2("somecsv.csvsd")
# writeInClassExercise()
# csv_reader = csv.reader(csv_file,delimiter = ',')
