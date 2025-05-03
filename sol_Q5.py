import torch
import networkx as nx
import numpy as np
import os
from sklearn.metrics import accuracy_score, mean_absolute_error
import csv

def label_propagation(graph, labels, alpha=0.99, max_iter=1000, tol=1e-4):
    """
    Algorithme de Label Propagation semi-supervisé (Zhu, 2002)
    graph : networkx.Graph
    labels : numpy array de taille [n_nodes], -1 pour les labels manquants
    """
    A = nx.adjacency_matrix(graph).todense()
    A = np.array(A, dtype=float)
    D = np.diag(np.sum(A, axis=1))
    
    # Matrice de transition (normalisation row-wise)
    D_inv = np.linalg.inv(D)
    S = D_inv @ A

    n_nodes = A.shape[0]
    classes = np.unique(labels[labels != -1])
    n_classes = len(classes)

    # Matrice de label : Y
    Y = np.zeros((n_nodes, n_classes))
    for i in range(n_nodes):
        if labels[i] != -1:
            class_idx = np.where(classes == labels[i])[0][0]
            Y[i, class_idx] = 1

    # Propagation : F ← α S F + (1 - α) Y
    F = torch.tensor(Y, dtype=torch.float32)
    S = torch.tensor(S, dtype=torch.float32)
    Y = torch.tensor(Y, dtype=torch.float32)

    for i in range(max_iter):
        F_new = alpha * S @ F + (1 - alpha) * Y
        if torch.norm(F_new - F) < tol:
            break
        F = F_new

    predictions = torch.argmax(F, axis=1).numpy()
    return classes[predictions]

def remove_labels(labels, fraction, seed=42):
    """
    Remplace une fraction des labels par -1 (manquants)
    """
    np.random.seed(seed)
    labels = np.array(labels)
    n = len(labels)
    to_remove = np.random.choice(n, size=int(fraction * n), replace=False)
    labels_missing = labels.copy()
    labels_missing[to_remove] = -1
    return labels_missing, to_remove

def evaluate_predictions(true_labels, predicted_labels, mask_indices):
    y_true = true_labels[mask_indices]
    y_pred = predicted_labels[mask_indices]
    accuracy = accuracy_score(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    return accuracy, mae

def extract_valid_attributes(G, required_attrs=['gender', 'major_index', 'dorm']):
    """
    Filtrer les nœuds qui contiennent toutes les attributs requis.
    Retourne un sous-graphe + un dictionnaire des attributs filtrés.
    """
    valid_nodes = []
    attr_dict = {attr: [] for attr in ['gender', 'major', 'dorm']}

    for node, data in G.nodes(data=True):
        if all(attr in data and data[attr] is not None for attr in required_attrs):
            valid_nodes.append(node)
            attr_dict['gender'].append(data['gender'])
            attr_dict['major'].append(data['major_index'])
            attr_dict['dorm'].append(data['dorm'])

    # Créer un sous-graphe avec uniquement les nœuds valides
    G_sub = G.subgraph(valid_nodes).copy()
    return G_sub, attr_dict

import os
import csv
import networkx as nx
import numpy as np

def extract_valid_attributes(G, required_attrs=['gender', 'major_index', 'dorm']):
    valid_nodes = []
    attr_dict = {attr: [] for attr in ['gender', 'major', 'dorm']}
    for node, data in G.nodes(data=True):
        if all(attr in data and data[attr] is not None for attr in required_attrs):
            valid_nodes.append(node)
            attr_dict['gender'].append(data['gender'])
            attr_dict['major'].append(data['major_index'])
            attr_dict['dorm'].append(data['dorm'])
    G_sub = G.subgraph(valid_nodes).copy()
    return G_sub, attr_dict

# === MAIN ===
if __name__ == "__main__":
    graph_paths = [
        "data/data/Princeton12.gml",
        "data/data/Caltech36.gml",
        "data/data/Oberlin44.gml",
        "data/data/Johns Hopkins55.gml",
        "data/data/Lehigh96.gml",
        "data/data/Bowdoin47.gml",
        "data/data/Mich67.gml", 
        "data/data/Tufts18.gml", 
        "data/data/Hamilton46.gml", 
        "data/data/Vassar85.gml", 
        "data/data/Vermont70.gml",  
        "data/data/Rice31.gml", 
    ]

    fractions = [0.1, 0.2, 0.3]
    attributes_to_test = ['dorm', 'major', 'gender']

    results_summary = {}

    for graph_path in graph_paths:
        graph_name = os.path.splitext(os.path.basename(graph_path))[0]
        if not os.path.exists(graph_path):
            print(f"Fichier manquant : {graph_path}")
            continue
        
        try:
            print(f"\nLecture du graphe : {graph_path}")
            G = nx.read_gml(graph_path)
            G = G.subgraph(max(nx.connected_components(G), key=len)).copy()
            print(f"Graphe connecté avec {G.number_of_nodes()} nœuds et {G.number_of_edges()} arêtes.")

            G, attr_dict = extract_valid_attributes(G)
            print(f"Attributs valides extraits : {list(attr_dict.keys())}")

            if graph_name not in results_summary:
                results_summary[graph_name] = {}

            for attr in attributes_to_test:
                print(f"\nTraitement de l'attribut : {attr}")
                original_labels = np.array(attr_dict[attr])
                unique_vals = np.unique(original_labels)
                label_map = {val: i for i, val in enumerate(unique_vals)}

                results_summary[graph_name][attr] = []

                for frac in fractions:
                    print(f"  ➤ Suppression aléatoire de {int(frac*100)}% des labels...")
                    labels_missing_raw, removed_idx = remove_labels(original_labels, frac)
                    labels_missing = np.array([label_map[l] if l != -1 else -1 for l in labels_missing_raw])
                    labels_encoded = np.array([label_map[l] for l in original_labels])

                    predicted = label_propagation(G, labels_missing)
                    acc, mae = evaluate_predictions(labels_encoded, predicted, removed_idx)

                    print(f" Accuracy: {acc:.3f} | MAE: {mae:.3f}")
                    results_summary[graph_name][attr].append((frac, acc, mae))

        except Exception as e:
            print(f" Erreur avec {graph_path} : {str(e)}")

    # Affichage résumé
    print("\nRésumé des résultats :")
    for graph, attr_data in results_summary.items():
        print(f"\nGraphe : {graph}")
        for attr, results in attr_data.items():
            print(f"    Attribut : {attr}")
            for frac, acc, mae in results:
                print(f"    ➤ {int(frac*100)}% — Accuracy: {acc:.3f} — MAE: {mae:.3f}")

    # Sauvegarde CSV
    with open("resultat_summary.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Graphe", "Attribut", "Fraction", "Accuracy", "MAE"])
        for graph, attr_data in results_summary.items():
            for attr, results in attr_data.items():
                for frac, acc, mae in results:
                    writer.writerow([graph, attr, frac, acc, mae])

    print("\nRésultats enregistrés dans 'resultat_summary.csv'")
