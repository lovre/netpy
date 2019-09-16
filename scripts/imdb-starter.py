import os
from time import *
import networkx as nx
from random import sample

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
  CCs = sorted(nx.connected_component_subgraphs(G), key = len, reverse = True)
  print("{0:>15s} | {1:.1f}% ({2:,d})".format('Components', 100.0 * CCs[0].number_of_nodes() / G.number_of_nodes(), len(CCs)))
  d, D = dists(CCs[0])
  print("{0:>15s} | {1:.3f} ({2:,d})".format('Distances', d, D))
  print("{0:>15s} | {1:.6f}".format('Clustering', nx.average_clustering(nx.Graph(G))))
  print("{0:>15s} | {1:.1f} sec\n".format('Timing', time() - tic))

G = read('toy')
# G = read('karate')
# G = read('women')
# G = read('lpp')
# G = read('imdb')

info(G)
