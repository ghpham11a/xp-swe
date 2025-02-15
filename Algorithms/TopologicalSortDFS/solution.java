import java.util.ArrayList;
import java.util.List;
import java.util.Collections;

class DirectedAcyclicGraph {

    int size;
    List<List<Integer>> adjacencyList;

    DirectedAcyclicGraph(int size) {
        this.size = size;
        this.adjacencyList = new ArrayList<>();
        for (int node = 0; node < size; node++) {
            this.adjacencyList.add(new ArrayList<>());
        }
    }
    
    void addEdge(int src, int dst) {
        this.adjacencyList.get(src).add(dst);
    }
}

class Solution {

    enum Marker {
        UNMARKED,
        TEMPORARY,
        PERMANENT;
    }

    public static List<Integer> topologicalSort(DirectedAcyclicGraph graph) {
        List<Integer> output = new ArrayList<>();

        List<Marker> markers = new ArrayList<>();
        for (int node = 0; node < graph.size; node++) {
            markers.add(Marker.UNMARKED);
        }

        for (int node = 0; node < graph.size; node++) {
            if (markers.get(node) == Marker.UNMARKED) {
                try {
                    topologicalSortDFS(node, graph, output, markers);
                } catch(Exception e) {
                    return new ArrayList<>();
                }
            }
        }
        
        Collections.reverse(output);
        
        return output;
    }
    
    public static void topologicalSortDFS(int node, DirectedAcyclicGraph graph, List<Integer> output, List<Marker> markers) throws Exception {
        
        if (markers.get(node) == Marker.PERMANENT) {
            return;
        }

        if (markers.get(node) == Marker.TEMPORARY) {
            throw new Exception();
        }
        
        markers.set(node, Marker.TEMPORARY);

        for (int neighbor : graph.adjacencyList.get(node)) {
            topologicalSortDFS(neighbor, graph, output, markers);
        }

        markers.set(node, Marker.PERMANENT);
        output.add(node);
    }

    public static void main(String[] args) {
        DirectedAcyclicGraph graph = new DirectedAcyclicGraph(7);
        
        graph.addEdge(0,1);
        graph.addEdge(0,2);
        graph.addEdge(0,5);
        graph.addEdge(1,3);
        graph.addEdge(1,2);
        graph.addEdge(2,3);
        graph.addEdge(2,4);
        graph.addEdge(3,4);
        graph.addEdge(5,4);
        
        List<Integer> output = topologicalSort(graph);
        
        System.out.println("PASS");
    }
}