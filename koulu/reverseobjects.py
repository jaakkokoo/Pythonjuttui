from stack import Stack

def reverseObjects(sequence):
	reversed_list = []
	pino = Stack()
	list_count = 0
	i = 0
	a = 0
	#pushataan sequence stackiin:
	for a in sequence:
		list_count += 1
		pino.push(a)
	#puretaan stack reverse_listiin
	while i != list_count:
		reversed_list.append(pino.pop())
		i += 1 
	return reversed_list
