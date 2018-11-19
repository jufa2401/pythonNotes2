# Make a BMI Calcualator that combines text and variables using commas. Remember to use the different operators.
def bmiWithInput():
    height: int = int(input("Enter height in inches: "))
    weight: int = int(input("Enter weight in lbs: "))
    bmiCalculate(height, weight)


def bmiCalculate(height: int, weight: int):
    # print("Enter height in inches and weight in lbs")
    bmi: int = 703 * (weight / height ** 2)
    outcome: str = "Your BMI is: "
    length = len(outcome)
    for letter in range(length):
        print(outcome[letter])

    print("Your BMI is:", "{:.2f}".format(bmi))


def countdown(upper: int, lower: int):
    for ct in range(lower, upper, -1):
        print(ct)


def greeting(cheer):
    length = len(cheer)
    for letter in range(length):
        print(cheer[letter])


def greetCountdown(upper: int, lower: int, cheer):
    countdown(upper, lower)
    print()
    greeting(cheer)


def midterm(x):
    import random
    data = []
    for ct in range(random.randint(0, 25)):
        data.insert(ct, random.randint(1, 100))
    print(data)
    import statistics
    print(statistics.median(data))
    # print(statistics.mode(data)

midterm()
