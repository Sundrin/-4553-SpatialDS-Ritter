
import csv
import json

nodes = []
edges = []
geomtry = {}

with open('nodes.csv', 'rb') as csvfile:
  rows = csv.reader(csvfile, delimiter=',', quotechar="")
  for row in rows:
    nodes.append(row) #.append because we need to add more memory as we go, same with edges

with open('edges.csv', 'rb') as csvfile:
  rows = csv.reader(csvfile, delimiter=',', quotechar="")
  for row in rows:
    edges.append(row)

f = open('nodegeometry.json'. 'r')

for line in f:
  line = json.loads(line)
  print line['id']
  geometry[line['id']] = line['geometry']
  
#print len(nodes)
#print len(edges)
geo =  json.loads(geometry[str(203982)])

#edit this to do some things
print len(geo)
