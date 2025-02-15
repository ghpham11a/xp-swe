class DisjointSet(val size: Int) {
    
    val parent: Array<Int>
    val rank: Array<Int>
    
    init {
        parent = Array<Int>(size) { 0 }        
        for (i in 0..<size) {
            parent[i] = i
        }
        rank = Array<Int>(size) { 1 }
    }
    
    fun find(node: Int): Int {
        if (parent[node] == node) {
            parent[node] = parent[parent[node]]
            return parent[node]
        }
        return find(parent[node])
    }
    
    fun union(nodeA: Int, nodeB: Int): Boolean {
        val rootA = find(nodeA)
        val rootB = find(nodeB)
        
        if (rootA == rootB) {
            return false
        }
        
        if (rank[rootA] > rank[rootB]) {
            parent[rootB] = rootA
            rank[rootA] += rank[rootB]
        } else {
            parent[rootA] = rootB
            rank[rootB] += rank[rootA]
        }
        
        return true
    }
}

fun main() {
    
    val edges = listOf(listOf(0,2), listOf(1,4), listOf(1,5), listOf(2,3), listOf(2,7), listOf(4,8), listOf(5,8))
    
    var disjointSet = DisjointSet(9)
    
    for (edge in edges) {
        disjointSet.union(edge[0], edge[1])
    }
    
    assert(disjointSet.parent.toList() == listOf(2, 4, 2, 2, 4, 4, 6, 2, 4))
    
    println("PASS")
}