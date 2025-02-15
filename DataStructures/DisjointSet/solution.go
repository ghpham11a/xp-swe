package main

import "fmt"

type DisjointSet struct {
	parent	[]int
	rank 	[]int 
}

func NewDisjointSet(size int) *DisjointSet {
	parent := make([]int, 0)
	rank := make([]int, 0)
	for i := 0; i < size; i++ {
		parent = append(parent, i)
		rank = append(rank, 1)
	}
	return &DisjointSet{parent, rank}
}

func (self *DisjointSet) find(node int) int {
	if self.parent[node] == node {
	    self.parent[node] = self.parent[self.parent[node]]
		return self.parent[node]   
	}
	return self.find(self.parent[node])
}

func (self *DisjointSet) union(nodeA int, nodeB int) bool {
    
    rootA := self.find(nodeA)
    rootB := self.find(nodeB)
    
    if rootA == rootB {
        return false
    }
    
    if self.rank[rootA] > self.rank[rootB] {
        self.parent[rootB] = rootA
        self.rank[rootA] += self.rank[rootB]
    } else {
        self.parent[rootA] = rootB
        self.rank[rootB] += self.rank[rootA]
    }

	return true
}

func main() {
    ds := NewDisjointSet(9)
    
    edges := [][]int{{0,2},{1,4},{1,5},{2,3},{2,7},{4,8},{5,8}}
    
    for _, edge := range edges {
        ds.union(edge[0], edge[1])
    }
    
    fmt.Println(ds.parent)
}




