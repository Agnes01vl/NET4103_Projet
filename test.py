





# Choix de la fraction d’arêtes à retirer
fractions = [0.05, 0.1, 0.15, 0.2]
G_modified, removed_edges = remove_edges_randomly(G, fractions[1])
print(f"Nombre d'arêtes supprimées : {len(removed_edges)}")

# Initialisation du prédicteur
predictor = CommonNeighbors(G_modified)

# Génération des paires de nœuds non connectés
non_edges = get_non_edge_node_pairs(G_modified)
print("Nombre de paires de nœuds non connectés :", len(non_edges))

# Calcul des scores avec barre de progression
print("Calcul des scores de prédiction...")
scores = []
bar = progressbar.ProgressBar(max_value=len(non_edges))
for i, (u, v) in enumerate(non_edges):
    score = predictor.fit(u, v)
    scores.append(((u, v), score))
    bar.update(i)

# Tri des scores en ordre décroissant
scores_sorted = sorted(scores, key=lambda x: x[1], reverse=True)

# Évaluation des performances : top@k, precision@k, recall@k
k_values = [50, 100, 200, 300, 400]
print("\nÉvaluation des prédictions :")
for k in k_values:
    top_k_predicted_edges = [pair for pair, _ in scores_sorted[:k]]
    correct_predictions = set(removed_edges).intersection(set(top_k_predicted_edges))
    
    tp = len(correct_predictions)
    fp = k - tp
    fn = len(removed_edges) - tp
    
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    
    print(f"Top@{k}={tp}, Precision@{k}={precision:.3f}, Recall@{k}={recall:.3f}")
