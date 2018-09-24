class node(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self,src,dest):
        self.source=src
        self.destination=dest
    def getSource(self):
        return self.source
    def getDestination(self):
        return self.destination
    def __str__(self):
        return self.source+" ---->"+self.destination

class Digraph(object):
    def __init__(self):
        self.edges={}

    def addNode(self,node):
        if node in self.edges:
            raise ValueError("Duplicate")
        else:
            self.edges[node]=[]

    def addEdge(self,edge):
        src=edge.getSource()
        dest=edge.getDestination()
        if (src not in self.edges and dest not in self.edges):
            raise ValueError(" Node not in graph")
        else:
            self.edges[src].append(dest)

    def getchildren(self,node):
        return self.edges[node]

    def hasNode(self,node):
        return node in self.edges

    def getNode(self,name):
        for n in self.edges:
            if n.getName()==name:
                return n
        raise NameError(name)

    def __str__(self):
        result=""
        for src in self.edges:
            for dest in self.edges[src]:
                result=result+src.getName()+"---->"+dest.getName()+"\n"
        return result[:-1]
class Graph(Digraph):
    def addEdge(self,edge):
        Digraph.addEdge(self,edge)
        rev=Edge(edge.getDestination(),edge.getSource())
        Digraph.addEdge(self,rev)

def buildcitygraph(graphtype):
    g=graphtype()
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'):  # Create 7 nodes
        g.addNode(node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g

def dfs(graph,start,end,path,shortest,toPrint=False):
    path=path+[start]
    if toPrint:
        print("Current DFS PAth:",printpath(path))
    if start==end:
        return path
    for node in graph.getchildren(start):
        if node not in path:
            if shortest==None or len(path)<len(shortest):
                newPath=dfs(graph,node,end,path,shortest, toPrint)
                if newPath!=None:
                   shortest=newPath
        elif toPrint:
            print("Already Visited")
    return shortest

def shortestpath(graph,start,end):
   return  dfs(graph,start,end,[],None)


def printpath(path):
    result=''
    for i in range(len(path)):
        result+=str(path[i])
        if i!=len(path)-1:
            result+="--->"
    return result



g=buildcitygraph(Digraph)
print(printpath(shortestpath(g,g.getNode("Boston"),g.getNode("Phoenix"))))

