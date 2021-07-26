mini_base = dict()

def set_base(input_cmd, type_base):
	if input_cmd == '':
		return
	if input_cmd[0] == 'SET':
		type_base[input_cmd[1]] = input_cmd[2]
	elif input_cmd[0] == 'GET':
		if type_base.get(input_cmd[1]):
			print(type_base[input_cmd[1]])
		else:
			print("NULL")
	elif input_cmd[0] == 'UNSET':
		if type_base.get(input_cmd[1]):
			type_base.pop(input_cmd[1])
		else:
			print("NULL")
	elif input_cmd[0] == 'COUNTS':
		c = 0
		for i in type_base:
			if type_base[i] == input_cmd[1]:
				c += 1
		print(c)
	elif input_cmd[0] == 'FIND':
		for i in type_base:
			if type_base[i] == input_cmd[1]:
				print(i)

n_first = ''
while True:
	n = input()
	if n == 'END':
		break
	n = n.split(' ')
	if n[0] == 'SET' or n[0] == 'UNSET':
		n_first = n
	set_base(n, mini_base)
	if n[0] == 'BEGIN':
		base_temp = mini_base.copy()
		n_last = ''
		# n_first = ''
		while True:
			n = input()
			n = n.split(' ')
			if n[0] == 'COMMIT':
				# for i in base_temp:
				mini_base = base_temp.copy()
				base_temp.clear()
				break
			if n[0] == 'ROLLBACK':
				print(n_first)
				set_base(n_first, base_temp)
				n_last = ''
			else:
				set_base(n_last, base_temp)
				if n[0] == 'SET' or n[0] == 'UNSET':
					if n_last != '':
						n_first = n_last
					n_last = n
				else:
					# n_first = n_last
					set_base(n_last, base_temp)
					set_base(n, base_temp)
print(mini_base)