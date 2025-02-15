package main
import (
    "fmt"
    "math"
)

func solution(s string) int {
    seenChars := make(map[rune]int)
    left := 0
    result := 0
    
    for right, currentChar := range s {
        if dictValue, ok := seenChars[currentChar]; ok && dictValue >= left {
            left = dictValue + 1
        } else {
            result = int(math.Max(float64(result), float64(right - left + 1)))
        }
        seenChars[currentChar] = right
    }
    
    return result
}

func main() {
  testOne := solution("abcbba")
  fmt.Println(testOne)
}