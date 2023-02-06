# CSE-5311-Design-and-Analysis-of-Algorithms (DAA)
This repository contains projects  that I did when I took CSE 5311 under Professor Noor at UTA in Fall 2022. 

Implemented two graph search algorithms BFS(Breadth First Search using Queue data structure) and DFS(Depth First Search using Stack data structure) in Python, compared their performances and running time analysis.

Learnings Outcomes:

1.Time Complexity:
From the plotting and the flow of BFS and DFS, we understood that the
performance of BFS and DFS are similar as their time complexity is O(V+E).
BFS:
In BFS,each vertex is enqueued and dequeued utmost twice since it is an
undirected graph.The enqueue and dequeue operations take constant
amount of time i.e O(1).Hence, the total queue operations would take O(V)
where V is number of nodes/vertices.When the node is dequeued, the node
is scanned across the adjacency list utmost once to get their neighbour
nodes.The sum of all the adjacency lists is O(E).The total time taken to scan
the lists is O(E).
As initialization takes O(V) and scanning takes O(E).The total time
complexity of BFS is O(V+E).
DFS:
DFS examines each edge at most twice since it is an Undirected graph, one
from each end of the node and stack supports push and pop operation in
O(1) time.
A constant amount of time is performed per edge which takes O(m).
Initialization takes O(n) time.
The running time for DFS would be O(m+2n) or O(V+2E) which is ~ O(V+E)
where n=|V| and m =|E|.

2. Space Complexity:
BFS:
The space complexity of BFS is O(V) as in the worst case it corresponds to
the maximum number of vertices present in the graph that may be stored in
the queue.
DFS:
The space complexity of DFS is O(V) as in the worst case it corresponds to
the maximum number of vertices present in the graph that may be stored in
the stack.

3.Plotting Of Graphs:
The matplotlib library is used to plot the graphs.In plotting, X-axis would be
the nodes and edges consisting of two different scenarios
(1) With increasing number of edges and constant number of nodes
(2) With increasing number of nodes and constant number of edges
And Y-axis would depict the average iteration time for the datasets.
The iteration time is captured using the monotonic() function.


Challenges faced:
- Initially we faced some challenges in generating the dataset using a
random generator. Later, we studied the Snap.Stanford module for
generating a large dataset for the graph.
- While experimenting with the wide range of data (in millions), the
loading of a huge dataset was taking a little longer time, thus the
nodes and edges were decreased to thousands and later we generated
the plotting for the above scenarios.


Results :
Comparing the performances of the Breadth first search and Depth first
search graph search algorithms, they are not much different as the time
complexity discussed in run time analysis is O(V+E) where V is the vertices
and E is the edges of the graph.
Although they seem to perform very much similar from the plots, it is
evident that BFS performs slightly better than DFS. The reason is Breadth
first search tries to reach the neighbour nodes with minimum number of
edges from the source vertex whereas Depth first search might be a little
slower as it traverses more edges to reach the vertex from the source node
as it traverses deeper . In general, when the source node is closer to the
target node, then Breadth first search performs better when compared to
depth first search as it tries to reach the destination/target node with
minimal edges
