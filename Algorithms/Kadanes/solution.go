package main

import (
	"fmt"
	"math"
)

func kadanes(nums []int) int {
	bestSum := math.Inf(-1)
	currSum := 0.0

	for _, num := range nums {
		currSum = math.Max(float64(num), currSum + float64(num))
		bestSum = math.Max(bestSum, currSum)
	}

	return int(bestSum)
}

func main() {
    nums := []int{-2, -3, 4, -1, -2, 1, 5, -3}
    result := kadanes(nums)
    fmt.Println(result)
}