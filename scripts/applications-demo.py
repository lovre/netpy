import os
import warnings
from time import *
import networkx as nx
from cdlib import viz
from cdlib.classes import *
from cdlib import algorithms
from random import sample

warnings.filterwarnings('ignore')

def read(file, path = '../nets'):
  """
  Construct undirected multigraph G from specified file in Pajek format.
  """
  G = nx.MultiGraph(name = file)
  with open(os.path.join(path, file + '.net'), 'r') as file:
    nodes = {}
    for line in file:
      if line.startswith('*vertices'):
        continue
      elif line.startswith('*edges') or line.startswith('*arcs'):
        break
      else:
        node = line.strip().split('"')
        nodes[node[0].strip()] = node[1]
        G.add_node(node[1], id = int(node[0]), cluster = int(node[2]) - 1 if len(node[2]) > 0 else 0)
    for line in file:
      edge = line.strip().split(' ')
      G.add_edge(nodes[edge[0]], nodes[edge[1]])
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
  print("{0:>15s} | {1:.1f} ({2:,d}, {3:,d})".format('Degree', 2.0 * G.number_of_edges() / G.number_of_nodes(), min(ks), max(ks)))
  print("{0:>15s} | {1:.8f}".format('Density', 2.0 * G.number_of_edges() / G.number_of_nodes() / (G.number_of_nodes() - 1.0)))
  CCs = sorted(nx.connected_component_subgraphs(G), key = len, reverse = True)
  print("{0:>15s} | {1:.1f}% ({2:,d})".format('Components', 100.0 * CCs[0].number_of_nodes() / G.number_of_nodes(), len(CCs)))
  d, D = dists(CCs[0])
  print("{0:>15s} | {1:.3f} ({2:,d})".format('Distances', d, D))
  print("{0:>15s} | {1:.6f}".format('Clustering', nx.average_clustering(nx.Graph(G))))
  print("{0:>15s} | {1:.1f} sec\n".format('Time', time() - tic))

tic = time()

for file in ['karate', 'java']:

  # Constructs a graph of real network

  G = read(file)

  # Prints out statistics of real network

  info(G)

  # Computes node centralities of real network

  g = nx.Graph(G)
  prs = nx.pagerank(g)
  cs = nx.clustering(g)

  dcs = nx.degree_centrality(G)
  ccs = nx.closeness_centrality(G)
  bcs = nx.betweenness_centrality(G)

  # Finds community structure of real network
  
  c = 0
  comms = {}
  for comm in algorithms.louvain(G).communities:
    for i in comm:
      comms[i] = c
    c += 1

  # Writes node features to tab-separated file

  with open(os.path.join('../nets', file + '.tab'), 'w') as file:
    file.write("m#id\tm#node\tC#dc\tC#cc\tC#bc\tC#pr\tC#c\tD#community\tcD#class\n")
    for node in G.nodes(data = True):
      file.write("{:d}\t{:s}\t{:f}\t{:f}\t{:f}\t{:f}\t{:f}\t{:d}\t{:d}\n".format(node[1]['id'], node[0], dcs[node[0]], ccs[node[0]], bcs[node[0]], prs[node[0]], cs[node[0]], comms[node[0]], node[1]['cluster']))

print("{0:>15s} | {1:.1f} sec\n".format('Total', time() - tic))
