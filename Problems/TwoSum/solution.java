import java.util.HashMap;

class TwoSum {

    public static void main(String[] args) {
        int[] testOne = solution(new int[]{2, 7, 11, 15}, 9);
        int[] testTwo = solution(new int[]{3, 2, 4}, 6);
        int[] testThree = solution(new int[]{3, 3}, 6);
    }

    public static int[] solution(int[] nums, int target) {

        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length; i++) {
            int diff = target - value;
            if (map.containsKey(diff)) {
                return new int[]{i, map.get(diff)};
            }
            map.put(nums[i], i);
        }

        return new int[]{};
    }
}