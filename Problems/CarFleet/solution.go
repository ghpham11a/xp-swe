package main

import "fmt"
import "sort"

func carFleet(target int, position []int, speed []int) int {

    var pair [][]int
    var stack []float64

    for index, _ := range position {
        pair = append(pair, []int{ position[index], speed[index] })
    }

	sort.Slice(pair, func(p, q int) bool {  
        return pair[p][0] < pair[q][0] 
    }) 

    for i, j := 0, len(pair) - 1; i < j; i, j = i + 1, j - 1 {
        pair[i], pair[j] = pair[j], pair[i]
    }

    for _, pAndS := range pair {
        stack = append(stack, (float64(target) - float64(pAndS[0])) / float64(pAndS[1]))
        if len(stack) >= 2 && stack[len(stack) - 1] <= stack[len(stack) - 2] {
            stack = stack[:len(stack) - 1]
        }
    }

    return len(stack)
}

func main() {
    result := carFleet(12, []int{10, 8, 0, 5, 3}, []int{2, 4, 1, 1, 3})
    if result != 3 {
        fmt.Println("FAIL")
    } else {
        fmt.Println("PASS")
    }
}