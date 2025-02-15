import heapq

# Create priority queue
pq = []

# Add to priority queue
heapq.heappush(pq, (5, "DATA"))
heapq.heappush(pq, (4, "DATA"))
heapq.heappush(pq, (3, "DATA"))
heapq.heappush(pq, (2, "DATA"))
heapq.heappush(pq, (1, "DATA"))

output = []
while pq:
    # Remove to priority queue
    data = heapq.heappop(pq)
    
    output.append(data)

assert(output == [(1, 'DATA'), (2, 'DATA'), (3, 'DATA'), (4, 'DATA'), (5, 'DATA')])

print("PASS")