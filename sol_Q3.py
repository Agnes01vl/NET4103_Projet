import os
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ATTRIBUTES = ['student_fac', 'major_index', 'degree', 'dorm', 'gender']

def compute_assortativity_taille(G, attribute):
    try:
        if attribute == 'degree':
            assortativity = nx.degree_assortativity_coefficient(G)
        else:
            if attribute not in G.nodes[list(G.nodes)[0]]:
                assortativity = np.nan
            else:
                assortativity = nx.attribute_assortativity_coefficient(G, attribute)
    except Exception as e:
        print(f"[WARN] Erreur d’assortativité sur {attribute} : {e}")
        assortativity = np.nan
    
    taille = G.number_of_nodes()
    return assortativity, taille


def create_scatter_plot(df, attribute, ax):
    df_sorted = df.sort_values('n_nodes')
    ax.scatter(df_sorted['n_nodes'], df_sorted[attribute], alpha=0.6)
    if attribute == 'gender':
        ax.axhline(0, color='r', linestyle='--')
    ax.set_xscale('log')
    ax.set_title(f'Assortativité vs Taille ({attribute})')
    ax.set_xlabel('Taille du réseau (log)')
    ax.set_ylabel('Assortativité')

def create_histogram(df, attribute, ax):
    ax.hist(df[attribute].dropna(), bins=20, alpha=0.7)
    if attribute == 'gender':
        ax.axvline(0, color='r', linestyle='--')
    ax.set_title(f'Distribution de l’assortativité ({attribute})')
    ax.set_xlabel('Valeur')
    ax.set_ylabel('Fréquence')


def load_gml_graph(file_path):
    """Charge un graphe GML et conserve sa plus grande composante connexe"""
    G = nx.read_gml(file_path)
    return G.subgraph(max(nx.connected_components(G), key=len)).copy()

def analyze_network(G, network_name):
    """
    Analyse un réseau pour tous les attributs pertinents
    Args:
        G: Le graphe NetworkX
        network_name: Nom du réseau
    Returns:
        Dictionnaire des résultats
    """
    results = {
        'network': network_name,
        'n_nodes': G.number_of_nodes(),
        'n_edges': G.number_of_edges()
    }
    
    # Attributs à analyser (adaptés à votre format GML)
    attributes = ['student_fac', 'gender', 'major_index', 'dorm']
    
    for attr in attributes:
        results[attr] = compute_assortativity(G, attr)
    
    # Ajout de l'assortativité par degré
    results['degree'] = compute_assortativity(G, 'degree')
    
    return results

def visualize_results(df, output_file):
    """
    Génère les visualisations
    Args:
        df: DataFrame avec les résultats
        output_file: Fichier de sortie pour les graphiques
    """
    attributes = ['student_fac', 'gender', 'major_index', 'dorm', 'degree']
    
    fig, axes = plt.subplots(2, len(attributes), figsize=(5*len(attributes), 10))
    
    for i, attr in enumerate(attributes):
        # Scatter plot
        axes[0,i].scatter(df['n_nodes'], df[attr], alpha=0.6)
        axes[0,i].axhline(0, color='r', linestyle='--')
        axes[0,i].set_xscale('log')
        axes[0,i].set_title(f'Assortativité: {attr}')
        axes[0,i].set_xlabel('Taille du réseau (log)')
        axes[0,i].set_ylabel('Coefficient')
        
        # Histogramme
        axes[1,i].hist(df[attr].dropna(), bins=20, alpha=0.7)
        axes[1,i].axvline(0, color='r', linestyle='--')
        axes[1,i].set_title(f'Distribution: {attr}')
        axes[1,i].set_xlabel('Valeur')
        axes[1,i].set_ylabel('Fréquence')
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300)
    plt.close()

def main():
    # Configuration
    DATA_DIR = '/home/agnes/NET4103/Projet/NET4103_Projet/data/data'
    OUTPUT_FILE = 'assortativity_analysis.png'
    
    # Analyse de tous les fichiers GML
    results = []
    for file_name in os.listdir(DATA_DIR):
        if file_name.endswith('.gml'):
            try:
                file_path = os.path.join(DATA_DIR, file_name)
                G = load_gml_graph(file_path)
                network_name = file_name.replace('.gml', '')
                results.append(analyze_network(G, network_name))
            except Exception as e:
                print(f"Erreur avec {file_name}: {str(e)}")
    
    # Création du DataFrame
    df = pd.DataFrame(results)
    
    # Visualisation
    visualize_results(df, OUTPUT_FILE)
    
    # Sauvegarde
    df.to_csv('assortativity_results.csv', index=False)
    print("Analyse terminée. Résultats sauvegardés.")

if __name__ == '__main__':
    main()