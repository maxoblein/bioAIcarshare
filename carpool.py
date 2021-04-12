#carpool functions#
import numpy as np
import pandas as pd
import networkx as nx
from scipy.sparse import save_npz, load_npz

def nodes_from_csv(path):
    df = pd.read_csv(path, index_col=0)
    nodes = []

    for ix , row in df.iterrows():
        d = dict(row)
        node = d.pop('node')
        nodes.append((node, {k:v for k,v in d.items() if v}))

    return nodes

def initialise():
    nodes = nodes_from_csv('uknetworknodes.csv')
    adj_mat = pd.read_csv('pandasedgelist.csv')


    G = nx.from_pandas_edgelist(adj_mat,edge_attr = 'length',create_using=nx.MultiDiGraph)
    G.update(nodes=nodes) # adds node info


    return G, nodes




if __name__ == '__main__':
    G,nodes = initialise()
