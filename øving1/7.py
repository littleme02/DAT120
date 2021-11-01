time = float(input("Type seconds in float: "))
speed = round((9.81 * time), 2)
distance = round(0.5 * 9.81 * speed * time, 2)
print('Object traveled ' + str(distance) + ' meters, reaching ' + str(speed) + 'm/s')