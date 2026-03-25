def average(measurements):
    sum = 0
    for value in measurements:
        sum += value
    return sum / len(measurements)