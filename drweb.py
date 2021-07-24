mini_base = dict()

while True:
	n = input()
	if n == 'END':
		break
	n = n.split(' ')
	if n[0] == 'SET':
		mini_base[n[1]] = n[2]
	elif n[0] == 'GET':
		if mini_base.get(n[1]):
			print(mini_base[n[1]])
		else:
			print("NULL")
	elif n[0] == 'UNSET':
		if mini_base.get(n[1]):
			mini_base.pop(n[1])
		else:
			print("NULL")
	elif n[0] == 'COUNTS':
		c = 0
		for i in mini_base:
			if mini_base[i] == n[1]:
				c += 1
		print(c)
	elif n[0] == 'FIND':
		for i in mini_base:
			if mini_base[i] == n[1]:
				print(i)

print(mini_base)