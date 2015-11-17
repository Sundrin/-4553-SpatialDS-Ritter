import csv
import json

nodes = []
edges = []

with open('nodes.csv', 'rb') as csvfile:
  rows = csv.reader(csvfile, delimiter=',', quotechar="")
  for row in rows:
    nodes.append(row)

with open('edges.csv', 'rb') as csvfile:
  rows = csv.reader(csvfile, delimiter=',', quotechar="")
  for row in rows:
    nodes.append(row)

