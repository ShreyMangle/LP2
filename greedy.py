# ==========================================
# 1. SELECTION SORT (Greedy Search)
# ==========================================
def selection_sort(data):
    arr = list(data)
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# ==========================================
# 2. PRIM'S ALGORITHM (Greedy MST)
# ==========================================
def run_prims():
    n_v = int(input("Enter number of vertices: "))
    n_e = int(input("Enter number of edges: "))
    edges = []
    print("Enter edges (u v weight):")
    for _ in range(n_e):
        u, v, w = input().split()
        edges.append((u, v, int(w)))
    
    start_node = input("Enter start vertex: ")
    visited = [start_node]
    mst_edges = []
    total_cost = 0

    while len(visited) < n_v:
        min_edge = None
        min_weight = 10**9 # Simple infinity

        for u, v, w in edges:
            u_in = False
            v_in = False
            for node in visited:
                if u == node: u_in = True
                if v == node: v_in = True
            
            # Greedy: One in, one out
            if (u_in and not v_in) or (v_in and not u_in):
                if w < min_weight:
                    min_weight = w
                    min_edge = (u, v, w)
        
        if min_edge:
            u, v, w = min_edge
            next_node = v if u in visited else u
            visited.append(next_node)
            mst_edges.append(min_edge)
            total_cost += w
            
    print("Prim's MST:", mst_edges)
    print("Total Cost:", total_cost)

# ==========================================
# 3. KRUSKAL'S ALGORITHM (Greedy MST)
# ==========================================
def run_kruskals():
    n_v = int(input("Enter number of vertices: "))
    n_e = int(input("Enter number of edges: "))
    edges = []
    print("Enter edges (u v weight):")
    for _ in range(n_e):
        u, v, w = input().split()
        edges.append((u, v, int(w)))

    # Greedy Step: Sort edges by weight
    for i in range(len(edges)):
        for j in range(i + 1, len(edges)):
            if edges[i][2] > edges[j][2]:
                edges[i], edges[j] = edges[j], edges[i]

    parent = {}
    def find(i):
        if parent[i] == i: return i
        return find(parent[i])

    # Setup parent tracking for cycle detection
    for u, v, w in edges:
        parent[u] = u
        parent[v] = v

    mst_edges = []
    total_cost = 0
    for u, v, w in edges:
        if find(u) != find(v): # If no cycle
            root_u = find(u)
            root_v = find(v)
            parent[root_u] = root_v # Union
            mst_edges.append((u, v, w))
            total_cost += w

    print("Kruskal's MST:", mst_edges)
    print("Total Cost:", total_cost)

# ==========================================
# MAIN FUNCTION
# ==========================================
def main():
    print("--- Greedy Algorithms Menu ---")
    print("1. Selection Sort")
    print("2. Prim's Algorithm")
    print("3. Kruskal's Algorithm")
    
    choice = input("\nEnter choice (1-3): ")

    if choice == '1':
        # Simple list input
        nums = input("Enter numbers (space separated): ").split()
        for i in range(len(nums)): nums[i] = int(nums[i])
        print("Sorted List:", selection_sort(nums))

    elif choice == '2':
        run_prims()

    elif choice == '3':
        run_kruskals()

if __name__ == "__main__":
    main()
