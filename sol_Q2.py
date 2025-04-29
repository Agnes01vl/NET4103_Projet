import networkx as nx
import matplotlib.pyplot as plt
import os
import numpy as np

def load_and_preprocess_graph(file_path):
    """Charge et prétraite le graphe en gardant la plus grande composante connexe"""
    G = nx.read_gml(file_path)
    G = G.subgraph(max(nx.connected_components(G), key=len)).copy()
    return G

def plot_degree_distribution(G, uni_name, output_dir="degree_distributions"):
    """Trace et sauvegarde la distribution des degrés"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    degrees = [d for _, d in G.degree()]
    degree_counts = nx.degree_histogram(G)
    
    plt.figure(figsize=(10, 6))
    
    # Histogramme
    plt.subplot(1, 2, 1)
    plt.hist(degrees, bins=30, edgecolor='black')
    plt.title(f"Degree Distribution - {uni_name}")
    plt.xlabel("Degree")
    plt.ylabel("Number of nodes")
    plt.grid(True)
    
    # Log-log plot
    plt.subplot(1, 2, 2)
    plt.loglog(degree_counts, 'bo')
    plt.title(f"Log-Log Degree Distribution - {uni_name}")
    plt.xlabel("Degree")
    plt.ylabel("Frequency")
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig(f"{output_dir}/{uni_name.replace(' ', '_')}_degree_dist.png")
    plt.close()

def vertexCC(G,v):
    v_neighbors = G[v]
    edges = 0.0
    for i in range(len(v_neighbors)):
        for j in range(i+1, len(v_neighbors)):
            if v_neighbors[j] in G[v_neighbors[i]]:
                edges += 1
    if edges == 0.0:
        return 0.0
    else:
        return edges / ((len(v_neighbors)**2 - len(v_neighbors))/2)

def graphCC(G):
    """Average clustering coefficient using vertexCC"""
    total = 0.0
    count = 0
    for v in G.nodes():
        cc = vertexCC(G, v)
        total += cc
        count += 1
    return total / count if count > 0 else 0.0


def from_dict_to_adj_matrix(G):
    """Convert graph to adjacency matrix"""
    nodes = list(G.nodes())
    N = len(nodes)
    node_index = {node: i for i, node in enumerate(nodes)}
    adj_matrix = np.zeros((N, N))
    
    for u in G.nodes():
        for v in G.neighbors(u):
            adj_matrix[node_index[u], node_index[v]] = 1
    return adj_matrix

def global_clustering(A):
    """Compute global clustering coefficient from adjacency matrix"""
    A = np.asarray(A)
    A_squared = np.dot(A, A)
    A_cubed = np.dot(A_squared, A)
    
    triangles = np.trace(A_cubed) / 6
    triplets = (np.sum(A_squared) - np.trace(A_squared)) / 2
    
    return (3 * triangles) / triplets if triplets > 0 else 0.0

def compute_graph_metrics(G):
    """Compute all graph metrics including both clustering methods"""
    metrics = {
        'global_clustering_matrix': global_clustering(from_dict_to_adj_matrix(G)),
        'mean_local_clustering': nx.average_clustering(G),
        'density': nx.density(G),
        'num_nodes': G.number_of_nodes(),
        'num_edges': G.number_of_edges()
    }
    return metrics

def compute_graph_metrics(G):
    """Calcule les métriques du graphe"""
    metrics = {
        'global_clustering': nx.transitivity(G),
        'mean_local_clustering': nx.average_clustering(G),
        'density': nx.density(G),
        'num_nodes': G.number_of_nodes(),
        'num_edges': G.number_of_edges()
    }
    return metrics

def plot_degree_vs_clustering(G, uni_name, output_dir="degree_clustering_plots"):
    """Generate scatter plot: Degree vs. Local Clustering Coefficient"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    degrees = [d for _, d in G.degree()]
    clustering = list(nx.clustering(G).values())  # Local clustering coefficients
    
    plt.figure(figsize=(10, 6))
    plt.scatter(degrees, clustering, alpha=0.6, edgecolor='k')
    plt.title(f"Degree vs. Clustering: {uni_name}", fontsize=14)
    plt.xlabel("Degree", fontsize=12)
    plt.ylabel("Local Clustering Coefficient", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    
    
    plt.savefig(f"{output_dir}/{uni_name.replace(' ', '_')}_degree_vs_clustering.png", dpi=300, bbox_inches='tight')
    plt.close()


def analyze_network(file_name, uni_name, data_dir="/home/agnes/NET4103/Projet/NET4103_Projet/data/data"):
    """Analyse complète d'un réseau"""
    try:
        file_path = os.path.join(data_dir, file_name)
        G = load_and_preprocess_graph(file_path)
        
        # Question (1-a): Distribution des degrés
        plot_degree_distribution(G, uni_name)
        
        # Question (1-b): Métriques
        metrics = compute_graph_metrics(G)
        
        print(f"\n--- {uni_name} ---")
        print(f"Number of nodes in LCC: {metrics['num_nodes']}")
        print(f"Number of edges: {metrics['num_edges']}")
        print(f"Global clustering coefficient: {metrics['global_clustering']:.4f}")
        print(f"Mean local clustering coefficient: {metrics['mean_local_clustering']:.4f}")
        print(f"Edge density: {metrics['density']:.6f}")

        #Question (1-c)

        plot_degree_vs_clustering(G, uni_name, output_dir="degree_clustering_plots")

        # Print key metrics for comparison
        avg_degree = sum(dict(G.degree()).values()) / G.number_of_nodes()
        avg_clustering = nx.average_clustering(G)

        print(f"Average Degree: {avg_degree:.2f}")
        print(f"Average Local Clustering: {avg_clustering:.4f}")
        print(f"Global Clustering (Transitivity): {nx.transitivity(G):.4f}")
        
        return metrics
    
    except Exception as e:
        print(f"Error processing {uni_name}: {str(e)}")
        return None

def main():
    universities = [
        ('Caltech36.gml', 'Caltech'),
        ('MIT8.gml', 'MIT'),
        ('Johns Hopkins55.gml', 'Johns Hopkins')
    ]
    
    all_metrics = {}
    
    for file_name, uni_name in universities:
        metrics = analyze_network(file_name, uni_name)
        if metrics:
            all_metrics[uni_name] = metrics
    
    
if __name__ == "__main__":
    main()