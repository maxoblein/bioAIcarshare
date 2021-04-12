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
    adjMat = pd.read_csv('pandasedgelist.csv',low_memory=False)


    G = nx.from_pandas_edgelist(adjMat,edge_attr = 'length',create_using=nx.MultiDiGraph)
    G.update(nodes=nodeList) # adds node info

    distMatrix = nx.linalg.graphmatrix.adjacency_matrix(G,weight='length')
    distMatrix = distMatrix.toarray()

    return G, nodeList, distMatrix

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

    distance = R * c * 1000

    return distance

def get_uniform_dist(potentialNextNodes):
    #placeholder function until james does his
    n = len(potentialNextNodes)

    distribution = [1/n for i in range(n)]


    return distribution

def update_ant_position(currentNode,goalNode,nodeList,distMatrix):
    # Get row of distance matrix corresponding to current node
    distVector = distMatrix[currentNode,:]

    #retrieve indices of all potential next nodes
    potentialNextNodes = np.argwhere(distVector)
    potentialNextNodes = [x[0] for x in potentialNextNodes]

    #form probability vector for potential next nodes

    ##NEED JAMES PROBABILITY FUNCTION##
    distribuion = get_uniform_dist(potentialNextNodes)

    #choose next node from potential next nodes according to probability distribuion
    nextNode = np.random.choice(potentialNextNodes)

    return nextNode

def distribute_passengers(numberPassengers,nodeList):
    indices = np.arange(len(nodeList))
    print(indices)
    passengerNodes = np.random.choice(indices,numberPassengers)

    for i in passengerNodes:
        nodeList[i][-1]['passenger'] = True

    return nodeList








if __name__ == '__main__':
    G, nodeList, distMatrix = initialise()

    #number of ants per iteration
    N = 500

    ##CHOOSE INITIAL NODE AND GOAL NODE##
    passengerNodeList = distribute_passengers(20,nodeList)

    print(passengerNodeList)
    #
