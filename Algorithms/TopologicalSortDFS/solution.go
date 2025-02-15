package main 

import (
	"errors"
	"fmt"
)

type DirectedAcyclicGraph struct {
	adjacencyList [][]int
	size		  int
}

func NewDirectedAcyclicGraph(size int) *DirectedAcyclicGraph {
    adjacencyList := make([][]int, size)
    return &DirectedAcyclicGraph{adjacencyList, size}
}

func (d *DirectedAcyclicGraph) addEdge(src int, dst int) {
    d.adjacencyList[src] = append(d.adjacencyList[src], dst)
}

type Marker int

const (
	Unmarked    Marker = 0
	Temporary   Marker = 1
	Permanent   Marker = 2
)

func topologicalSort(graph *DirectedAcyclicGraph) []int {

	var output []int
	markers := make(map[int]Marker)
	
	for node := 0; node < graph.size; node++ {
	    markers[node] = Unmarked
	}
	
	for node := 0; node < graph.size; node++ {
	    if markers[node] == Unmarked {
	        err := topologicalSortDFS(node, graph, markers, &output)
        	if err != nil {
        	    return make([]int, 0)
        	}
	    }
	}
	
	for i, j := 0, len(output) - 1; i < j; i, j = i + 1, j - 1 {
        output[i], output[j] = output[j], output[i]
    }

	return output
}

func topologicalSortDFS(node int, graph *DirectedAcyclicGraph, markers map[int]Marker, output *[]int) error {
    
    if markers[node] == Permanent {
        return nil
    }
    
    if markers[node] == Temporary {
        return errors.New("Cycle error")
    }
    
    markers[node] = Temporary
    
    for _, neighbor := range graph.adjacencyList[node] {
        err := topologicalSortDFS(neighbor, graph, markers, output)
        if err != nil {
            return err
        }
    }
    
    markers[node] = Permanent
    
    *output = append(*output, node)
    
    return nil
}

func main() {
	graph := NewDirectedAcyclicGraph(7)

	graph.addEdge(0,1)
	graph.addEdge(0,2)
	graph.addEdge(0,5)
	graph.addEdge(1,3)
	graph.addEdge(1,2)
	graph.addEdge(2,3)
	graph.addEdge(2,4)
	graph.addEdge(3,4)
	graph.addEdge(5,4)
	
	result := topologicalSort(graph)
	
	for _, node := range result {
	    fmt.Println(node)
	}
}
