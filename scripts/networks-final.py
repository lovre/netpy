import os
from time import *
import numpy as np
import networkx as nx
from random import sample
import matplotlib.pyplot as plt

def read(file, path = '../nets'):
  """
  Construct undirected multigraph G from specified file in Pajek format.
  """
  G = nx.read_pajek(os.path.join(path, file + '.net'))
  G.name = file
  return G

def dists(G, n = 100):
  """
  Compute approximate average distance and diameter of undirected multigraph G.
  """
  ds = []
  for i in G.nodes() if len(G) <= n else sample(G.nodes(), n):
    ds.extend([d for d in nx.shortest_path_length(G, source = i).values() if d > 0])
  return sum(ds) / len(ds), max(ds)

def info(G):
  """
  Compute and print out standard statistics of undirected multigraph G.
  """
  tic = time()
  print("{0:>15s} | '{1:s}'".format('Graph', G.name.replace('_', '-')))
  multi = False
  for edge in G.edges():
    if G.number_of_edges(edge[0], edge[1]) > 1:
      multi = True
      break
  print("{0:>15s} | '{1:s}'".format('Type', '===' if multi else '---'))
  print("{0:>15s} | {1:,d} ({2:,d})".format('Nodes', G.number_of_nodes(), nx.number_of_isolates(G)))
  print("{0:>15s} | {1:,d} ({2:,d})".format('Edges', G.number_of_edges(), nx.number_of_selfloops(G)))
  ks = [k for _, k in G.degree()]
  print("{0:>15s} | {1:.1f} ({2:,d}, {3:,d})".format('Degrees', 2.0 * G.number_of_edges() / G.number_of_nodes(), min(ks), max(ks)))
  print("{0:>15s} | {1:.8f}".format('Density', 2.0 * G.number_of_edges() / G.number_of_nodes() / (G.number_of_nodes() - 1.0)))
  CCs = sorted(nx.connected_component_subgraphs(G), key = len, reverse = True)
  print("{0:>15s} | {1:.1f}% ({2:,d})".format('Components', 100.0 * CCs[0].number_of_nodes() / G.number_of_nodes(), len(CCs)))
  d, D = dists(CCs[0])
  print("{0:>15s} | {1:.3f} ({2:,d})".format('Distances', d, D))
  print("{0:>15s} | {1:.6f}".format('Clustering', nx.average_clustering(nx.Graph(G))))
  print("{0:>15s} | {1:.1f} sec\n".format('Timing', time() - tic))

# G = nx.MultiGraph(name = 'toy')
# G.add_node(1)
# G.add_node(2)
# G.add_node('foo')
# G.add_node('bar')
# G.add_node('baz')
# G.add_edge(1, 2)
# G.add_edge(1, 'foo')
# G.add_edge(2, 'foo')
# G.add_edge('foo', 'bar')

# G = read('toy')
# G = read('karate')
# G = read('women')
# G = read('dolphins')
# G = read('ingredients')
# G = read('darknet')
G = read('ppi')
# G = read('internet')
# G = read('amazon')
# G = read('aps')
# G = read('google')
# G = read('texas')

G = nx.gnm_random_graph(G.number_of_nodes(), G.number_of_edges())
G.name = 'random'

info(G)

(cs, ks) = np.histogram([G.degree(i) for i in G.nodes()], bins = 100)
plt.loglog(ks[:-1], cs, '*')
plt.ylabel('Number of nodes')
plt.xlabel('Node degree')
plt.show()
