import graphviz as gv

g1 = gv.Digraph(format='svg')

nodeStyle = {'style':'filled','shape':'circle','fixedsize':'true','fontcolor':'#FFFFF'}

print nodeStyle

Nodes = [[1,2,3],[2,3,4],[4,1,6],[2,2,8],[6,7,8]]
Temp = []

for n in Nodes:
    print n
    n = ','.join(map(str, n))
    print n
    Temp.append(n)
    g1.node(n, label = n)

g1.edge('1,2,3', '4,5,6')
g1.edge('3,4,5', '1,5,3')

filename = g1.render(filename='img/g1')
