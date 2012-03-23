'''
Created on 17/05/2010

@author: lporras
'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
 
Infinity = float("inf")
 
def IDA_star():
    cost_limit = heuristics[rootNode]
 
    while True:
        (solution, cost_limit) = DFS(0, rootNode, cost_limit, [rootNode])
        if solution != None: return (solution, cost_limit)
        if cost_limit == Infinity: return None
 
# returns (solution-sequence or None, new cost limit)
def DFS(start_cost, node, cost_limit, path_so_far):
    print "start_cost:", start_cost, ", node:", node, ", cost_limit:", cost_limit, ", path_so_far:", path_so_far
 
    minimum_cost = start_cost + heuristics[node]
    print "  minimum_cost:", minimum_cost
    if minimum_cost > cost_limit: return (None, minimum_cost)
    if node in goalNodes: return (path_so_far, cost_limit)
 
    next_cost_limit = Infinity
    for succNode in successors[node]:
        newStartCost = start_cost + edgeCosts[(node,succNode)]
        (solution, new_cost_limit) = DFS(newStartCost, succNode, cost_limit, path_so_far + [succNode])
        if solution != None: return (solution, new_cost_limit)
        next_cost_limit = min(next_cost_limit, new_cost_limit)    
 
    return (None, next_cost_limit)
 
 
 
# search space and problem definition
 
rootNode = 0
nodes = set([0,1,2,3])
successors = {0:[1,2,3], 1:[2], 2:[3], 3:[]}
edgeCosts = {(0,1):4, (0,2):5, (0,3):50, (1,2):20, (2,3):1}
heuristics = {0:5, 1:6, 2:1, 3:0}
goalNodes = set([ x for x in heuristics if heuristics[x] == 0 ])
 
print "rootNode:", rootNode
print "nodes:", nodes
print "successors:", successors
print "edgeCosts:", edgeCosts
print "heuristics:", heuristics
print "goalNodes:", goalNodes
 
print "result:", IDA_star()