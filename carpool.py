#carpool functions#
import numpy as np
import pandas as pd
import networkx as nx
from scipy.sparse import save_npz load_npz

def initialise():
    nodes = pd.read_csv('uknetworknodes.csv')
    adj_mat = load_npz('adjacency_matrix.npz')
