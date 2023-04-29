# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import matplotlib.pyplot as plt
import networkx as nx


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

n=5  #节点数
k=5
p=0.5
G=nx.watts_strogatz_graph(n, k, p)

G1 = nx.DiGraph()
G1 = G.to_directed()

a = 3
G1.remove_edges_from([(0, a)])


#for i in range(len(list(G1.neighbors(1)))):
#    print(list(G1.neighbors(1))[i])
#    G1.remove_edges_from([1, list(G1.neighbors(1))[i]])


nx.draw(G1, with_labels=True)
plt.show()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
