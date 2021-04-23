# ICSSgen v1.4, 2021-04-24
# 2D-ICSS input file generator powered by Python 3.9
# Written by Zhe Wang, Hiroshima university
# Catch me with wongzit@yahoo.co.jp
# Personal webpage: https://www.wangzhe95.net

import random

# Program information section
print("*******************************************************************************")
print("*                                                                             *")
print("*      $$$     $$$$      $$$$      $$$$                                       *")
print("*       $    $$    $$  $$    $$  $$    $$                                     *")
print("*       $   $$         $$        $$                                           *")
print("*       $   $$           $$$$      $$$$      $$$$      $$$$    $$$$$$$        *")
print("*       $   $$               $$        $$  $$    $$  $$    $$  $$    $$       *")
print("*       $    $$    $$  $$    $$  $$    $$  $$    $$  $$    $$  $$    $$       *")
print("*      $$$     $$$$      $$$$      $$$$      $$$$$$  $$$$$$$   $$    $$       *")
print("*                                                $$  $$        $$    $$       *")
print("*                                          $$    $$   $$$$$$   $$    $$       *")
print("*                                            $$$$                             *")
print("*                                                                             *")
print("*     =================== Version 1.4 for Source Code ===================     *")
print("*                           Last update: 2021-04-24                           *")
print("*                                                                             *")
print("*      A ICSS input file generator, developed by Zhe Wang. Online document    *")
print("*    is available from GitHub (https://github.com/wongzit/ICSSgen).           *")
print("*                                                                             *")
print("*                             -- Catch me with --                             *")
print("*                         E-mail  wongzit@yahoo.co.jp                         *")
print("*               Personal webpage  https://www.wangzhe95.net                   *")
print("*                                                                             *")
print("*******************************************************************************")
print("\nPRESS Ctrl+c to exit the program.\n")


# ========================== Read original input file ==========================
print("Please specify the original input file path:")

fileName = input("(eg.: /ICSSgen/example/benzene.gjf)\n")
if fileName.strip()[0] == '\'' and fileName.strip()[-1] == '\'':
    fileName = fileName[1:-2]

with open(fileName.strip(), 'r') as originalInput:
    inputLines = originalInput.readlines()

# ========================== Working parameters ==========================
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

# Specify the altitude over the plane
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

# Specify grid
print("Please specify the grid quality (value smaller than 0.25 is recommanded):")
userGrid = input("(press Enter to use default value 0.2)\n")
if userGrid:
    grid = float(userGrid)
    if grid < 0:
    	grid = 0 - grid
    elif grid == 0:
    	print("Input error, default grid value 0.2 will be used.\n")
    	grid = 0.2
else:
    grid = 0.2
print(f"ICSSgen will use grid quality of {grid}.\n")

# ========================== ICSS input file section ==========================
# Creat input file for ICSS
routeLine = []
coordinatesLine = []
chargeSpin = ''

for line in inputLines:

    if line[0] == '%':
        routeLine.append(line)

    elif line[0] == '#':
        if 'geom=connectivity' in line.lower():
            routeLine.append(line)
        else:
            routeLine.append(f"{line.rstrip()} geom=connectivity\n")

    elif len(line.split()) == 2 and len(''.join(line.rstrip())) < 6:
        chargeSpin = line

    elif ( line[0].isalpha or line[1].isalpha ) and line.count('.') == 3:
        coordinatesLine.append(f"{line.rstrip()}\n")

icssInput = open(f"{fileName.strip()[:-4]}_ICSS_{plane.upper()}_{int(altitude)}.gjf", "w")

for route in routeLine:
    icssInput.write(route)

icssInput.write(f"\n{fileName.strip()[:-4]}_ICSS_{plane.upper()}_{int(altitude)}//Created_by_ICSSgen\n\n")
icssInput.write(chargeSpin)

for i in range(len(coordinatesLine)):
    icssInput.write(coordinatesLine[i])

# Coordinates of Bq atoms
if planeFlag == 1:
    x_position = x_min
    bqFlag = 0     # Total Bq atom: 10*(max-min)+1
    while x_position <= (x_max + 0.5 * grid):
        y_position = y_min
        while y_position <= (y_max + 0.5 * grid):
            icssInput.write(f" Bq      {round(x_position, 2)}      {round(y_position, 2)}      {round(z, 2)}\n")
            bqFlag += 1
            y_position += grid
        x_position += grid
    for bqNumber in list(range(1, bqFlag + len(coordinatesLine) + 1)):
        icssInput.write(f"\n{bqNumber}")

elif planeFlag == 2:
    x_position = x_min
    bqFlag = 0
    while x_position <= (x_max + 0.5 * grid):
        z_position = z_min
        while z_position <= (z_max + 0.5 * grid):
            icssInput.write(f" Bq      {round(x_position, 2)}      {round(y, 2)}      {round(z_position, 2)}\n")
            bqFlag += 1
            z_position += grid
        x_position += grid
    for bqNumber in list(range(1, bqFlag + len(coordinatesLine) + 1)):
        icssInput.write(f"\n{bqNumber}")

else:
    y_position = y_min
    bqFlag = 0
    while y_position <= (y_max + 0.5 * grid):
        z_position = z_min
        while z_position <= (z_max + 0.5 * grid):
            icssInput.write(f" Bq      {round(x, 2)}      {round(y_position, 2)}      {round(z_position, 2)}\n")
            bqFlag += 1
            z_position += grid
        y_position += grid
    for bqNumber in list(range(1, bqFlag + len(coordinatesLine) + 1)):
        icssInput.write(f"\n{bqNumber}")

icssInput.write("\n\n")
icssInput.close()

# ========================== Result information ==========================
print("\n*******************************************************************************")
print("")
print("                     Input file is successfully generated.")
print("                        Normal termination of ICSSgen.")
print("")
print("*******************************************************************************\n")

# ========================== Quotes output ==========================
quotes = [
    {'name': 'Ronald Anstrom', 'said': 'You know you\'re a teacher when you say 2, write 3, and mean 4.'},
    {'name': 'Werner von Barun', 'said': 'Research is what I am doing when I don\'t know what I am doing.'},
    {'name': 'Snoopy', 'said': 'Learn from yesterday, live for today, look to tomorrow, rest this afternoon.'},
#    {'name': 'NO NAME', 'said': 'The great thing about being imperfect is the joy it brings others.'},
    {'name': 'G. W. von Leibniz', 'said': 'It is unworthy of excellent men to lose hours like slaves in the labor of calculation which could be safely relegated to anyone else if a machine were used.'},
    {'name': 'From the back of a sugar packet', 'said': 'Achievement — the man who rows the boat generally doesn\'t have time to rock it'},
    {'name': 'Paul Dickson', 'said': 'Nothing will be attempted if all possible objections must first be overcome.'},
#    {'name': 'NO NAME', 'said': 'The reason man\'s best friend is a dog is because he wags his tail instead of his tongue.'},
    {'name': 'Murphy\'s twelfth law', 'said': 'If you perceive that there are four possible ways in which a procedure can go wrong and circumvent these, then a fifth way will develop.'},
    {'name': 'Margaret Thatcher', 'said': 'Standing in the middle of the road is very dangerous; you get knocked down by the traffic from both sides.'},
    {'name': 'Robert Frost', 'said': 'Forgive my nonsense as I also forgive those who think they talk sense.'},
#    {'name': 'NO NAME', 'said': 'When all else fails, try the boss\'s suggestion.'},
    {'name': 'Whistler\'s principle', 'said': 'If other people are going to talk, conversation is simply impossible.'},
    {'name': 'Bertrand Russell', 'said': 'There is much pleasure to be gained from useless knowledge.'},
    {'name': 'Steven Wright', 'said': 'Everywhere is walking distance if you have the time.'},
    {'name': 'Charles Bixton', 'said': 'You will never "find" time for anything. If you want time, you must make it.'},
    {'name': 'Alexander Pope', 'said': 'Be not the first by whom the new are tried, nor yet the the last to lay the old aside.'},
    {'name': 'The unnamed law from Paul Dickson\'s "The Official Rules"', 'said': 'If it happens, it must be possible.'},
#    {'name': 'NO NAME', 'said': 'College professor: someone who talks in other people\'s sleep.'},
    {'name': 'Kirkegaard', 'said': 'Life can only be understood backward, but must be lived forward.'},
    {'name': 'Richard Bach', 'said': 'The best way to pay for a lovely moment is to enjoy it.'},
    {'name': 'Mrs. Severn', 'said': 'Happiness is not having what you want — happiness is wanting what you have!'},
    {'name': 'Mark Twain', 'said': 'There ain\'t no surer way to find out whether you like people or hate them than to travel with them.'},
    {'name': 'Len Wein', 'said': 'A true friend is someone who is there for you when he\'d rather be anywhere else.'},
    {'name': 'Mark Twain', 'said': 'Sacred cows make the best hamburger.'},
    {'name': 'John Peers', 'said': 'The solution to a problem changes the problem.'},
#    {'name': '', 'said': ''},
]

length = len(quotes)
output = random.randint(0, length - 1)

print(f"{quotes[output]['said']}\n                     ---- {quotes[output]['name']}\n")
