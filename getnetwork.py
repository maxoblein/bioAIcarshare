#Python script to import osmnx as build a network structure of bristol and the south west#
import numpy as np
import pandas as pd
import osmnx as ox
import networkx as nx
from scipy.sparse import save_npz

def download_graphml():
    ox.utils.config(use_cache=True, log_console=True,timeout=10000)



    G = ox.graph_from_place('England', network_type='drive', custom_filter='["highway"~"motorway|primary|secondary"]')

    #|primary|secondary

    stats = ox.stats.basic_stats(G)

    print(stats)

    #fig, ax = ox.plot_graph(G,node_size = 5)


    ox.io.save_graphml(G, filepath='ukstreetnetwork', gephi=False, encoding='utf-8')

def nodes_to_csv(G, savepath):
    unpacked = [pd.DataFrame({**{'node': node, **data}}, index=[i]) for i, (node, data) in enumerate(G.nodes(data=True))]
    df = pd.concat(unpacked)
    df.to_csv(savepath)
    return df

def nodes_from_csv(path):
    df = pd.read_csv(path, index_col=0)
    nodes = []

    for ix , row in df.iterrows():
        d = dict(row)
        node = d.pop('node')
        nodes.append((node, {k:v for k,v in d.items() if v}))

    return nodes

def export_data():
    G = ox.io.load_graphml('ukstreetnetwork')

    nodes_to_csv(G, 'uknetworknodes.csv')

    # adj_mat = nx.linalg.graphmatrix.adjacency_matrix(G,weight='length')
    # print(adj_mat)
    #
    # save_npz('adjacency_matrix',adj_mat)

    adj_matrix = nx.to_pandas_edgelist(G)
    adj_matrix.to_csv('pandasedgelist.csv')


if __name__ == '__main__':
    export_data()
