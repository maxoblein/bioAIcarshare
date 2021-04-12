#carpool functions#
import numpy as np
import pandas as pd
import networkx as nx
from scipy.sparse import save_npz, load_npz
from math import sin, cos, sqrt, atan2, radians
from james import *


def nodes_from_csv(path):
    df = pd.read_csv(path, index_col=0)
    nodes = []

    for ix , row in df.iterrows():
        d = dict(row)
        node = d.pop('node')
        nodes.append((node, {k:v for k,v in d.items() if v}))

    return nodes

def initialise():
    nodeList = nodes_from_csv('uknetworknodes.csv')
    adjMat = pd.read_csv('pandasedgelist.csv')


    G = nx.from_pandas_edgelist(adjMat,edge_attr = 'length',create_using=nx.MultiDiGraph)
    G.update(nodes=nodeList) # adds node info


    return G, nodeList

def distance_to_goal_node(currentNode,goalNode,nodeList):

    currentNodeDict = nodeList[currentNode][-1]
    goalNodeDict = nodeList[goalNode][-1]

    xCurrent = currentNodeDict['x']
    yCurrent = currentNodeDict['y']
    xGoal = goalNodeDict['x']
    yGoal = goalNodeDict['y']

    # approximate radius of earth in km
    R = 6373.0

    latCurrent = radians(yCurrent)
    lonCurrent = radians(xCurrent)
    latGoal = radians(yGoal)
    lonGoal = radians(xGoal)

    dlon = lonGoal - lonCurrent
    dlat = latGoal - latCurrent

    a = sin(dlat / 2)**2 + cos(latCurrent) * cos(latGoal) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance




if __name__ == '__main__':
    G,nodeList = initialise()

    distance_to_goal_node(2,5,nodeList)
