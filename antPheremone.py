#wrapper script#

from max import *
from james import *


#number of ants per step
N = 500

G, nodeList, distMatrix = initialise()

initialNode = np.random.choice(nodeList,1)

print(initialNode)

G = synthetic_network(10)

print(G.edges(data=True))
