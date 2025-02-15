package main

import (
    "fmt"
)

func binarySearch(target int, nums []int) int {
    lo := 0
    hi := len(nums) - 1

    for lo <= hi {
        mid := lo + (hi - lo) / 2

        if nums[mid] == target {
            return mid
        }

        if nums[mid] < target {
            lo = mid + 1
        }

        if nums[mid] > target {
            hi = mid - 1
        }
    }

    return -1
}

func main() {
    result := binarySearch(3, []int{2, 3, 4, 10, 40})
    if result == -1 {
        fmt.Println("FAIL")
    } else {
        fmt.Println("PASS")
    }
}