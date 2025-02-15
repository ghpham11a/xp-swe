import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Arrays;
import java.util.List;
import java.util.Collections;
import java.util.Comparator;

class WeightedEdge {
    int node;
    int weight;
    
    WeightedEdge(int node, int weight) {
        this.node = node;
        this.weight = weight;
    }
}

class UndirectedWeightedGraph {
    
    int size;
    List<List<WeightedEdge>> adjacencyList;
    
    UndirectedWeightedGraph(int size) {
        this.size = size;
        this.adjacencyList = new ArrayList<List<WeightedEdge>>();
        for (int node = 0; node < size; node++) {
            List<WeightedEdge> neighbors = new ArrayList<>(0);
            this.adjacencyList.add(neighbors);
        }
    }
    
    void addEdge(int src, int dst, int weight) {
        this.adjacencyList.get(src).add(new WeightedEdge(dst, weight));
        this.adjacencyList.get(dst).add(new WeightedEdge(src, weight));
    }
}

class Solution {
    
    private static Comparator<WeightedEdge> comparator =
        new Comparator<WeightedEdge>() {
            @Override
            public int compare(WeightedEdge a, WeightedEdge b) {
                return (a.node - b.node) > 0 ? +1 : -1;
            }
        };
    
    public static List<Integer[]> dijkstras(UndirectedWeightedGraph graph, int start) {
        
        Boolean[] visited = new Boolean[graph.size];
        Arrays.fill(visited, false);
        
        Integer[] distances = new Integer[graph.size];
        Arrays.fill(distances, Integer.MAX_VALUE);
        
        Integer[] prevNodes = new Integer[graph.size];
        Arrays.fill(prevNodes, null);
        
        PriorityQueue<WeightedEdge> pq = new PriorityQueue<>(2 * graph.size, comparator);

        distances[start] = 0;
        pq.offer(new WeightedEdge(start, distances[start]));
        
        while (!pq.isEmpty()) {
            WeightedEdge edge = pq.poll();
            int src = edge.node;
            int srcWeight = edge.weight;
            
            visited[src] = true;
            
            for (WeightedEdge dstEdge : graph.adjacencyList.get(src)) { 
                int dst = dstEdge.node;
                int toDstWeight = dstEdge.weight;
                
                if (visited[dst]) {
                    continue;
                }
                
                int newWeight = distances[src] + toDstWeight;
                
                if (newWeight < distances[dst]) {
                    prevNodes[dst] = src;
                    distances[dst] = newWeight;
                    pq.offer(new WeightedEdge(dst, newWeight));
                }
            }
        }
        
        return new ArrayList<>(Arrays.asList(distances, prevNodes));
    }
    
    public static void main(String[] args) {
        
        UndirectedWeightedGraph graph = new UndirectedWeightedGraph(7);
        
        graph.addEdge(0,1,2);
        graph.addEdge(0,2,6);
        graph.addEdge(1,3,5);
        graph.addEdge(2,3,8);
        graph.addEdge(3,4,10);
        graph.addEdge(3,5,15);
        graph.addEdge(4,6,2);
        graph.addEdge(5,6,6);
        
        List<Integer[]> result = dijkstras(graph, 1);
        
        System.out.println("PASS");
        
    }
}