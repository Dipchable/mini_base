mini_base = dict()
last_comand = list()

#Работа с базой данных
def set_base(comand_input, type_base):
	if comand_input == '':
		return
	if comand_input[0] == 'SET':
		type_base[comand_input[1]] = comand_input[2]
	elif comand_input[0] == 'GET':
		if type_base.get(comand_input[1]):
			print(type_base[comand_input[1]])
		else:
			print("NULL")
	elif comand_input[0] == 'UNSET':
		if type_base.get(comand_input[1]):
			type_base.pop(comand_input[1])
		else:
			print("NULL")
	elif comand_input[0] == 'COUNTS':
		c = 0
		for i in type_base:
			if type_base[i] == comand_input[1]:
				c += 1
		print(c)
	elif comand_input[0] == 'FIND':
		for i in type_base:
			if type_base[i] == comand_input[1]:
				print(i)

while True:
	comand_input = input()
	if comand_input == 'END':
		break
	comand_input = comand_input.split(' ')
	if comand_input[0] == 'SET' or comand_input[0] == 'UNSET': #запоминаем последние команды для каждого элемент БД
		c = 0
		for i in range(len(last_comand)):
			if last_comand[i][1] == comand_input[1]:
				last_comand.pop(i)
				break
		last_comand.append(comand_input)
	if comand_input[0] == 'BEGIN': #транзакции
		comand_input_last = ''
		base_temp = mini_base.copy()
		while True:
			comand_input = input()
			comand_input = comand_input.split(' ')
			if comand_input[0] == 'COMMIT':
				mini_base = base_temp.copy()
				base_temp.clear()
				break
			if comand_input[0] == 'ROLLBACK':
				if last_comand:
					for i in range(len(last_comand)):
						if last_comand[i][1] == comand_input_last[1]:
							set_base(last_comand[i], base_temp)
				elif comand_input_last[0] == 'SET':
					comand_input_last[0] = 'UNSET'
					set_base(comand_input_last, base_temp)
				elif comand_input_last[0] == 'UNSET':
					comand_input_last[0] = 'SET'
					set_base(comand_input_last, base_temp)
				comand_input_last = ''
			else:
				set_base(comand_input_last, base_temp)
				if comand_input[0] == 'SET' or comand_input[0] == 'UNSET':
					if comand_input_last != '':
						for i in range(len(last_comand)):
							if last_comand[i][1] == comand_input_last[1]:
								last_comand.pop(i)
								break
						last_comand.append(comand_input_last)
					comand_input_last = comand_input
				else:
					set_base(comand_input, base_temp)
	set_base(comand_input, mini_base)