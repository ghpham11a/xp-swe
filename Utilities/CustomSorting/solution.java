import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.Collections;
import java.util.Arrays;

class Officer {
    String rank;
    Officer(String rank) {
        this.rank = rank;
    }
}

class Solution {
    
    private static Map<String, Integer> ranks  = new HashMap<String, Integer>() {{
        put("2LT", 1);
        put("1LT", 2);
        put("CPT", 3);
        put("MAJ", 4);
        put("LTC", 5);
        put("COL", 6);
    }};
    
    private static Comparator<Officer> comparator =
        new Comparator<Officer>() {
            @Override
            public int compare(Officer x, Officer y) {
                return ranks.get(x.rank) - ranks.get(y.rank);
            }
        };
    
    public static void main(String[] args) {
        
        Officer[] objects = new Officer[] { 
            new Officer("CPT"),
            new Officer("MAJ"),
            new Officer("2LT"),
            new Officer("COL"),
            new Officer("LTC"),
            new Officer("1LT")
        };
        
        Arrays.sort(objects, comparator);
        
        for (Officer object : objects) {
            System.out.println(object.rank);
        }

        // 2LT
        // 1LT
        // CPT
        // MAJ
        // LTC
        // COL
    }
}