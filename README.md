# NET4103_Projet

## 1. 
Le plus petit réseau (Caltech) a 762 nœuds dans la plus grande composante connectée (LCC), et le plus grand a plus de 40000 nœuds dans la LCC.,Utilisons trois réseaux du FB100 : Caltech (avec 762 nœuds dans la LCC), MIT (qui a 6402 nœuds dans la LCC), et Johns Hopkins (qui a 5157 nœuds dans la LCC).

## (a) Degree Distributions

### Caltech (avec 762 nœuds dans la LCC)
![Caltech Degree Distribution](degree_distributions/Caltech_degree_dist.png)

### MIT(qui a 6402 nœuds dans la LCC)
![MIT Degree Distribution](degree_distributions/MIT_degree_dist.png)

### Johns Hopkins (qui a 5157 nœuds dans la LCC)
![Johns Hopkins Degree Distribution](degree_distributions/Johns_Hopkins_degree_dist.png)

> What are you able to conclude from these
degree distributions?

## (b) Coefficients de clustering et densité

Nous avons calculé les métriques suivantes pour chaque réseau (LCC uniquement) :

| Université       | Global Clustering | Mean Local Clustering | Densité des Arêtes |
|------------------|-------------------|------------------------|--------------------|
| Caltech          | 0.2913            | 0.4091                 | 0.057429           |
| MIT              | 0.1803            | 0.2724                 | 0.012261           |
| Johns Hopkins    | 0.1932            | 0.2690                 | 0.014034           |

### Interprétation

> L'un ou l'autre de ces réseaux doit-il être considéré comme peu dense ? Sur la base des informations relatives à la densité et au regroupement, que pouvez-vous dire de la topologie du graphe ?

Oui, tous ces réseaux sont peu denses, particulièrement MIT et Johns Hopkins (densité ≈ 1–2%).

Clustering global/local mesure la tendance des voisins d’un sommet à aussi être voisins entre eux, donc la présence de triangles (groupes d'amis mutuels).

Caltech a les meilleurs scores de clustering :
- Global Clustering : 0.2913 (assez élevé)
- Mean Local Clustering : 0.4091

➔ Cela suggère que Caltech a une structure fortement communautaire : des petits groupes très connectés, même si globalement le réseau reste peu dense.

MIT et Johns Hopkins ont un clustering plus bas :
- Environ 0.18–0.19 global, et 0.27 en local.

➔ Cela indique des structures plus "diffuses" : il y a des liens, mais moins de triangles fermés, donc moins de petits groupes très soudés.

## (c) diagramme de dispersion

(1 point) Pour chaque réseau, dessinez également un diagramme de dispersion du degré en fonction du coefficient de regroupement local. Sur la base de ces calculs et des précédents, êtes-vous en mesure de tirer des conclusions sur les similitudes ou les différences entre les réseaux d'arbres ? Quelles autres observations pouvez-vous faire ?


### Caltech (avec 762 nœuds dans la LCC)
![Caltech Degree Distribution](degree_clustering_plots/Caltech_degree_vs_clustering.png)

### MIT(qui a 6402 nœuds dans la LCC)
![MIT Degree Distribution](degree_clustering_plots/MIT_degree_vs_clustering.png)

### Johns Hopkins (qui a 5157 nœuds dans la LCC)
![Johns Hopkins Degree Distribution](degree_clustering_plots/Johns_Hopkins_degree_vs_clustering.png)

### **1. Les réseaux sont-ils clairsemés (sparse) ? Que peut-on dire de leur topologie ?**  

✅ **Tous les réseaux sont extrêmement clairsemés** :  
- **Densité** très faible (Caltech : 0.057, MIT : 0.012, Johns Hopkins : 0.014), ce qui est typique des grands réseaux réels (ex : Facebook a une densité ~10⁻⁶).  
- **Preuve de parcimonie** : La densité diminue avec la taille du réseau (MIT/JHU plus grands → densité plus faible).  

#### **Caractéristiques topologiques**  
| Métrique               | Caltech       | MIT           | Johns Hopkins |  
|------------------------|---------------|---------------|---------------|  
| **Densité**            | 0.057         | 0.012         | 0.014         |  
| **Degré moyen**        | 43.7          | 78.5          | 72.4          |  
| **Clustering local**   | 0.409         | 0.272         | 0.269         |  
| **Clustering global**  | 0.291         | 0.180         | 0.193         |  

- **Propriété "petit monde"** (small-world) :  
  - **Clustering élevé** (≫ réseaux aléatoires) + **chemins courts** (typique des réseaux sociaux).  
  - Caltech est le plus marqué (clustering le plus fort).  
- **Tendance "scale-free"** :  
  - Distribution des degrés probablement en loi de puissance (quelques hubs, beaucoup de nœuds peu connectés).  
  - MIT/JHU ont des degrés moyens plus élevés → plus de hubs.  

**Implications** :  
- La **faible densité** permet une structure économe en liens.  
- Le **clustering élevé** favorise la diffusion d’information dans des communautés soudées.  

---

### **2. Comparaison des réseaux et observations**  

#### **Similitudes**  
- **Propriétés universelles** :  
  - Tous sont **clairsemés**, **petits mondes**, et montrent une **corrélation négative** entre degré et clustering.  
  - Architecture typique des réseaux sociaux réels.  

#### **Différences clés**  
| Aspect                | Caltech              | MIT                  | Johns Hopkins        |  
|-----------------------|----------------------|----------------------|----------------------|  
| **Structure communautaire** | Plus forte (clustering élevé) | Plus faible (liens "ponts") | Intermédiaire |  
| **Centralisation**    | Moins hiérarchique   | Plus de hubs         | Hubs modérés         |  
| **Taille**           | Petit (762 nœuds)    | Grand (6402 nœuds)   | Moyen (5157 nœuds)   |  

#### **Observations notables**  
- **Anomalie de Caltech** :  
  - Densité plus élevée que MIT/JHU malgré sa petite taille → **sociabilité très concentrée** (ex : campus petit, interactions fréquentes).  
- **MIT vs. Johns Hopkins** :  
  - MIT a un **degré moyen plus élevé** mais un **clustering plus faible** → réseautage plus large (ex : cours massifs, collaborations interdisciplinaires).  
  - Johns Hopkins est un compromis entre Caltech et MIT.  

#### **Questions complémentaires**  
- La distribution des degrés suit-elle une **loi de puissance** ? (Vérifier les plots log-log.)  
- Les hubs jouent-ils un rôle de **ponts** entre communautés ? (Analyser la centralité intermédiaire.)  

---

### **Synthèse finale**  
1. **Clairsemés mais petits mondes** :  
   - Optimisés pour la diffusion d’information (chemins courts + clusters serrés).  
2. **Effet de la taille** :  
   - Petit réseau (Caltech) → clustering fort, densité élevée.  
   - Grands réseaux (MIT/JHU) → plus de hubs, clustering relâché.  
3. **Culture institutionnelle** :  
   - Caltech reflète une communauté soudée, MIT un réseau décentralisé.  

**Pistes d’approfondissement** :  
- Comparer les **coefficients d’assortativité** (homophilie par degré).  
- Identifier les **communautés** via des algorithmes (Louvain, Girvan-Newman).  

Vous souhaitez explorer une de ces pistes ?