import os
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def compute_assortativity_taille(G, attribute):
    """Calcule l'assortativité et la taille pour un attribut donné"""
    try:
        if attribute == 'degree':
            assortativity = nx.degree_assortativity_coefficient(G)
        else:
            if attribute not in G.nodes[list(G.nodes)[0]]:
                assortativity = np.nan
            else:
                assortativity = nx.attribute_assortativity_coefficient(G, attribute)
                print('tu en a réussii 1111!!')
    except Exception as e:
        
        print(f"[WARN] Erreur d'assortativité sur {attribute} : {e}")
        assortativity = np.nan
    
    taille = G.number_of_nodes()
    return assortativity, taille

def process_all_graphs(data_dir, attributes):
    """Traite tous les graphes GML et collecte les données"""
    data = {'assortativity': [], 'taille': []}
    
    for file_name in os.listdir(data_dir):
        if file_name.endswith('.gml'):
            file_path = os.path.join(data_dir, file_name)
            try:
                G = nx.read_gml(file_path)
                G = G.subgraph(max(nx.connected_components(G), key=len)).copy()
                
                attr = attributes
                if (attr == attributes) :
                    assort, taille = compute_assortativity_taille(G, attr)
                    data[attr]['assortativity'].append(assort)
                    data[attr]['taille'].append(taille)
                    
            except Exception as e:
                print(f"[ERREUR] Impossible de traiter {file_name} : {e}")
    
    return data

def plot_assortativity(data, attributes, output_dir='plots'):
    """Génère les scatter plots pour chaque attribut"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    attr = attributes
    if (attr == attributes) :
        plt.figure(figsize=(10, 6))
        plt.scatter(data[attr]['taille'], data[attr]['assortativity'], alpha=0.6)
        plt.axhline(0, color='r', linestyle='--', label='Assortativité nulle')
        plt.xscale('log')
        plt.xlabel('Taille du réseau (log)')
        plt.ylabel('Coefficient d\'assortativité')
        plt.title(f'Assortativité par {attr}')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.6)
        
        plot_file = os.path.join(output_dir, f'assortativity_{attr}.png')
        plt.savefig(plot_file, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Plot sauvegardé : {plot_file}")

def main():
    # Configuration
    data_dir = '/home/agnes/NET4103/Projet/NET4103_Projet/data/data'
    attributes = 'student_fac'
    
    # Traitement
    print("Début du traitement des graphes...")
    data = process_all_graphs(data_dir, attributes)
    
    # Visualisation
    print("Génération des plots...")
    plot_assortativity(data, attributes)
    
    print("Traitement terminé!")

if __name__ == '__main__':
    main()