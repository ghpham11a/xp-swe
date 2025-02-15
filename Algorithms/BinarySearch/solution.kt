fun binarySearch(target: Int, nums: List<Int>): Int {
    var lo = 0 
    var hi = nums.size - 1
    
    while (lo <= hi) {
        
        var mid = lo + (hi - lo) / 2
        
        if (nums[mid] == target) {
            return mid
        }
        
        if (nums[mid] < target) {
            lo = mid + 1
        }
        
        if (nums[mid] > target) {
            hi = mid - 1
        }
        
    }
    
    return -1
    
}

fun main() {
   
    assert(binarySearch(3, listOf(2, 3, 4, 10, 40)) == 1)
    
    println("PASS")
}