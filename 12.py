import heapq

def prim_mst(graph, start_vertex):
    """
    Implements Prim's algorithm to find the Minimum Spanning Tree (MST).
   
    Parameters:
        graph (dict): A dictionary representing the graph, where keys are vertex labels
                      and values are lists of tuples (neighbor, weight).
        start_vertex (str): The starting vertex for the MST.
   
    Returns:
        mst (list): A list of edges (tuples) in the MST.
        total_cost (int): The total cost of the MST.
    """
    min_heap = []  # Min-heap (priority queue) to select edges with the minimum weight
    visited = set()  # Set to keep track of visited vertices
    mst = []  # List to store the edges of the MST
    total_cost = 0  # Total cost of the MST
   
    # Start with the start vertex
    visited.add(start_vertex)
   
    # Push all the edges from the start vertex to the heap
    for neighbor, weight in graph[start_vertex]:
        heapq.heappush(min_heap, (weight, start_vertex, neighbor))
   
    while min_heap:
        # Pop the edge with the smallest weight
        weight, u, v = heapq.heappop(min_heap)
       
        if v not in visited:  # If the destination vertex is not visited
            visited.add(v)  # Mark it as visited
            mst.append((u, v, weight))  # Add the edge to the MST
            total_cost += weight  # Add the weight of the edge to the total cost
           
            # Add all edges from the new vertex to the heap
            for neighbor, w in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (w, v, neighbor))
   
    return mst, total_cost

# Example graph representing houses (A, B, C, D, E) and their connection costs
# Each house is a vertex, and each tuple (neighbor, weight) represents a pipeline (edge with cost).
graph = {
    'A': [('B', 5), ('C', 10)],
    'B': [('A', 5), ('D', 3)],
    'C': [('A', 10), ('D', 2)],
    'D': [('B', 3), ('C', 2), ('E', 7)],
    'E': [('D', 7)]
}

# Define the starting vertex (house) for Prim's algorithm
start_vertex = 'A'

# Run the Prim's algorithm to find the MST and the total cost
mst, total_cost = prim_mst(graph, start_vertex)

# Output the result
print("Minimum Spanning Tree (MST):")
for u, v, weight in mst:
    print(f"{u} -- {v} (cost {weight})")
print(f"Total cost of laying pipelines: {total_cost}")