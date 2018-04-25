""" There are a row of n houses, each house can be painted with one of the three colors: red, blue or green."""
""" The cost of painting each house with a certain color is different. """
""" You have to paint all the houses such that no two adjacent houses have the same color."""

""" The cost of painting each house with a certain color is represented by a n x 3 cost matrix. """
""" For example, costs[0][0] is the cost of painting house 0 with color red;"""
""" costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses."""
def Paint_house(costs):
    """
    :param costs: n*3 matrix, 3 -- 3 colors, n = number of house
    :return: min cost for paint n house

    """
    if(costs.empty() or costs[0].empty):
        return 0

    pcosts=costs
    for i in range(1,pcosts.size):
        for j in range(3):
            pcosts[i][j] += min(pcosts[i-1][(j+1)%3],pcosts[i-1][(j+2)%3])
    
    return min(pcosts[len(costs)-1])
