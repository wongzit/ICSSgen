# ICSSgen v1.1, 2021-04-20
# 2D-ICSS input file generator powered by Python 3.9
# Written by Zhe Wang in Hiroshima, Japan
# Catch me with wongzit@yahoo.co.jp
# Personal webpage: https://www.wangzhe95.net

# Program information section
print("========================================================")
print("")
print("                      ICSSgen v1.1")
print("             ------------------------------")
print("")
print("          Written by Zhe Wang with Python 3.9")
print("              E-mail: wongzit@yahoo.co.jp")
print("               https://www.wangzhe95.net")
print("")
print("              Hiroshima University, Japan")
print("")
print("========================================================")
print("Press Ctrl+c to exit the program.")
print("The default intercept is 0.2 angstrom, the value can be modified at line 160.\n")

# Read original input file
print("Please specify the original input file path:")
fileName = input("(eg.: /ICSSgen/example/benzene.gjf)\n")
with open(fileName.rstrip(), 'r') as originalInput:
    lines = originalInput.readlines()

# Specify the map plane
plane = input("\nPlease specify the plane for ICSS map (XY, XZ, YZ):\n")
plane = plane.lower()

while plane != 'xy' and plane != 'xz' and plane != 'yz':
    print("\nInput error, please input again.\n")
    plane = input("Please specify the plane for ICSS map (XY, XZ, YZ):\n")
    plane = plane.lower()

# Checking which plane will be used for ICSS map
if plane == 'xy':
    planeFlag = 1
elif plane == 'xz':
    planeFlag = 2
else:
    planeFlag = 3

# Check the altitude over the plane
while True:
    try:
        altitude = float(input("\nPlease input the altitude over the plane (in angstrom):\n"))
        break
    except ValueError:
        print("\nInput error, please input a number!")
        continue

# Specify the mapping range
if planeFlag == 1:
    z = altitude
    while True:
        try:
            x_min, x_max = input("\nPlease specify the range of X axis (in angstrom, eg. -10 10):\n").split()
            x_min = float(x_min)
            x_max = float(x_max)
            break
        except ValueError:
            print("\nInput error, please input 2 numbers:")
            continue
    while True:
        try:
            y_min, y_max = input("\nPlease specify the range of Y axis (in angstrom, eg. -8 8):\n").split()
            y_min = float(y_min)
            y_max = float(y_max)
            break
        except ValueError:
            print("\nInput error, please input 2 numbers!")
            continue
    print(f"\n2D-ICSS({plane.upper()},{altitude}) map in [X: {x_min} to {x_max}, Y: {y_min} to {y_max}].\n")

elif planeFlag == 2:
    y = altitude
    while True:
        try:
            x_min, x_max = input("\nPlease specify the range of X axis (in angstrom, eg. -10 10):\n").split()
            x_min = float(x_min)
            x_max = float(x_max)
            break
        except ValueError:
            print("\nInput error, please input 2 numbers!")
            continue
    while True:
        try:
            z_min, z_max = input("\nPlease specify the range of Z axis (in angstrom, eg. -8 8):\n").split()
            z_min = float(z_min)
            z_max = float(z_max)
            break
        except ValueError:
            print("\nInput error, please input 2 numbers!")
            continue
    print(f"\n2D-ICSS({plane.upper()},{altitude}) map in [X: {x_min} to {x_max}, Z: {z_min} to {z_max}].\n")

else:
    x = altitude
    while True:
        try:
            y_min, y_max = input("\nPlease specify the range of Y axis (in angstrom, eg. -10 10):\n").split()
            y_min = float(y_min)
            y_max = float(y_max)
            break
        except ValueError:
            print("\nInput error, please input 2 numbers:")
            continue
    while True:
        try:
            z_min, z_max = input("\nPlease specify the range of Z axis (in angstrom, eg. -8 8):\n").split()
            z_min = float(z_min)
            z_max = float(z_max)
            break
        except ValueError:
            print("\nInput error, please input 2 numbers:")
            continue
    print(f"\n2D-ICSS({plane.upper()},{altitude}) map in [Y: {y_min} to {y_max}, Z: {z_min} to {z_max}].\n")

# Creat input file for ICSS
icssInput = open(f"{fileName.rstrip()[:-4]}_ICSS_{plane.upper()}_{int(altitude)}.gjf", "w")
lineCounter = 0
routeCounter = 0
for line in lines:
    if lineCounter == 0:
        if '#' in line:
            if 'geom=connectivity' not in line.lower():
                icssInput.write(f"{line.rstrip()} geom=connectivity\n")
                lineCounter += 1
            else:
                icssInput.write(line)
                lineCounter += 1
        else:
            icssInput.write(line)
            lineCounter += 1
    elif lineCounter < 9:
        if '#' in line:
            if 'geom=connectivity' not in line.lower():
                icssInput.write(f"{line.rstrip()} geom=connectivity\n")
                lineCounter += 1
            else:
                icssInput.write(line)
                lineCounter += 1
        else:
            icssInput.write(line)
            lineCounter += 1
    else:
#        if line == '\n':
#            line = line.strip('\n')
#        icssInput.write(f"\n{line.rstrip()}")
        if '.' in line:
            icssInput.write(line)
            lineCounter += 1
    if '%' in line:
        routeCounter += 1

# ********Intercept can be modified at here!*************
intercept = 0.2   # in angstrom
# *******************************************************

# Coordinates of Bq atoms
if planeFlag == 1:
    x_position = x_min
    bqFlag = 0     # Total Bq atom: 10*(max-min)+1
    while x_position <= x_max:
        y_position = y_min
        while y_position <= y_max:
            icssInput.write(f"Bq      {round(x_position, 2)}      {round(y_position, 2)}      {round(z, 2)}\n")
            bqFlag += 1
            y_position += intercept
        x_position += intercept
    for bqNumber in list(range(1, bqFlag + lineCounter - routeCounter - 4)):
        icssInput.write(f"\n{bqNumber}")

elif planeFlag == 2:
    x_position = x_min
    bqFlag = 0
    while x_position <= x_max:
        z_position = z_min
        while z_position <= z_max:
            icssInput.write(f"Bq      {round(x_position, 2)}      {round(y, 2)}      {round(z_position, 2)}\n")
            bqFlag += 1
            z_position += intercept
        x_position += intercept
    for bqNumber in list(range(1, bqFlag + lineCounter - routeCounter - 4)):
        icssInput.write(f"\n{bqNumber}")

else:
    y_position = y_min
    bqFlag = 0
    while y_position <= y_max:
        z_position = z_min
        while z_position <= z_max:
            icssInput.write(f"Bq      {round(x, 2)}      {round(y_position, 2)}      {round(z_position, 2)}\n")
            bqFlag += 1
            z_position += intercept
        y_position += intercept
    for bqNumber in list(range(1, bqFlag + lineCounter - routeCounter - 4)):
        icssInput.write(f"\n{bqNumber}")

icssInput.write("\n\n")
icssInput.close()

# Program termination
print("==============================")
print("Normal termination of ICSSgen.")
print("==============================\n")