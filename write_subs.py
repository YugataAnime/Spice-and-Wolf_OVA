# check subs
f = open("subs.txt", "r", encoding='utf-8')
Sub = f.readlines()[33:]

writeLine = list()
indexWriteLine = 0

for line in Sub:

	Name = False
	Dialog = False
	index1 = 0
	indexStartDialog = 0

	writeLine.append(['',''])

	for i in line:
		if i == ',' and index1 == 3:
			Name = True
		elif i == ',' and index1 == 8:
			Dialog = True

		elif i != ',':

			if Name == True:
				if i == 'Х':
					NameText = 'Хоро'
				elif i == 'Л':
					NameText = 'Лоуренс'
				elif i == 'Н':
					NameText = 'Нора'
				writeLine[indexWriteLine][0] = NameText

				Name = False

			if Dialog == True:

				writeLine[indexWriteLine][1] = Sub[indexWriteLine][indexStartDialog:-1]

				Dialog = False

		if i == ',':
			index1 +=1

		indexStartDialog += 1
	
	indexWriteLine += 1

f.close()

with open("subsAfterProgram.txt", "w") as file:

	for i in writeLine:

		if i[0] == 'Нора' or i[0] == 'Хоро':
			spaces = 4
		else:
			spaces = 1

		file.write(i[0] + ' ' * spaces + ':=> ' + i[1] + '\n')