with open('benzene.gjf', 'r') as inputFile:
	inputLines = inputFile.readlines()

#newInput = open('newInputfile.gjf', 'w')

#routeCounter = 0
#atomCounter = 0

routeLine = []
coordinatesLine = []
chargeSpin = ''

#atom = {'atomNumber': '0', 'element': 'X', 'x_coor': '0.0', 'y_coor': '0.0', 'z_coor': '0.0'}

# How many atoms here
for line in inputLines:
	if line[0] == '%':
		routeLine.append(line)

	elif line[0] == '#':
		if 'geom=connectivity' in line:
			routeLine.append(line)
		else:
			routeLine.append(f"{line.rstrip()} geom=connectivity\n")
	
	elif len(line.split()) == 2 and len(''.join(line.rstrip())) < 6:
		chargeSpin = line

	elif ( line[0].isalpha or line[1].isalpha ) and line.count('.') == 3:
#		atomCounter += 1
		coordinatesLine.append(line)

icssInput = open('newInputfile.gjf', 'w')

for route in routeLine:
	icssInput.write(route)

icssInput.write('\nTitle\n\n')
icssInput.write(chargeSpin)

for i in range(len(coordinatesLine)):
	icssInput.write(coordinatesLine[i])

icssInput.close()

#print(coordinatesLine)
#print("No.     Element         X            Y            Z")
#for i in range(len(coordinatesLine)):
#	print(f" {i + 1}        {coordinatesLine[i].split()[0]}        {coordinatesLine[i].split()[1]} {coordinatesLine[i].split()[2]} {coordinatesLine[i].split()[3]}")


'''
# Reserve place for all atoms
for n in range(atomCounter):
	coordinates.append(atom)

# Write atom information
i = 0
for line in inputLines:
	if line[0] == '%':
		routeCounter += 1
	elif line[0] == '#':
		print("Method found!")
	elif ( line[0].isalpha or line[1].isalpha ) and line.count('.') == 3:
		coordinates[i]['atomNumber'] = i + 1
		coordinates[i]['element'] = line.split()[0]
		print(coordinates[i], i)
		print(coordinates)
		i += 1

'''

'''
coordinates[i]['x_coor'] = line.split()[1]
coordinates[i]['y_coor'] = line.split()[2]
coordinates[i]['z_coor'] = line.split()[3]




No.     Element              X            Y            Z
 1 C -0.42995840 0.20110957 0.00000000
 2 C 0.96520160 0.20110957 0.00000000
 3 C 1.66273960 1.40886057 0.00000000
 4 C 0.96508560 2.61736957 -0.00119900
 5 C -0.42973940 2.61729157 -0.00167800
 6 C -1.12734040 1.40908557 -0.00068200
 7 H -0.97971740 -0.75120743 0.00045000
 '''