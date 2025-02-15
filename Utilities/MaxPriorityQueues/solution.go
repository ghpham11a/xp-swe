package main

import (
    "container/heap"
    "fmt"
)

type PriorityQueue []int

func (h PriorityQueue) Len() int { 
	return len(h) 
}
func (h PriorityQueue) Less(i, j int) bool { 
	return h[i] < h[j] 
}
func (h PriorityQueue) Swap(i, j int) { 
	h[i], h[j] = h[j], h[i] 
}
func (h *PriorityQueue) Push(x interface{}) {
    *h = append(*h, x.(int))
}
func (h *PriorityQueue) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[0 : n-1]
    return x
}

func main() {
	
    pq := &PriorityQueue{-2, -1, -5}
    heap.Init(pq)

    heap.Push(pq, -3)

    fmt.Println(-1 * heap.Pop(pq).(int))
    fmt.Println(-1 * heap.Pop(pq).(int))
    fmt.Println(-1 * heap.Pop(pq).(int))
    fmt.Println(-1 * heap.Pop(pq).(int))
}