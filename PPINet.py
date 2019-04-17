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

def constructNetwork(df,node1_colname,node2_colname,weighted_by=None):
    P = nx.Graph()
    P.add_nodes_from(df.node1)
    if weighted_by == None:
        nodes = [(entry[0], entry[1]) for ind, entry in
                 df.loc[:, [node1_colname, node2_colname]].iterrows()]
    else:
        nodes = [(entry[0], entry[1], entry[2]) for ind, entry in
                 df.loc[:, [node1_colname, node2_colname, weighted_by]].iterrows()]
    P.add_weighted_edges_from(nodes)
    return P

def findCommunities(G):
    communities = community.centrality.girvan_newman(G)
    return communities


if __name__ == '__main__':
    df = loadFile(sep='\t')
    print(df.head())
    P = constructNetwork(df,'node1','node2','combined_score')
    communities = findCommunities(P)

    comm_graphs = []
    for c in next(communities):
        C = nx.Graph()
        print([entry[1] for node in list(c) for entry in df[df['node1']==node].iterrows()])
        comm_graphs.append(C)