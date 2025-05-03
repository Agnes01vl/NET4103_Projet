import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from matplotlib.lines import Line2D

output_dir = 'analyse_label_propagation'
os.makedirs(output_dir, exist_ok=True)

# Charger les résultats
df = pd.read_csv('resultat_summary.csv')

# Afficher les colonnes disponibles
print("Colonnes du fichier :", df.columns)

# Boxplot de l'Accuracy
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Fraction', y='Accuracy', hue='Attribut')
plt.title('Distribution de l’Accuracy par Attribut selon la Fraction de labels supprimés')
plt.xlabel('Fraction des labels supprimés')
plt.ylabel('Accuracy')
plt.grid(True)
plt.legend(title='Attribut')
plt.savefig(os.path.join(output_dir, 'boxplot_accuracy_par_attribut.png'), dpi=300, bbox_inches='tight')

# Boxplot du MAE
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Fraction', y='MAE', hue='Attribut', showfliers=False)
plt.title('Distribution du MAE par Attribut selon la Fraction de labels supprimés (sans outliers)')
plt.xlabel('Fraction des labels supprimés')
plt.ylabel('MAE')
plt.grid(True)
plt.legend(title='Attribut')
plt.savefig(os.path.join(output_dir, 'boxplot_mae_par_attribut.png'), dpi=300, bbox_inches='tight')

# Palette cohérente pour les attributs
attributes = df['Attribut'].unique()
palette = sns.color_palette("Set2", n_colors=len(attributes))
color_map = dict(zip(attributes, palette))

# ----- KDE pour l'Accuracy -----
plt.figure(figsize=(10, 5))
for attr in attributes:
    subset = df[df['Attribut'] == attr]
    sns.kdeplot(subset['Accuracy'], fill=True, label=attr, alpha=0.3, color=color_map[attr])
    mean_val = subset['Accuracy'].mean()
    plt.axvline(mean_val, linestyle='--', color=color_map[attr], linewidth=2, label=f"Moyenne {attr}")

plt.title("Densité de l'Accuracy par Attribut avec lignes de moyenne")
plt.xlabel("Accuracy")
plt.ylabel("Densité")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'densite_accuracy_par_attribut_moyenne.png'), dpi=300)

# Moyennes par attribut
mean_scores = df.groupby('Attribut')[['Accuracy', 'MAE']].mean().reset_index()
print("\nScores moyens par attribut :")
print(mean_scores)


plt.show()
