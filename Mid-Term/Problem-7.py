
nodes = []
for i in range(n):
    nodes.append(newNode(i))


for i in range(len(nodes)):
	x = random.choice(nodes)
	y = random.choice(nodes)
	addEdge(x,y)


for i in range(len(nodes)):
	x = random.choice(nodes)
	y = random.choice(nodes)
	addEdge(x,y)
	addEdge(y,x)
	


for i in range(len(nodes)):
	w = random.choice(nodes)
	x = random.choice(nodes)
	y = random.choice(nodes)
	z = random.choice(nodes)
	addEdge(w,x)
	addEdge(x,y)
	addEdge(y,z)
	addEdge(z,w)


for x in nodes:
	for y in nodes:
		addEdge(x,y)
		addEdge(y,x)
	

