def medianlow_generated_data():
    import statistics, random
    data: list[int] = []
    for ct in range(10):
        data.append(random.randint(1, 10))
    print('Generated data:', data)
    return statistics.median_low(data)


print(medianlow_generated_data())


def mode_generated_data():
    import statistics, random
    data: list[int] = []
    for ct in range(10):
        data.append(random.randint(8, 10))
    print('Generated data:', data)
    return statistics.mode(data)


# print(mode_generated_data())


def mode2():
    import statistics
    return statistics.median(range(0, 10))


print("Mode:", mode2())
