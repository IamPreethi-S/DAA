import snap

# This file is used for generating dataset for Graphs using Random generator
graph = snap.TUNGraph.New()   #graph creation
graph = snap.GenRndGnm(snap.TUNGraph,10000,30000) # Undirected Graph with 10k nodes and 30k edges
FOut = snap.TFOut("test_sample_undirected_10knodes_30k_edges.graph")
graph.Save(FOut)
FOut.Flush()
FIn = snap.TFIn("test_sample_undirected_10knodes_30k_edges.graph")
Undirected_Graph = snap.TUNGraph.Load(FIn)
Undirected_Graph.SaveEdgeList("dataset\\test_sample_undirected_10knodes_30k_edges.txt", "Save as tab-separated list of edges")

