package main

import (
    "fmt"
    "math"
    "strings"
)

func buildGraph(graph map[string][]string, words []string) bool {

    for _, word := range words {
        for _, c := range word {
            graph[string(c)] = make([]string, 0)
        }
    }
    
    for i := 0; i < len(words) - 1; i++ {
        word := words[i]
        nextWord := words[i + 1]
        minWordSize := int(math.Min(float64(len(word)), float64(len(nextWord))))
        didBreak := false
        
        for j := 0; j < minWordSize; j++ {
            
            var wordChar string
            var nextWordChar string
            
            if j < len(word) {
                wordChar = string(word[j])
            }
            if j < len(nextWord) {
                nextWordChar = string(nextWord[j])
            }
            
            if !didBreak && wordChar != nextWordChar {
                graph[wordChar] = append(graph[wordChar], nextWordChar)
                didBreak = true
                break
            }
        }
        
        if !didBreak && len(nextWord) < len(word) {
            return false
        }
    }
    
    return true
}

func alienOrder(words []string) string {
    
    graph := make(map[string][]string)
    output := make([]string, 0)
    
    if !buildGraph(graph, words) {
        return ""
    }
    
    seen := make(map[string]bool)

    for node, _ := range graph {
        result := dfs(graph, seen, &output, node)
        if !result {
            return ""
        }
	}

    for i, j := 0, len(output) - 1; i < j; i, j = i + 1, j - 1 {
        output[i], output[j] = output[j], output[i]
    }

    return strings.Join(output, "")
}

func dfs(graph map[string][]string, seen map[string]bool, output *[]string, node string) bool {

    if val, ok := seen[node]; ok {
        return val
	}

    seen[node] = false 
    for _, nextNode := range graph[node] {
        result := dfs(graph, seen, output, nextNode)
        if !result {
            return false
        }
    }
    seen[node] = true
    *output = append(*output, node)

    return true
}

func main() {
 
    words := []string{"wrt","wrf","er","ett","rftt"}
    output := alienOrder(words)
    
    fmt.Println(output)
}