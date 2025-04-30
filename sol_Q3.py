import os
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns  # Ajoute ceci en haut si ce n'est pas encore fait


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
                print(assortativity)
    except Exception as e:

        print(f"[WARN] Erreur d'assortativité sur {attribute} : {e}")
        assortativity = np.nan
    
    taille = G.number_of_nodes()
    return assortativity, taille


def process_all_graphs(data_dir, attributes, cache_dir='cache'):
    """Traite les graphes pour chaque attribut et sauvegarde les résultats"""
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

    all_data = {}

    for attr in attributes:
        cache_file = os.path.join(cache_dir, f"{attr}_assort.csv")

        if os.path.exists(cache_file):
            print(f"[INFO] Chargement depuis le cache : {cache_file}")
            df = pd.read_csv(cache_file)
        else:
            print(f"[INFO] Calcul en cours pour l'attribut : {attr}")
            results = {'assortativity': [], 'taille': [], 'network': []}

            for file_name in os.listdir(data_dir):
                if file_name.endswith('.gml'):
                    file_path = os.path.join(data_dir, file_name)
                    try:
                        G = nx.read_gml(file_path)
                        G = G.subgraph(max(nx.connected_components(G), key=len)).copy()
                        assort, taille = compute_assortativity_taille(G, attr)
                        results['assortativity'].append(assort)
                        results['taille'].append(taille)
                        results['network'].append(file_name)
                    except Exception as e:
                        print(f"[ERREUR] {file_name} : {e}")

            df = pd.DataFrame(results)
            df.to_csv(cache_file, index=False)
            print(f"[INFO] Sauvegarde du cache : {cache_file}")

        all_data[attr] = df

    return all_data

def plot_assortativity(data, attributes, output_dir='assortivity'):
    """Génère les scatter plots ET les courbes de densité pour chaque attribut"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for attr in attributes:
        valid_data = data[attr]['assortativity'].dropna()  # Évite les NaN

        if not valid_data.empty:
            print("[INFO]: on continue tout va bien")
        else:
            print(f"[WARN] Pas de données valides pour {attr}, densité non générée.")
            continue

        mean_assortativity = valid_data.mean()
        print(f"assortivité moyenne: {mean_assortativity} pour {attr}")

        plt.figure(figsize=(12, 6))  

        # --- SCATTER PLOT ---
        plt.subplot(1, 2, 1)
        plt.scatter(data[attr]['taille'], data[attr]['assortativity'], alpha=0.6)
        plt.axhline(0, color='r', linestyle='--', label='Assortativité nulle')
        plt.xscale('log')
        plt.xlabel('Taille du réseau (log)')
        plt.ylabel('Coefficient d\'assortativité')
        plt.title(f'Scatter : Assortativité vs Taille - {attr}')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.6)

        # --- COURBE DE DENSITÉ ---
        plt.subplot(1, 2, 2)
        sns.kdeplot(valid_data, fill=True, bw_adjust=0.5)
        plt.axvline(0, color='r', linestyle='--', label='Assortativité nulle (0)')
        plt.axvline(mean_assortativity, color='b', linestyle='--', label=f'Moyenne ({mean_assortativity:.2f})')
        plt.xlabel('Coefficient d\'assortativité')
        plt.ylabel('Densité')
        plt.title(f'Densité des valeurs d\'assortativité - {attr}')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.6)

        plt.tight_layout()
        plot_file = os.path.join(output_dir, f'assortativity_{attr}.png')
        plt.savefig(plot_file, dpi=300, bbox_inches='tight')
        plt.show()
        plt.close()
        print(f"[INFO] Graphiques sauvegardés : {plot_file}")

def main():
    data_dir = '/home/agnes/NET4103/Projet/NET4103_Projet/data/data'
    attributes = ['student_fac', 'gender', 'major_index', 'dorm', 'degree']

    print("Traitement ou chargement des données...")
    all_data = process_all_graphs(data_dir, attributes)

    print("Génération des visualisations...")
    plot_assortativity(all_data,attributes)

    print("Terminé !")


if __name__ == '__main__':
    main()
