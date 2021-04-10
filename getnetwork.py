#Python script to import osmnx as build a network structure of bristol and the south west#
import numpy as np
import pandas as pd
import osmnx as ox

ox.utils.config(use_cache=True, log_console=True,timeout=10000)



G = ox.graph_from_place('England', network_type='drive', custom_filter='["highway"~"motorway|primary|secondary"]')

#|primary|secondary

stats = ox.stats.basic_stats(G)

print(stats)

fig, ax = ox.plot_graph(G,node_size = 5)


ox.io.save_graphml(G, filepath='ukstreetnetwork', gephi=False, encoding='utf-8')
