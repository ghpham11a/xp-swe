def solution(nums, target):
    map = {}
    for index, value in enumerate(nums):
        diff = target - value
        if diff in map:
            return [index, map[diff]]
        map[value] = index

test_one = solution([2, 7, 11, 15], 9)
test_two = solution([3, 2, 4], 6)
test_three = solution([3, 3], 6)