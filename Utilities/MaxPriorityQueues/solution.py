import heapq

# Create priority queue
pq = []

# Add to priority queue
heapq.heappush(pq, (-1 * 1, "DATA"))
heapq.heappush(pq, (-1 * 2, "DATA"))
heapq.heappush(pq, (-1 * 3, "DATA"))
heapq.heappush(pq, (-1 * 4, "DATA"))
heapq.heappush(pq, (-1 * 5, "DATA"))

output = []
while pq:
    # Remove to priority queue
    key, data = heapq.heappop(pq)
    
    output.append((-key, data))

assert(output == [(5, 'DATA'), (4, 'DATA'), (3, 'DATA'), (2, 'DATA'), (1, 'DATA')])

print("PASS")
