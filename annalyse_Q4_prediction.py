import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

output_dir='annalyse_link_prediction'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Charger le CSV
df = pd.read_csv('Q4_prediction.csv')  # Ne pas filtrer sur un graphe spécifique

#############################Important
plt.figure(figsize=(14, 6))
sns.boxplot(data=df, x='K', y='Precision', hue='Predictor')
plt.title('Distribution de la précision par prédicteur selon K')
plt.xlabel('K')
plt.ylabel('Précision')
plt.grid(True)
plt.legend(title='Prédicteur')
plot_file = os.path.join(output_dir, f'Distribution_precision.png')
plt.savefig(plot_file, dpi=300, bbox_inches='tight')


# Boxplot du Recall
plt.figure(figsize=(14, 6))
sns.boxplot(data=df, x='K', y='Recall', hue='Predictor', showfliers=False)
plt.title('Distribution du recall par prédicteur selon K (sans outliers)')
plt.xlabel('K')
plt.ylabel('Recall')
plt.grid(True)
plt.legend(title='Prédicteur')
plot_file = os.path.join(output_dir, 'Distribution_recall_sans_outliers.png')
plt.savefig(plot_file, dpi=300, bbox_inches='tight')


# Moyennes par prédicteur
mean_scores = df.groupby('Predictor')[['Precision', 'Recall']].mean().reset_index()
print ("les scores moyens sont:")
print(mean_scores)

# Écart-type par prédicteur
std_scores = df.groupby('Predictor')[['Precision', 'Recall']].std().reset_index()
print("ecart-type par prédicteur")
print(std_scores)

#peux tu me faire un histogramme lisse de la densité de la précision et du recall pour les 3 prédictor avec un axe qui montre la moyenne

df = pd.read_csv('Q4_prediction.csv')  # sans filtrage

# Regroupe globalement
recall_stats = df.groupby('Predictor')['Recall'].describe()

# Palette de couleurs pour chaque prédicteur
palette = sns.color_palette("Set1", n_colors=len(df['Predictor'].unique()))
predictors = df['Predictor'].unique()
color_map = dict(zip(predictors, palette))

# KDE de la précision
plt.figure(figsize=(10, 5))
sns.kdeplot(data=df, x='Precision', hue='Predictor', fill=True, common_norm=False, alpha=0.4)

# Lignes verticales avec couleurs personnalisées
for predictor in predictors:
    mean_val = df[df['Predictor'] == predictor]['Precision'].mean()
    plt.axvline(mean_val, linestyle='--', color=color_map[predictor], label=f'Moyenne {predictor}', linewidth=1.5)

plt.title('Densité de la Précision par Prédicteur')
plt.xlabel('Precision')
plt.ylabel('Densité')
plt.legend()
plt.grid(True)
plot_file = os.path.join(output_dir, 'Densité_Precision_Prédicteur.png')
plt.savefig(plot_file, dpi=300, bbox_inches='tight')

# KDE du recall
plt.figure(figsize=(10, 5))
sns.kdeplot(data=df, x='Recall', hue='Predictor', fill=True, common_norm=False, alpha=0.4)

for predictor in predictors:
    mean_val = df[df['Predictor'] == predictor]['Recall'].mean()
    plt.axvline(mean_val, linestyle='--', color=color_map[predictor], label=f'Moyenne {predictor}', linewidth=1.5)

plt.title('Densité du Recall par Prédicteur')
plt.xlabel('Recall')
plt.ylabel('Densité')
plt.legend()
plt.grid(True)
plot_file = os.path.join(output_dir, 'Densité_Recall_Prédicteur.png')
plt.savefig(plot_file, dpi=300, bbox_inches='tight')
plt.show()

