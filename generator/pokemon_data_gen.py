import random

distribution = {30:[1,30],50:[31,60],70:[61,90],85:[91,120],92:[121,145],93:[146,151]}
prob = [30,50,70,85,92,93]

for i in range(100000):
	generator = random.randint(0,93)
	for e in prob:
		if generator <= e:
			choice = distribution[e]
			break
	low = choice[0]
	high = choice[1]
	print(random.randint(low,high))

for i in range(30000):
	event = random.randint(0,4)
	if event == 0:
		print(25)
	else:	
		generator = random.randint(0,93)
		for e in prob:
			if generator <= e:
				choice = distribution[e]
				break
		low = choice[0]
		high = choice[1]
		print(random.randint(low,high))

for i in range(70000):
	generator = random.randint(0,93)
	for e in prob:
		if generator <= e:
			choice = distribution[e]
			break
	low = choice[0]
	high = choice[1]
	print(random.randint(low,high))
