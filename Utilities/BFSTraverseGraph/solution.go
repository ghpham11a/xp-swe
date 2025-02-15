package main

import (
	"container/list"
	"fmt"
)

type UndirectedGraph struct {
	adjacencyList [][]int
	size		  int
}

func NewUndirectedGraph(size int) *UndirectedGraph {
    adjacencyList := make([][]int, size)
    return &UndirectedGraph{adjacencyList, size}
}

func (self *UndirectedGraph) addEdge(src int, dst int) {
    self.adjacencyList[src] = append(self.adjacencyList[src], dst)
    self.adjacencyList[dst] = append(self.adjacencyList[dst], src)
}

func bfs(graph *UndirectedGraph, node int) []int {
    
    output := make([]int, 0)
    visited := make([]bool, 0)
    for i := 0; i < graph.size; i++ {
        visited = append(visited, false)
    } 
    queue := list.New()
    
    queue.PushBack(node)
    visited[node] = true
    
    for queue.Len() > 0 {
        
        currNode := queue.Front()
        output = append(output, currNode.Value.(int))
        queue.Remove(currNode)
        
        for _, neighbor := range graph.adjacencyList[node] {
            if visited[neighbor] == false {
                queue.PushBack(neighbor)
                visited[neighbor] = true
            }
        }
    } 
    
    return output
}

func main() {
    
    graph := NewUndirectedGraph(4)
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(1, 2)
    graph.addEdge(2, 0)
    graph.addEdge(2, 3)
    graph.addEdge(3, 3)
    
    output := bfs(graph, 2)
    
    for _, num := range output {
        fmt.Println(num)
    }
}