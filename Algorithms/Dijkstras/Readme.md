g - adjacency list of weighted graph
n - the number of nodes in the graph
s - the index of the starting node

function dijkstra(g, n, s):

    vis = [false, false, ..., false] # size n
    prev = [null, null, ..., null] # size n
    dist = [inf, inf, ..., inf] # size n

    dist[s] = 0
    pq = empty priority queue
    pq.insert((s, 0))

    while pq.size() != 0:
        index, minValue = pq.poll()
        vis[index] = true
        if dist[index] < minValue: continue

        for (edge : g[index]):

            if vis[edge.to]: continue

            newDist = dist[index] + edge.cost

            if newDist < dist[edge.to]:
                prev[edge.to] = index 
                dist[edge.to] = newDist
                pq.insert((edge.to, newDist))

    return (dist, prev)

