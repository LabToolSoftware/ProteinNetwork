import numpy as np
import pandas as pd
import networkx as nx
from networkx.algorithms import community
from tkinter import filedialog
import matplotlib.pyplot as plt

def loadFile(sep=','):
    with filedialog.askopenfile() as file:
        df = pd.read_csv(file,sep=sep)
    return df

def constructGraph(df):
    P = nx.Graph()
    P.add_nodes_from(df.node1)
    nodes = [(entry[0],entry[1],entry[2]) for ind, entry in df.loc[:,['node1','node2','combined_score']].iterrows()]
    P.add_weighted_edges_from(nodes)
    return P

def findCommunities(G):
    communities = community.centrality.girvan_newman(G)
    return communities

df = loadFile(sep='\t')
P = constructGraph(df)
comm_graphs = []

for c in next(findCommunities(P)):
    C = nx.Graph()
    for node in c:
        print(c)

