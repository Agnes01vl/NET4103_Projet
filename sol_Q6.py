from sknetwork.clustering import Louvain
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder
import networkx as nx
from collections import Counter


def load_and_preprocess_graph(file_path):
    G = nx.read_gml(file_path)
    G = G.subgraph(max(nx.connected_components(G), key=len)).copy()
    return G


file_path = "data/data/Johns Hopkins55.gml"
G = load_and_preprocess_graph(file_path)

unG = nx.Graph(G)
largest_cc = max(nx.connected_components(unG), key=len)
S = G.subgraph(largest_cc).copy()
node_list = list(S.nodes())

adjacency = nx.adjacency_matrix(S, nodelist=node_list, weight="weight").todense()

pr = nx.pagerank(S)
louvain = Louvain()
communities = louvain.fit_predict(adjacency)

labels = LabelEncoder().fit_transform(communities)

cmap = plt.get_cmap('tab20')

pos = nx.spring_layout(S, seed=80, k=1.2, iterations=200)
plt.figure(figsize=(10, 8))
nx.draw_networkx_edges(S, pos, alpha=0.1)

nodes = nx.draw_networkx_nodes(
    S,
    pos,
    node_size=50,
    node_color=labels,
    cmap=cmap
)

plt.title("Communautés détectées par Louvain")

# Légende pour les communautés
handles = []
for i in range(np.max(labels) + 1): 
    handle = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=cmap(i / (np.max(labels) + 1)), markersize=10, label=f'Communauté {i}')
    handles.append(handle)

plt.legend(handles=handles, title="Communautés", loc="upper left", fontsize=10)
plt.axis('off')
plt.show()


# Fonction pour calculer l'attribut dominant pour chaque communauté
def compute_dominant_attributes_with_counts(community_nodes, graph, attributes):
    dominant_attributes = {}
    
    for attr in attributes:
        values = [graph.nodes[node].get(attr) for node in community_nodes]
        value_count = Counter(values)
        dominant_value, count = value_count.most_common(1)[0]
        dominant_attributes[attr] = {
            "dominant_value": dominant_value,
            "count": count
        }
    
    return dominant_attributes

attributes = ["student_fac", "gender", "major_index", "second_major", "dorm", "year", "high_school"]
community_dominant_attributes = {}

# Parcours des communautés et calcul des attributs dominants
for i in range(np.max(labels) + 1): 
    community_nodes = [node_list[j] for j in range(len(node_list)) if labels[j] == i]
    dominant_attributes = compute_dominant_attributes_with_counts(community_nodes, G, attributes)
    community_dominant_attributes[i] = dominant_attributes

# Afficher les résultats
for community, dominant_attrs in community_dominant_attributes.items():
    print(f"Communauté {community}:")
    for attr, data in dominant_attrs.items():
        print(f"  {attr}: {data['dominant_value']} (count: {data['count']})")

