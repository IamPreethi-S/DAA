STEPS FOR EXECUTION OF THE SOURCE CODE:

We have implemented this project in Python using Pycharm IDE

Step 1: Prequisite to have Python Interpreter and Pycharm IDE ( Python version-3.7 or greater) and also have the following libraries installed (networkx, matplotlib).

Step 2: Open the terminal and navigate to the downloaded project file and locate the folder named 'CSE_5311_011_Project_Source_code'.

Step 3: Execute the main file of the code (~python main.py).

Step 4: After executing the main file, the command line will display the nodes and edges of the undirected graph along with the average time taken to execute the BFS and DFS function.
 
Step 5: A pop up window will appear showing the plotting of the graph for the first scenario which is "Keeping Constant number of nodes and Increasing edges".

Step 6: Only when the first plotting graph is closed, the second scenario of the experimentation which is "Keeping Constant number of edges and Increasing nodes" will start executing.

Step 7: A pop up window will appear showing the plotting of the graph for the second scenario.

Step 8: Once the pop-up window is closed for the second graph, the main program will be terminated.


DATASET:

- A dataset folder is present inside the project folder named 'CSE_5311_011_Project_Source_code' which is used to compare the performances of the Graph Search algorithm (BFS and DFS).

- A file named graph_dataset_generator is present inside the folder named 'CSE_5311_011_Project_Source_code' which is used to generate the graph datasets (10 datasets) using Random Generator (Graphs with edges and nodes as Adjacency list in .txt file).

- The project is implemented in 2 sceanrios by keeping constant node and increasing edges and keeping constant number of edges and increasing nodes thereby having 5 datasets each.

- The bfs and dfs functions are executed 5 times to capture the average running time for each dataset and the same is plotted in the graphs (which is created using Matplotlib library).




