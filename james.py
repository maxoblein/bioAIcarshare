#Script for James' functions
from max import *


def distribute_pheremone(routes, nodeList)
    #routes is a list of lists. List of nodes on route

    #pheremone is a nxn matrix number of ants to use edge row x column
    
    n = len(nodeList)
    pheremone = np.zeros(n,n)

    for i in routes:
        for j in range(0,len(i)-1):
            pheremone[i[j],i[j+1]] +=1
                




    return pheremone

def route_scoring(route_length, num_pickups)
    #####MIGHT NEED TO CALCULATE ROUTES####
    ###Need to decide what 'scaling_term' we want trial and error###
    ###constant 'a' to decide how influnetial pick_ups are
    a=1
    scaling_term = 1/(a*num_pickups+1)

    
    route_score = route_length*scaling_term

    return route_score




def choose_node(current_node,potential_next_nodes,goalNode,nodeList, pheremone, distMatrix,strength_pheremone,strength_goal,strength_next)
    #current_node --- 'int'
    #potential_next_nodes ---'list nodes'
    #pheremone --- Matrix equivalent to edges

    distribution = np.array([]) 

    #generate distribution
    ###will need scaling terms###
    for node in potential_next_nodes:
        goaldist = distance_to_goal_node(node,goalNode,nodeList)
        next_node_dist = distMatrix[current_node][node]
        pheremone_weight = pheremone[current_node][node]
        pheremone_weight = 2
        a = (strength_goal*(1/goaldist) + strength_next*(1/next_node_dist))*strength_pheremone*pheremone_weight
        distribution = np.append(distribution,a)
    
    
    normalized_distribution = distribution/sum(distribution)
    normalized_distribution = np.around(normalized_distribution,3)


    next_node = np.random.choice(potential_next_nodes, p=normalized_distribution)

    return next_node


def synthetic_network(n):

    # create n nodes
    nodes = list(range(1, n))
    
    edges = []

    #n random xy coordinates in unit square
    xy = np.random.random((n,2))

    #triangulation over the network
    tri = Delaunay(xy)

    #add three edges of the triangles
    for i in tri.simplices:
        edges.append([i[0],i[1]])
        edges.append([i[0],i[2]])
        edges.append([i[1],i[2]])

    #initialise network
    G=nx.Graph()
    #add nodes
    G.add_nodes_from(nodes)
    #add edges
    ####THINK THIS REMOVES DUPLICATE EDGES####
    G.add_edges_from(edges)

    #add xy coordinates to nodes
    for j in G:
        G.nodes[j]['pos'] = (xy[j][0], xy[j][1])



    ####To plot the network
    #nx.draw(G, pos=nx.get_node_attributes(G, 'pos'))

    ####Find [x,y] of node i 
    #(G.nodes[i]['pos'])

    ####Find edges
    #G.edges
    return G




    
    
