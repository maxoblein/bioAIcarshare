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


    # next_node = np.random.choice(potential_next_nodes, p=normalized_distribution)

    return normalized_distribution
