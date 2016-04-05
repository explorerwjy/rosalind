# -*- coding: utf-8 -*-
"""
Completing a Tree
Given: A positive integer nn (n≤1000n≤1000) and an adjacency list corresponding to a graph on n nodes that contains no cycles.
Return: The minimum number of edges that can be added to the graph to produce a tree.
Solution: Judge the number of connected component from a undirected graph.
"""
from sys import argv

class TREE:
	#Graph Represented Using Adjacency Sets
	def __init__(self,num,adjacencylist):
		self.adjacencyset = {}	#adjacencyset
		self.nodes = [x for x in range(1,num+1)] #nodes list
		self.addadjacency(adjacencylist) #complete adjacencyset

	def addadjacency(self,adjacencylist):
		for i in self.nodes:
			self.adjacencyset[i] = set([])
		for i in adjacencylist:
			self.adjacencyset[i[0]].add(i[1])
			self.adjacencyset[i[1]].add(i[0])

	def walk(self,s,S=set()): #walk througth a graph from node s
		G = self.adjacencyset
		P,Q = dict(),set() # P:Predecessors Q:nodes needs to reach
		P[s] = None
		Q.add(s) #start with s
		while Q:
			u = Q.pop() #randomly pick one
			for v in G[u].difference(P,S): #new nodes?
				Q.add(v) #plan to reach
				P[v] = u #where we come from
		return P # The traversal tree

	def components(self):
		comp = []
		seen = set() #nodes we have seen
		G = self.adjacencyset
		for u in G:
			if u in seen:
				continue
			C = self.walk(u)
			seen.update(C)
			comp.append(C)
		return comp


	def tree(self): #Find how many connected component in graph
		return len(self.components())-1

if __name__ == '__main__':
	small_input = "test.txt"
	large_input = 'D:/Study/rosalind_data/rosalind_tree.txt'
	handle = open(small_input,'r')
	handle = open(large_input,'r')
	num = int(handle.readline().strip())
	adjacencylist = [map(int,nodes.split()) for nodes in handle.read().split('\n')]
	print adjacencylist
	sol = TREE(num,adjacencylist)
	print sol.nodes
	print sol.adjacencyset
	print sol.components()
	print sol.tree()
