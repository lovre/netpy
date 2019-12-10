import os
import warnings
from time import *
import networkx as nx
from cdlib import viz
from cdlib.classes import *
from cdlib import algorithms
from matplotlib import pyplot as plt
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

def kcore(G, k):
  """
  Find and construct k-cores of undirected multigraph G for specified k.
  """
  K = nx.MultiGraph(G)
  K.name = str(k) + '-core'
  change = True
  while change:
    change = False
    for i in list(K.nodes()):
      if K.degree(i) < k:
        K.remove_node(i)
        change = True
  return K

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

def clusters(G, alg):
  """
  Find and print out standard statistics of clusters of undirected multigraph G.
  """
  tic = time()
  print("{0:>15s} | '{1:s}'".format('Graph', G.name.replace('_', '-')))
  comms = alg(G)
  print("{0:>15s} | '{1:s}'".format('Algorithm', comms.method_name.lower()))
  print("{0:>15s} | {1:,d} ({2:.1f})".format('Count', len(comms.communities), G.number_of_nodes() / len(comms.communities)))
  print("{0:>15s} | {1:.1f} ({2:.1f}%)".format('Degree', comms.average_internal_degree().score, 100.0 * comms.average_internal_degree().score * G.number_of_nodes() / G.number_of_edges() / 2.0))
  print("{0:>15s} | {1:.6f}".format('Q', comms.erdos_renyi_modularity().score))
  truths = {}
  for node in G.nodes(data = True):
    cluster = node[1]['cluster'] if 'cluster' in node[1] else 0
    if cluster not in truths:
      truths[cluster] = []
    truths[cluster].append(node[0])
  truths = NodeClustering(list(truths.values()), G, 'truth')
  print("{0:>15s} | {1:.6f}".format('NMI', comms.normalized_mutual_information(truths).score))
  print("{0:>15s} | {1:.6f}".format('ARI', comms.adjusted_rand_index(truths).score))
  print("{0:>15s} | {1:.1f} sec\n".format('Time', time() - tic))
  return comms

def kcores(G):
  """
  Find and print out largest k-core of undirected multigraph G.
  """
  tic = time()
  print("{0:>15s} | '{1:s}'".format('Graph', G.name.replace('_', '-')))
  k = 1
  Ks = []
  K = nx.MultiGraph(G)
  while True:
    K = kcore(K, k)
    if K.number_of_nodes() == 0:
      break
    Ks.append(K)
#    Cs = sorted(nx.connected_component_subgraphs(K), key = len, reverse = True)
#    print("{0:>15s} | {1:,d} ({2:,d})".format(K.name, Cs[0].number_of_nodes(), len(Cs)))
    k += 1
  Cs = sorted(nx.connected_component_subgraphs(Ks[-1]), key = len, reverse = True)
  print("{0:>15s} | {1:,d} ({2:,d})".format(Ks[-1].name, Cs[0].number_of_nodes(), len(Cs)))
  print("{0:>15s} | {1:.1f} sec\n".format('Time', time() - tic))
  return Ks

tic = time()

for file in ['karate', 'women', 'dolphins']:

  # Constructs a graph of real network

  G = read(file)

  # Prints out statistics of real network

  info(G)

  # Finds community structure of real network

#  comms = clusters(G, lambda G: algorithms.louvain(G))
#  comms = clusters(G, lambda G: algorithms.label_propagation(G))
  comms = clusters(G, lambda G: algorithms.girvan_newman(G, level = 1))

  # Visualizes community structure of real network

#  viz.plot_network_clusters(G, comms, nx.spring_layout(G))
#  plt.show()

for file in ['got-appearance', 'diseasome', 'wars', 'transport', 'java', 'imdb', 'wikileaks']:

  # Constructs a graph of real network

  G = read(file)

  # Prints out statistics of real network

  info(G)

  # Finds community structure of real network

  comms = clusters(G, lambda G: algorithms.louvain(G))
#  comms = clusters(G, lambda G: algorithms.label_propagation(G))
#  comms = clusters(G, lambda G: algorithms.girvan_newman(G, level = 1))

  # Print out largest community of real network

  print(sorted(comms.communities, key = len, reverse = True)[0])
  print()

for k in range(5, 25, 5):

  # Constructs Erdös-Rényi random graph

  G = nx.gnm_random_graph(10000, 5000 * k)
  G.name = 'Erdös-Rényi'

  # Prints out statistics of random graph

  info(G)

  # Finds community structure of random graph

#  clusters(G, lambda G: algorithms.louvain(G))
  clusters(G, lambda G: algorithms.label_propagation(G))
#  clusters(G, lambda G: algorithms.girvan_newman(G, level = 1))

for file in ['got-appearance', 'diseasome', 'wars', 'transport', 'java', 'imdb', 'wikileaks']:

  # Constructs a graph of real network

  G = read(file)
  
  # Prints out statistics of real network

  info(G)
  
  # Finds k-core decomposition of real network

  Ks = kcores(G)
  
  # Prints out largest k-core of real network
  
  print(Ks[-1].nodes())
  print()

print("{0:>15s} | {1:.1f} sec\n".format('Total', time() - tic))
