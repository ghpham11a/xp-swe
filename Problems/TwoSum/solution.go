package main
import "fmt"

func solution(nums []int, target int) []int {
	dict := make(map[int]int)
	for index, value := range nums {
		var diff = target - value
		if dictValue, ok := dict[diff] {
			return []int{index, dictValue}
		}
		dict[value] = index
	}
	return []int{}
}

func main() {
	testOne := solution([]int{2, 7, 11, 15}, 9)
	fmt.Println(testOne)

	testTwo := solution([]int{3, 2, 4}, 6)
	fmt.Println(testOne)

	testThree := solution([]int{3, 3}, 6)
	fmt.Println(testThree)
}