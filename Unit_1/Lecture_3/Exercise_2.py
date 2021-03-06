from Unit_1.Lecture_3.graphs import *

nodes = list()
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)


edges = list()
edges.append(Edge(g.getNode('ABC'), g.getNode('BAC')))
edges.append(Edge(g.getNode('ABC'), g.getNode('ACB')))
edges.append(Edge(g.getNode('ACB'), g.getNode('CAB')))
edges.append(Edge(g.getNode('BAC'), g.getNode('BCA')))
edges.append(Edge(g.getNode('BCA'), g.getNode('CBA')))
edges.append(Edge(g.getNode('CBA'), g.getNode('CAB')))

for n in edges:
    g.addEdge(n)

print(g)