from abc import ABC, abstractmethod
import networkx as nx
import numpy as np
import random
import progressbar
from itertools import combinations
import os
import csv

class LinkPrediction(ABC):
    def __init__(self, graph):
        """
        Constructeur
        ------------
        graph : networkx.Graph
            Le graphe sur lequel appliquer la prédiction de lien
        """
        self.graph = graph
        self.N = len(graph)

    def neighbors(self, v):
        """
        Retourne la liste des voisins d’un sommet

        Parameters
        ----------
        v : int
            Identifiant du sommet

        Returns
        -------
        list
            Liste des voisins
        """
        return list(self.graph.neighbors(v))

    @abstractmethod
    def fit(self, u, v):
        """
        Méthode à implémenter dans chaque sous-classe.
        Prend deux nœuds u et v et retourne un score de prédiction.
        """
        raise NotImplementedError("fit doit être implémenté dans la sous-classe.")


# === Métrique 1 : Voisins communs ===
class CommonNeighbors(LinkPrediction):
    def fit(self, u, v):
        """Score = nombre de voisins communs"""
        return len(set(self.neighbors(u)) & set(self.neighbors(v)))


# === Métrique 2 : Jaccard ===
class Jaccard(LinkPrediction):
    def fit(self, u, v):
        """Score = Jaccard index = intersection / union"""
        set_u = set(self.neighbors(u))
        set_v = set(self.neighbors(v))
        intersection = set_u & set_v
        union = set_u | set_v
        if not union:
            return 0
        return len(intersection) / len(union)


# === Métrique 3 : Adamic/Adar ===
class AdamicAdar(LinkPrediction):
    def fit(self, u, v):
        """Score = somme des 1 / log(degré) des voisins communs"""
        common = set(self.neighbors(u)) & set(self.neighbors(v))
        score = 0.0
        for w in common:
            deg = len(self.neighbors(w))
            if deg > 1:
                score += 1 / np.log(deg)
        return score



def remove_edges_randomly(G, f=0.05):
    """
    Supprime aléatoirement une fraction f des arêtes.
    Retourne une copie du graphe modifié et la liste des arêtes supprimées.
    """
    G_copy = G.copy()
    edges = list(G_copy.edges())
    nb_to_remove = int(len(edges) * f)
    removed_edges = random.sample(edges, nb_to_remove)
    G_copy.remove_edges_from(removed_edges)
    return G_copy, removed_edges



def get_non_edge_node_pairs(G):
    """Retourne les paires de nœuds non connectés"""
    return [(u, v) for u, v in combinations(G.nodes(), 2) if not G.has_edge(u, v)]


def evaluate_link_predictor(G, graph_path, fraction=0.1, output_csv="Q4_predicttion_f01.csv"):
    """
    Fonction qui évalue les prédicteurs de lien et stocke les résultats dans un CSV.
    """
    # Suppression aléatoire des arêtes
    G_modified, removed_edges = remove_edges_randomly(G, fraction)
    print(f"Nombre d'arêtes supprimées : {len(removed_edges)}")

    # Génération des paires de nœuds non connectés
    non_edges = get_non_edge_node_pairs(G_modified)
    print("Nombre de paires de nœuds non connectés :", len(non_edges))

    # Définir les prédicteurs
    predictors = {
        "CommonNeighbors": CommonNeighbors(G_modified),
        "Jaccard": Jaccard(G_modified),
        "AdamicAdar": AdamicAdar(G_modified),
    }

    k_values = [50, 100, 200, 300, 400]
    results = []

    for predictor_name, predictor in predictors.items():
        print(f"\nÉvaluation du prédicteur : {predictor_name}")

        scores = []
        bar = progressbar.ProgressBar(max_value=len(non_edges))
        for i, (u, v) in enumerate(non_edges):
            score = predictor.fit(u, v)
            scores.append(((u, v), score))
            bar.update(i)

        scores_sorted = sorted(scores, key=lambda x: x[1], reverse=True)

        for k in k_values:
            top_k_predicted_edges = [pair for pair, _ in scores_sorted[:k]]
            correct_predictions = set(removed_edges).intersection(set(top_k_predicted_edges))

            tp = len(correct_predictions)
            fp = k - tp
            fn = len(removed_edges) - tp

            precision = tp / (tp + fp) if (tp + fp) > 0 else 0
            recall = tp / (tp + fn) if (tp + fn) > 0 else 0

            results.append([
                graph_path,
                predictor_name,
                k,
                round(precision, 3),
                round(recall, 3),
                len(removed_edges),
                len(non_edges)
            ])

            print(f"Top@{k}={tp}, Precision@{k}={precision:.3f}, Recall@{k}={recall:.3f}")

    # Écriture dans le fichier CSV
    file_exists = os.path.exists(output_csv)
    with open(output_csv, mode='a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Graph", "Predictor", "K", "Precision", "Recall", "RemovedEdges", "NonConnectedPairs"])
        writer.writerows(results)

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

    output_csv = "Q4_predicttion_f01.csv"
    fractions = [0.05, 0.1, 0.15, 0.2]
    fraction = 0.15

    for graph_path in graph_paths:
        if not os.path.exists(graph_path):
            print(f"Fichier manquant : {graph_path}")
            continue
        G = nx.read_gml(graph_path)
        G = G.subgraph(max(nx.connected_components(G), key=len)).copy()
        print(f"\nÉvaluation sur le graphe : {graph_path} avec fraction={fraction}")
        evaluate_link_predictor(G, graph_path, fraction, output_csv=output_csv)

