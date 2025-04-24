import networkx as nx
import matplotlib.pyplot as plt
import os


if not os.path.exists('degree_distributions'):
    os.makedirs('degree_distributions')

# Liste des fichiers et noms des universités
universities = [
    ('Caltech36.gml', 'Caltech'),
    ('MIT8.gml', 'MIT'),
    ('Johns Hopkins55.gml', 'Johns Hopkins')
]

for file_name, uni_name in universities:
    try:
        G = nx.read_gml(f"/home/agnes/NET4103/Projet/NET4103_Projet/data/data/{file_name}")
        G = G.subgraph(max(nx.connected_components(G), key=len)).copy()
        
        # Calculer le degré de chaque nœud
        degrees = [d for _, d in G.degree()]
        
        # Créer la figure
        plt.figure(figsize=(10, 6))
        
        # Deux sous-graphiques: histogramme et log-log plot
        plt.subplot(1, 2, 1)
        plt.hist(degrees, bins=30, edgecolor='black')
        plt.title(f"Degree Distribution - {uni_name}")
        plt.xlabel("Degree")
        plt.ylabel("Number of nodes")
        plt.grid(True)
        
        plt.subplot(1, 2, 2)
        plt.loglog(nx.degree_histogram(G), 'bo')
        plt.title(f"Log-Log Degree Distribution - {uni_name}")
        plt.xlabel("Degree")
        plt.ylabel("Frequency")
        plt.grid(True)
        
        plt.tight_layout()
        
        # Sauvegarder la figure
        plt.savefig(f"degree_distributions/{uni_name.replace(' ', '_')}_degree_dist.png")
        plt.close()  # Fermer la figure pour libérer la mémoire
        
        print(f"Graphique pour {uni_name} sauvegardé avec succès.")

        # Calculs des métriques
        global_clustering = nx.transitivity(G)
        mean_local_clustering = nx.average_clustering(G)
        density = nx.density(G)
        
        # Affichage des résultats
        print(f"\n--- {uni_name} ---")
        print(f"Global clustering coefficient: {global_clustering:.4f}")
        print(f"Mean local clustering coefficient: {mean_local_clustering:.4f}")
        print(f"Edge density: {density:.6f}")

    except Exception as e:
        print(f"Erreur lors du traitement de {uni_name}: {str(e)}")


print("Traitement terminé pour toutes les universités.")

for _, uni_name in universities:
    file_path = f"degree_distributions/{uni_name.replace(' ', '_')}_degree_dist.png"
    if os.path.exists(file_path):
        print(f"✅ Image trouvée : {file_path}")
    else:
        print(f"❌ Image manquante : {file_path}")
