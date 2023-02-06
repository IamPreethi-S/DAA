import time
import networkx as nx
import matplotlib.pyplot as plt

# dataset for constant nodes and increasing edges
graph_constant_nodes_file_list = [
    ("dataset\\test_sample_undirected_10knodes_5k_edges.txt", 10000),  # graph file, number of nodes/vertices
    ("dataset\\test_sample_undirected_10knodes_8k_edges.txt", 10000),
    ("dataset\\test_sample_undirected_10knodes_10k_edges.txt", 10000),
    ("dataset\\test_sample_undirected_10knodes_12k_edges.txt", 10000),
    ("dataset\\test_sample_undirected_10knodes_15k_edges.txt", 10000)]


# dataset for constant edges and increasing nodes
graph_constant_edges_file_list = [
    ("dataset\\test_sample_undirected_3knodes_30k_edges.txt", 3000),
    ("dataset\\test_sample_undirected_6knodes_30k_edges.txt", 6000),
    ("dataset\\test_sample_undirected_10knodes_30k_edges.txt", 10000),
    ("dataset\\test_sample_undirected_12knodes_30k_edges.txt", 12000),
    ("dataset\\test_sample_undirected_15knodes_30k_edges.txt", 15000)]


class Graph:
    def __init__(self, nodes, edges):
        self.data = [[] for _ in range(nodes)]
        for v1, v2 in edges:
            self.data[v1].append(v2)
            self.data[v2].append(v1)


def bfs(graph, source):
    visited = []
    queue = [source]
    while len(queue):
        vertex = queue.pop()
        for v in graph.data[vertex]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited


def dfs(graph, source):
    visited = []
    stack = [source]
    while len(stack):
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            for adjacent_nodes in graph.data[vertex]:
                stack.append(adjacent_nodes)
    return visited


# to capture average time taken to execute Bfs function for graph
# average is taken by executing the Bfs function for 5 times

def bfs_avg(graph):
    start = time.monotonic()
    for i in range(5):
        bfs(graph, 0)
    end = time.monotonic()
    bfs_average = (end - start) / 5
    return bfs_average


# to capture average time taken to execute Dfs function for graph
# average is taken by executing the Dfs function for 5 times

def dfs_avg(graph):
    start = time.monotonic()
    for i in range(5):
        dfs(graph, 0)
    end = time.monotonic()
    dfs_average = (end - start) / 5
    return dfs_average


print("\n Generating Undirected graphs for BFS Vs DFS : Constant Node and Increasing Edges \n")

increasing_edges_array = []  # list of increasing edges
bfs_result = []  # average time of Bfs for constant nodes_increasing edges
dfs_result = []  # average time for Dfs for constant nodes_increasing edges

for (graph_dataset_file, node_size) in graph_constant_nodes_file_list:
    nx_graph = nx.Graph()
    nx_edges = nx.read_edgelist(graph_dataset_file)
    nx_nodes = nx.read_adjlist(graph_dataset_file)
    nx_graph.add_edges_from(nx_edges.edges())
    nx_graph.add_nodes_from(nx_nodes)

    edges = [[int(j) for j in i] for i in list(nx_graph.edges())]
    # print (edges)
    print(" \n Generating Undirected graph with ", node_size, "nodes and ", len(edges), "edges")
    graph = Graph(node_size, edges)

    increasing_edges_array.append(len(edges))
    bfs_result.append(bfs_avg(graph))
    dfs_result.append(dfs_avg(graph))

# print(graph)
print("List of Increasing Edges:",increasing_edges_array)
print("Average time taken for Breadth first search for constant nodes and Increasing edges: ", bfs_result)
print("Average time taken for Depth first search for constant nodes and Increasing edges:", dfs_result)
# print (bfs(graph,0)) # to get the list of Bfs traversal path
# print (dfs(graph,0)) # to get the list of Dfs traversal path

# Plotting Bfs and Dfs Graph for constant nodes and Increasing edges
plt.title("BFS Vs DFS: Constant Node & Increasing edges ")
plt.plot(increasing_edges_array, bfs_result, "g", linestyle='solid', label="BFS", marker='.')
plt.plot(increasing_edges_array, dfs_result, "b", linestyle='dotted', label="DFS", marker='.')
plt.xlabel("Constant Node: 10000")
labels = ["E1:5000", "E2:8000", "E3:10000", "E4:12000", "E5:15000"]
plt.xticks(increasing_edges_array, labels)
plt.ylabel("Average Iteration Time (in seconds)")
plt.legend()
plt.show()

print("---------------------------------------------------------------------------")

print("\n Generating Undirected graphs for BFS Vs DFS : Constant Edges and Increasing Nodes \n")

increasing_nodes_array = []  # length of increasing edges
bfs_result_ = []  # average time of Bfs for constant nodes_increasing edges
dfs_result_ = []  # average time for Dfs for constant nodes_increasing edges

for (graph_dataset_file, node_size) in graph_constant_edges_file_list:
    nx_graph = nx.Graph()
    nx_edges = nx.read_edgelist(graph_dataset_file)
    nx_nodes = nx.read_adjlist(graph_dataset_file)
    nx_graph.add_edges_from(nx_edges.edges())
    nx_graph.add_nodes_from(nx_nodes)

    # print(nx_graph.nodes())
    # nx.draw(my_ungraph, with_labels=True, font_weight='bold') - drawm graph

    node_length = len(nx_graph.nodes())
    edges = [[int(j) for j in i] for i in list(nx_graph.edges())]
    # print (edges)

    graph = Graph(node_size, edges)
    increasing_nodes_array.append((node_size))
    print(" \n Generating Undirected graph with ", node_size, "nodes and ", len(edges), "edges")
    bfs_result_.append(bfs_avg(graph))
    dfs_result_.append(dfs_avg(graph))

# print(graph)
print("List of Increasing Nodes:", increasing_nodes_array)
print("Average time taken for Breadth first search for constant edges and Increasing nodes:", bfs_result_)
print("Average time taken for Depth first search for constant edges and Increasing nodes:", dfs_result_)
# print (bfs(graph,0)) # to get the list of Bfs traversal path
# print (dfs(graph,0)) # to get the list of Dfs traversal path

# Plotting Bfs and Dfs Graph for constant edges and Increasing nodes
plt.title("BFS Vs DFS: Constant Edge & Increasing Nodes ")
plt.plot(increasing_nodes_array, bfs_result_, "g", linestyle='solid', label="BFS", marker='.')
plt.plot(increasing_nodes_array, dfs_result_, "b", linestyle='dotted', label="DFS", marker='.')
plt.xlabel("Constant Edge: 30000")
labels = ["N1:3000", "N2:6000", "N3:10000", "N4:12000", "N5:15000"]
plt.xticks(increasing_nodes_array, labels)
plt.ylabel("Average Iteration Time (in seconds)")
plt.legend()
plt.show()
