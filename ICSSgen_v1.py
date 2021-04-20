# ICSSgen v1.0, 2021-04-20
# 2D-ICSS input file generator powered by Python 3
# Written by Zhe Wang in Hiroshima, Japan
# Catch me with wongzit@yahoo.co.jp
# Personal webpage: https://www.wangzhe95.net

# Program information section
print("========================================================")
print("")
print("                      ICSSgen v1.0")
print("             ------------------------------")
print("")
print("           Written by Zhe Wang with Python 3")
print("              E-mail: wongzit@yahoo.co.jp")
print("               https://www.wangzhe95.net")
print("")
print("              Hiroshima University, Japan")
print("")
print("========================================================")
print("Press Ctrl+c to exit the program.")
print("The default intercept is 0.2 angstrom, the value can be modified at line 113.\n")

# Read original input file
fileName = input("Please specify the original input file:\n")
with open(fileName.rstrip()) as originalInput:
#    contents = originalInput.read()
    lines = originalInput.readlines()

# Program running
plane = input("\nPlease specify the plane for ICSS map (XY, XZ, YZ):\n")
plane = plane.lower()

# For inputting correctly
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
altitude = float(input("\nPlease input the altitude over the plane (in angstrom):\n"))

# Specify the mapping range
if planeFlag == 1:
    z = altitude
    x_min, x_max = input("\nPlease specify the range of X axis (in angstrom, eg. -10 10):\n").split()
    x_min = float(x_min)
    x_max = float(x_max)
    y_min, y_max = input("\nPlease specify the range of Y axis (in angstrom, eg. -8 8):\n").split()
    y_min = float(y_min)
    y_max = float(y_max)
    print(f"\n2D-ICSS({plane.upper()},{altitude}) map in [X: {x_min} to {x_max}, Y: {y_min} to {y_max}].\n")

elif planeFlag == 2:
    y = altitude
    x_min, x_max = input("\nPlease specify the range of X axis (in angstrom, eg. -10 10):\n").split()
    x_min = float(x_min)
    x_max = float(x_max)
    z_min, z_max = input("\nPlease specify the range of Z axis (in angstrom, eg. -8 8):\n").split()
    z_min = float(z_min)
    z_max = float(z_max)
    print(f"\n2D-ICSS({plane.upper()},{altitude}) map in [X: {x_min} to {x_max}, Z: {z_min} to {z_max}].\n")

else:
    x = altitude
    y_min, y_max = input("\nPlease specify the range of Y axis (in angstrom, eg. -10 10):\n").split()
    y_min = float(y_min)
    y_max = float(y_max)
    z_min, z_max = input("\nPlease specify the range of Z axis (in angstrom, eg. -8 8):\n").split()
    z_min = float(z_min)
    z_max = float(z_max)
    print(f"\n2D-ICSS({plane.upper()},{altitude}) map in [Y: {y_min} to {y_max}, Z: {z_min} to {z_max}].")

# Creat input file for ICSS
#file = open(f"ICSS_{plane.upper()}_{int(altitude)}.gjf", "w")
file = open(f"{fileName.rstrip()[:-4]}_ICSS_{plane.upper()}_{int(altitude)}.gjf", "w")
lineCounter = 0
routeCounter = 0
for line in lines:
    if lineCounter == 0:
        if '#' in line:
            if 'geom=connectivity' not in line.lower():
                file.write(f"{line.rstrip()} geom=connectivity")
                lineCounter += 1
            else:
                file.write(f"{line.rstrip()}")
                lineCounter += 1
        else:
            file.write(f"{line.rstrip()}")
            lineCounter += 1
    else:
        if '#' in line:
            if 'geom=connectivity' not in line.lower():
                file.write(f"\n{line.rstrip()} geom=connectivity")
                lineCounter += 1
            else:
                file.write(f"\n{line.rstrip()}")
                lineCounter += 1
        else:
            file.write(f"\n{line.rstrip()}")
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
            file.write(f"Bq      {round(x_position, 2)}      {round(y_position, 2)}      {round(z, 2)}\n")
            bqFlag += 1
            y_position += intercept
        x_position += intercept
    file.write("\n")
    for bqNumber in list(range(1, bqFlag + lineCounter - routeCounter - 5)):
        file.write(f"{bqNumber}\n")
    file.write("\n")
    file.close()

elif planeFlag == 2:
    x_position = x_min
    bqFlag = 0
    while x_position <= x_max:
        z_position = z_min
        while z_position <= z_max:
            file.write(f"Bq      {round(x_position, 2)}      {round(y, 2)}      {round(z_position, 2)}\n")
            bqFlag += 1
            z_position += intercept
        x_position += intercept
    file.write("\n")
    for bqNumber in list(range(1, bqFlag + lineCounter - routeCounter - 5)):
        file.write(f"{bqNumber}\n")
    file.write("\n")
    file.close()

else:
    y_position = y_min
    bqFlag = 0
    while y_position <= y_max:
        z_position = z_min
        while z_position <= z_max:
            file.write(f"Bq      {round(x, 2)}      {round(y_position, 2)}      {round(z_position, 2)}\n")
            bqFlag += 1
            z_position += intercept
        y_position += intercept
    file.write("\n")
    for bqNumber in list(range(1, bqFlag + lineCounter - routeCounter - 5)):
        file.write(f"{bqNumber}\n")
    file.write("\n")
    file.close()

# Program termination
print("\n==============================")
print("Normal termination of ICSSgen.")
print("==============================\n")
