import os
from time import *
import numpy as np
import networkx as nx
from random import sample
import matplotlib.pyplot as plt

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
  print("{0:>15s} | {1:,d}".format('Nodes', G.number_of_nodes()))
  print("{0:>15s} | {1:,d}".format('Edges', G.number_of_edges()))
  print("{0:>15s} | {1:.1f} sec\n".format('Timing', time() - tic))

G = nx.MultiGraph(name = 'toy')
G.add_node(1)
G.add_node(2)
G.add_edge(1, 2)

info(G)
