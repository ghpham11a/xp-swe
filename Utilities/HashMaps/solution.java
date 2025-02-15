import java.util.HashMap;
import java.util.Map;

class Solution {

    public static void main(String[] args) {
        
        // Create HashMap
        HashMap<String, Integer> map = new HashMap<>();
        
        // Add to HashMap
        map.put("ALPHA", 10);
        map.put("BRAVO", 20);
        map.put("CHARLIE", 30);
        
        // Check if HashMap contains key
        if (map.containsKey("ALPHA")) {
            
        }
        
        // Get value from HashMap
        int value = map.get("ALPHA");
        
        // Delete key from HashMap
        int value = (int)map.remove("ALPHA");
        
        // Iterate through keys in HashMap
        for (String key : map.keySet()) {
            
        }
        
        // Iterate through values in HashMap
        for (int value : map.values()) {
            
        }
        
        // Iterate through keys and values in HashMap
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            String key = entry.getKey();
            int value = entry.getValue();
            System.out.println(key + " => " + value);
        }
    }
}