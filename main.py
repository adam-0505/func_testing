def average(measurements):
    if len(measurements) == 0:
        return
    
    sum = 0

    for value in measurements:
        sum += value
    
    return sum / len(measurements)

def calculate_max(measurements):
    maximum = measurements[0]

    for value in measurements:
        if value > maximum:
            maximum = value

    return maximum

def calculate_min(measurements):
    minimum = measurements[0]

    for value in measurements:
        if value < minimum:
            minimum = value

    return minimum

def outliers(measurements, threshold):
    avg = average(measurements)
    measurement_outliers = []

    for value in measurements:
        diff = avg - value
        if diff > threshold or diff < -threshold:
            measurement_outliers.append(value)

    return measurement_outliers


def is_valid_value(measurement):
    return measurement >= 0 and measurement <= 40