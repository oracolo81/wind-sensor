def get_average(angles):
    sin_sum = 0.0
    cos_sum = 0.0

    for angle in angles:
        r = math.radians(angle)
        sin_sum += math.sin(r)
        cos_sum += math.cos(r)

    flen = float(len(angles))
    s = sin_sum / flen
    c = cos_sum / flen
    arc = math.degrees(math.atan(s / c))
    average = 0.0

    if s > 0 and c > 0:
        average = arc
    elif c < 0:
        average = arc + 180
    elif s < 0 and c > 0:
        average = arc + 360

    return 0.0 if average == 360 else average

def get_value(length=5):
        data = []
        print("Measuring wind direction for %d seconds..." % length)
        start_time = time.time()

        while time.time() - start_time <= length:
            wind = round(adc.value * 3.3, 1)
            if not wind in volts:  # keep only good measurements
                print('unknown value ' + str(wind))
            else:
                data.append(volts[wind])

        return get_average(data)