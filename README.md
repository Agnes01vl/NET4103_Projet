# NET4103_Projet

## 2. 
Le plus petit réseau (Caltech) a 762 nœuds dans la plus grande composante connectée (LCC), et le plus grand a plus de 40000 nœuds dans la LCC.,Utilisons trois réseaux du FB100 : Caltech (avec 762 nœuds dans la LCC), MIT (qui a 6402 nœuds dans la LCC), et Johns Hopkins (qui a 5157 nœuds dans la LCC).

### (a) Degree Distributions

#### Caltech (avec 762 nœuds dans la LCC)
![Caltech Degree Distribution](degree_distributions/Caltech_degree_dist.png)

#### MIT(qui a 6402 nœuds dans la LCC)
![MIT Degree Distribution](degree_distributions/MIT_degree_dist.png)

#### Johns Hopkins (qui a 5157 nœuds dans la LCC)
![Johns Hopkins Degree Distribution](degree_distributions/Johns_Hopkins_degree_dist.png)

> What are you able to conclude from these
degree distributions?

### (b) Coefficients de clustering et densité

Nous avons calculé les métriques suivantes pour chaque réseau (LCC uniquement) :

| Université       | Global Clustering | Mean Local Clustering | Densité des Arêtes |
|------------------|-------------------|------------------------|--------------------|
| Caltech          | 0.2913            | 0.4091                 | 0.057429           |
| MIT              | 0.1803            | 0.2724                 | 0.012261           |
| Johns Hopkins    | 0.1932            | 0.2690                 | 0.014034           |

#### Interprétation

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

### (c) diagramme de dispersion

(1 point) Pour chaque réseau, dessinez également un diagramme de dispersion du degré en fonction du coefficient de regroupement local. Sur la base de ces calculs et des précédents, êtes-vous en mesure de tirer des conclusions sur les similitudes ou les différences entre les réseaux d'arbres ? Quelles autres observations pouvez-vous faire ?


#### Caltech (avec 762 nœuds dans la LCC)
![Caltech Degree Distribution](degree_clustering_plots/Caltech_degree_vs_clustering.png)

#### MIT(qui a 6402 nœuds dans la LCC)
![MIT Degree Distribution](degree_clustering_plots/MIT_degree_vs_clustering.png)

#### Johns Hopkins (qui a 5157 nœuds dans la LCC)
![Johns Hopkins Degree Distribution](degree_clustering_plots/Johns_Hopkins_degree_vs_clustering.png)

#### **1. Les réseaux sont-ils clairsemés (sparse) ? Que peut-on dire de leur topologie ?**  

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

#### **2. Comparaison des réseaux et observations**  

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

## 3. Analyse de l’assortativité sur les réseaux Facebook100

Nous avons analysé l’assortativité sur 100 réseaux sociaux issus du jeu de données **Facebook100**. L’étude a été menée pour les 5 attributs suivants :

1. **Statut étudiant/enseignant (`student_fac`)**
2. **Genre (`gender`)**
3. **Majeure (`major_index`)**
4. **Dortoir (`dorm`)**
5. **Degré du sommet (`degree`)**

Chaque attribut a été examiné selon deux types de visualisations :

- **Un diagramme de dispersion (scatter plot)** : montre l’assortativité en fonction de la taille du réseau (avec un axe logarithmique pour le nombre de nœuds), avec une ligne horizontale :
  - **Rouge** : niveau d’assortativité nulle (`0`)

- **Une courbe de densité (histogramme lissé)** : montre la distribution des valeurs d’assortativité pour les 100 réseaux, avec deux lignes verticales :
  - **Rouge** : niveau d’assortativité nulle (`0`)
  - **Bleue** : valeur moyenne de l’assortativité pour l’attribut


### 1. Statut étudiant/enseignant (`student_fac`)

![student_fac](assortivity/assortativity_student_fac.png)

- **Assortativité moyenne** : `0.3227`
- L’assortativité est relativement élevée, indiquant une forte tendance des individus à se connecter avec d'autres du même statut (étudiants entre eux, enseignants entre eux). Cela suggère que les interactions sociales dans les universités sont majoritairement homogènes selon le statut institutionnel.
- La distribution est concentrée au-dessus de zéro, ce qui montre une homogénéité constante à travers les universités.

---

### 2. Genre (`gender`)

![gender](assortivity/assortativity_gender.png)

- **Assortativité moyenne** : `0.0429`
- L’assortativité est très faible en moyenne, proche de zéro. Certaines universités présentent même une **assortativité légèrement négative**, jusqu’à -0.10, ce qui signifie que dans ces cas, les connexions sont légèrement plus fréquentes entre genres différents que similaires.
- La densité maximale atteint environ 11, avec une forte concentration autour de 0, et une pointe de densité à 4.8 pour une assortativité nulle. Cela suggère que, dans la majorité des cas, **le genre n’est pas un facteur structurant fort** dans les relations sociales étudiées.

---

### 3. Majeure (`major_index`)

![major_index](assortivity/assortativity_major_index.png)

- **Assortativité moyenne** : `0.0511`
- Faible mais toujours positive, ce qui indique une légère tendance à se connecter avec des personnes de la même filière académique.
- L’histogramme est très concentré autour de 0.042, avec une densité atteignant jusqu’à 35, indiquant une forte homogénéité dans la distribution.
- La taille du réseau n’a pas d’effet clair sur l’assortativité, bien que les réseaux les plus grands montrent parfois des valeurs plus élevées, absentes chez les plus petits réseaux. Cela pourrait refléter des structures académiques plus différenciées dans les grandes universités.

---

### 4. Dortoir (`dorm`)

![dorm](assortivity/assortativity_dorm.png)

- **Assortativité moyenne** : `0.1751`
- L’assortativité est modérée et toujours strictement positive, indiquant que les personnes ont tendance à se connecter davantage avec celles de leur propre dortoir.
- La densité maximale est d’environ 8, avec une forte densité entre 0.1 et 0.25.
- L’assortativité est relativement stable quel que soit la taille du réseau, suggérant que le lieu de résidence est un **facteur cohérent d’organisation sociale** dans les campus.

---

### 5. Degré du sommet (`degree`)

![degree](assortivity/assortativity_degree.png)

- **Assortativité moyenne** : `0.0626`
- Faible en moyenne, mais la distribution est **très étalée**, avec des valeurs allant jusqu’à **0.2** et descendant à **-0.1**.
- La densité maximale est d’environ 9, avec une densité de 6 autour d’une assortativité nulle.
- **Les petits réseaux** présentent parfois des assortativités négatives, tandis que les **grands réseaux** montrent une plus grande dispersion des valeurs. Cela indique que dans les grandes universités, les profils de connexion sont plus variés en termes de degré ( certains utilisateurs très connectés interagissent avec des utilisateurs peu connectés, et vice-versa) . Ce qui est logique avec le fait que dans une petite université, les étudiants ont plus de chances de se connaître mutuellement, ce qui peut mener à un nombre de connexions similaire entre pairs et donc une assortativité plus homogène. 


## 4.

Dans cette question, on attend de vous que vous calculiez des algorithmes de prédiction de liens sur un grand nombre de graphes (plus de 10).

### (a) Lire le document [4].

### (b)  Implémentez les métriques de prédiction de liens suivantes : 

Voir sol_Q4.py où l'on trouve:

- class CommonNeighbors(LinkPrediction):
- class Jaccard(LinkPrediction):
- class AdamicAdar(LinkPrediction):

#### (d) **(2 points)** Choisissez quelques graphes du dataset Facebook100, exécutez et évaluez les performances de chaque prédicteur de lien, puis **concluez sur l’efficacité** des trois métriques suivantes :  
- voisins communs,  
- Jaccard,  
- Adamic/Adar.

Évaluation sur le graphe : data/data/Rice31.gml avec une fraction de 0.05 des arêtes supprimées
Nombre d'arêtes supprimées : 9241
Nombre de paires de nœuds non connectés : 8157818

Évaluation du prédicteur : CommonNeighbors
 99% (8153233 of 8157818) |########################################################################## | Elapsed Time: 0:01:01 ETA:   0:00:00
Évaluation des performances :
Top@50=40, Precision@50=0.800, Recall@50=0.004
Top@100=71, Precision@100=0.710, Recall@100=0.008
Top@200=136, Precision@200=0.680, Recall@200=0.015
Top@300=193, Precision@300=0.643, Recall@300=0.021
Top@400=233, Precision@400=0.583, Recall@400=0.025

Évaluation du prédicteur : Jaccard
 99% (8152197 of 8157818) |########################################################################## | Elapsed Time: 0:01:39 ETA:   0:00:00
Évaluation des performances :
Top@50=22, Precision@50=0.440, Recall@50=0.002
Top@100=42, Precision@100=0.420, Recall@100=0.005
Top@200=77, Precision@200=0.385, Recall@200=0.008
Top@300=109, Precision@300=0.363, Recall@300=0.012
Top@400=145, Precision@400=0.362, Recall@400=0.016

Évaluation du prédicteur : AdamicAdar
 99% (8151958 of 8157818) |########################################################################## | Elapsed Time: 0:02:00 ETA:   0:00:00
Évaluation des performances :
Top@50=40, Precision@50=0.800, Recall@50=0.004
Top@100=74, Precision@100=0.740, Recall@100=0.008
Top@200=138, Precision@200=0.690, Recall@200=0.015
Top@300=196, Precision@300=0.653, Recall@300=0.021
Top@400=244, Precision@400=0.610, Recall@400=0.026


Évaluation sur le graphe : data/data/Princeton12.gml avec une fraction de 0.05 des arêtes supprimées
Nombre d'arêtes supprimées : 14665
Nombre de paires de nœuds non connectés : 21333383

Évaluation du prédicteur : CommonNeighbors
 99% (21325358 of 21333383) |######################################################################## | Elapsed Time: 0:02:57 ETA:   0:00:00
Évaluation des performances :
Top@50=34, Precision@50=0.680, Recall@50=0.002
Top@100=64, Precision@100=0.640, Recall@100=0.004
Top@200=106, Precision@200=0.530, Recall@200=0.007
Top@300=145, Precision@300=0.483, Recall@300=0.010
Top@400=189, Precision@400=0.472, Recall@400=0.013

Évaluation du prédicteur : Jaccard
 99% (21328910 of 21333383) |######################################################################## | Elapsed Time: 0:04:55 ETA:   0:00:00
Évaluation des performances :
Top@50=6, Precision@50=0.120, Recall@50=0.000
Top@100=22, Precision@100=0.220, Recall@100=0.002
Top@200=49, Precision@200=0.245, Recall@200=0.003
Top@300=79, Precision@300=0.263, Recall@300=0.005
Top@400=109, Precision@400=0.273, Recall@400=0.007

Évaluation du prédicteur : AdamicAdar
 99% (21327894 of 21333383) |############################################################################### | Elapsed Time: 0:05:05 ETA:   0:00:00
Évaluation des performances :
Top@50=32, Precision@50=0.640, Recall@50=0.002
Top@100=60, Precision@100=0.600, Recall@100=0.004
Top@200=109, Precision@200=0.545, Recall@200=0.007
Top@300=151, Precision@300=0.503, Recall@300=0.010
Top@400=196, Precision@400=0.490, Recall@400=0.013

Évaluation sur le graphe : data/data/Caltech36.gml avec une fraction de 0.05 des arêtes supprimées
Nombre d'arêtes supprimées : 832
Nombre de paires de nœuds non connectés : 274122

Évaluation du prédicteur : CommonNeighbors
 99% (272258 of 274122) |################################################################################### | Elapsed Time: 0:00:01 ETA:   0:00:00
Évaluation des performances :
Top@50=19, Precision@50=0.380, Recall@50=0.023
Top@100=39, Precision@100=0.390, Recall@100=0.047
Top@200=61, Precision@200=0.305, Recall@200=0.073
Top@300=80, Precision@300=0.267, Recall@300=0.096
Top@400=98, Precision@400=0.245, Recall@400=0.118

Évaluation du prédicteur : Jaccard
 96% (264799 of 274122) |#################################################################################   | Elapsed Time: 0:00:01 ETA:   0:00:00
Évaluation des performances :
Top@50=14, Precision@50=0.280, Recall@50=0.017
Top@100=27, Precision@100=0.270, Recall@100=0.032
Top@200=52, Precision@200=0.260, Recall@200=0.062
Top@300=67, Precision@300=0.223, Recall@300=0.081
Top@400=79, Precision@400=0.198, Recall@400=0.095

Évaluation du prédicteur : AdamicAdar
 97% (268528 of 274122) |##################################################################################  | Elapsed Time: 0:00:02 ETA:   0:00:00
Évaluation des performances :
Top@50=19, Precision@50=0.380, Recall@50=0.023
Top@100=37, Precision@100=0.370, Recall@100=0.044
Top@200=64, Precision@200=0.320, Recall@200=0.077
Top@300=80, Precision@300=0.267, Recall@300=0.096
Top@400=98, Precision@400=0.245, Recall@400=0.118

Évaluation sur le graphe : data/data/Oberlin44.gml avec une fraction de 0.05 des arêtes supprimées
Nombre d'arêtes supprimées : 4495
Nombre de paires de nœuds non connectés : 4176323

Évaluation du prédicteur : CommonNeighbors
 99% (4163275 of 4176323) |################################################################################# | Elapsed Time: 0:00:27 ETA:   0:00:00
Évaluation des performances :
Top@50=27, Precision@50=0.540, Recall@50=0.006
Top@100=43, Precision@100=0.430, Recall@100=0.010
Top@200=70, Precision@200=0.350, Recall@200=0.016
Top@300=90, Precision@300=0.300, Recall@300=0.020
Top@400=112, Precision@400=0.280, Recall@400=0.025

Évaluation du prédicteur : Jaccard
 99% (4171083 of 4176323) |################################################################################# | Elapsed Time: 0:00:36 ETA:   0:00:00
Évaluation des performances :
Top@50=8, Precision@50=0.160, Recall@50=0.002
Top@100=30, Precision@100=0.300, Recall@100=0.007
Top@200=58, Precision@200=0.290, Recall@200=0.013
Top@300=86, Precision@300=0.287, Recall@300=0.019
Top@400=108, Precision@400=0.270, Recall@400=0.024

Évaluation du prédicteur : AdamicAdar
 99% (4173650 of 4176323) |################################################################################# | Elapsed Time: 0:00:40 ETA:   0:00:00
Évaluation des performances :
Top@50=28, Precision@50=0.560, Recall@50=0.006
Top@100=45, Precision@100=0.450, Recall@100=0.010
Top@200=70, Precision@200=0.350, Recall@200=0.016
Top@300=96, Precision@300=0.320, Recall@300=0.021
Top@400=119, Precision@400=0.297, Recall@400=0.026

Évaluation sur le graphe : data/data/Johns Hopkins55.gml avec une fraction de 0.05 des arêtes supprimées
Nombre d'arêtes supprimées : 9328
Nombre de paires de nœuds non connectés : 13117502

Évaluation du prédicteur : CommonNeighbors
 99% (13109589 of 13117502) |############################################################################### | Elapsed Time: 0:01:29 ETA:   0:00:00
Évaluation des performances :
Top@50=28, Precision@50=0.560, Recall@50=0.003
Top@100=58, Precision@100=0.580, Recall@100=0.006
Top@200=114, Precision@200=0.570, Recall@200=0.012
Top@300=164, Precision@300=0.547, Recall@300=0.018
Top@400=216, Precision@400=0.540, Recall@400=0.023

Évaluation du prédicteur : Jaccard
 99% (13113192 of 13117502) |############################################################################### | Elapsed Time: 0:02:22 ETA:   0:00:00
Évaluation des performances :
Top@50=6, Precision@50=0.120, Recall@50=0.001
Top@100=29, Precision@100=0.290, Recall@100=0.003
Top@200=59, Precision@200=0.295, Recall@200=0.006
Top@300=94, Precision@300=0.313, Recall@300=0.010
Top@400=119, Precision@400=0.297, Recall@400=0.013

Évaluation du prédicteur : AdamicAdar
 99% (13109360 of 13117502) |############################################################################### | Elapsed Time: 0:02:36 ETA:   0:00:00
Évaluation des performances :
Top@50=26, Precision@50=0.520, Recall@50=0.003
Top@100=55, Precision@100=0.550, Recall@100=0.006
Top@200=112, Precision@200=0.560, Recall@200=0.012
Top@300=164, Precision@300=0.547, Recall@300=0.018
Top@400=211, Precision@400=0.527, Recall@400=0.023

Évaluation sur le graphe : data/data/Lehigh96.gml avec une fraction de 0.05 des arêtes supprimées
Nombre d'arêtes supprimées : 9917
Nombre de paires de nœuds non connectés : 12676699

Évaluation du prédicteur : CommonNeighbors
 99% (12665354 of 12676699) |############################################################################### | Elapsed Time: 0:01:34 ETA:   0:00:00
Évaluation des performances :
Top@50=24, Precision@50=0.480, Recall@50=0.002
Top@100=47, Precision@100=0.470, Recall@100=0.005
Top@200=80, Precision@200=0.400, Recall@200=0.008
Top@300=115, Precision@300=0.383, Recall@300=0.012
Top@400=147, Precision@400=0.367, Recall@400=0.015

Évaluation du prédicteur : Jaccard
 99% (12667993 of 12676699) |############################################################################### | Elapsed Time: 0:02:29 ETA:   0:00:00
Évaluation des performances :
Top@50=17, Precision@50=0.340, Recall@50=0.002
Top@100=47, Precision@100=0.470, Recall@100=0.005
Top@200=92, Precision@200=0.460, Recall@200=0.009
Top@300=118, Precision@300=0.393, Recall@300=0.012
Top@400=160, Precision@400=0.400, Recall@400=0.016

Évaluation du prédicteur : AdamicAdar
 99% (12672878 of 12676699) |############################################################################### | Elapsed Time: 0:02:39 ETA:   0:00:00
Évaluation des performances :
Top@50=22, Precision@50=0.440, Recall@50=0.002
Top@100=42, Precision@100=0.420, Recall@100=0.004
Top@200=72, Precision@200=0.360, Recall@200=0.007
Top@300=108, Precision@300=0.360, Recall@300=0.011
Top@400=141, Precision@400=0.352, Recall@400=0.014

Évaluation sur le graphe : data/data/Bowdoin47.gml avec une fraction de 0.05 des arêtes supprimées
Nombre d'arêtes supprimées : 4219
Nombre de paires de nœuds non connectés : 2449958

Évaluation du prédicteur : CommonNeighbors
 99% (2438734 of 2449958) |################################################################################# | Elapsed Time: 0:00:15 ETA:   0:00:00
Évaluation des performances :
Top@50=22, Precision@50=0.440, Recall@50=0.005
Top@100=44, Precision@100=0.440, Recall@100=0.010
Top@200=75, Precision@200=0.375, Recall@200=0.018
Top@300=94, Precision@300=0.313, Recall@300=0.022
Top@400=115, Precision@400=0.287, Recall@400=0.027

Évaluation du prédicteur : Jaccard
 99% (2443727 of 2449958) |################################################################################# | Elapsed Time: 0:00:24 ETA:   0:00:00
Évaluation des performances :
Top@50=21, Precision@50=0.420, Recall@50=0.005
Top@100=36, Precision@100=0.360, Recall@100=0.009
Top@200=65, Precision@200=0.325, Recall@200=0.015
Top@300=97, Precision@300=0.323, Recall@300=0.023
Top@400=121, Precision@400=0.302, Recall@400=0.029

Évaluation du prédicteur : AdamicAdar
 99% (2443711 of 2449958) |################################################################################# | Elapsed Time: 0:00:32 ETA:   0:00:00
Évaluation des performances :
Top@50=21, Precision@50=0.420, Recall@50=0.005
Top@100=46, Precision@100=0.460, Recall@100=0.011
Top@200=78, Precision@200=0.390, Recall@200=0.018
Top@300=96, Precision@300=0.320, Recall@300=0.023
Top@400=122, Precision@400=0.305, Recall@400=0.029

Évaluation sur le graphe : data/data/Mich67.gml avec une fraction de 0.05 des arêtes supprimées
Nombre d'arêtes supprimées : 4095
Nombre de paires de nœuds non connectés : 6932834

Évaluation du prédicteur : CommonNeighbors
 99% (6925564 of 6932834) |################################################################################# | Elapsed Time: 0:00:33 ETA:   0:00:00
Évaluation des performances :
Top@50=21, Precision@50=0.420, Recall@50=0.005
Top@100=37, Precision@100=0.370, Recall@100=0.009
Top@200=64, Precision@200=0.320, Recall@200=0.016
Top@300=88, Precision@300=0.293, Recall@300=0.021
Top@400=116, Precision@400=0.290, Recall@400=0.028

Évaluation du prédicteur : Jaccard
 99% (6930561 of 6932834) |################################################################################# | Elapsed Time: 0:00:50 ETA:   0:00:00
Évaluation des performances :
Top@50=14, Precision@50=0.280, Recall@50=0.003
Top@100=34, Precision@100=0.340, Recall@100=0.008
Top@200=69, Precision@200=0.345, Recall@200=0.017
Top@300=90, Precision@300=0.300, Recall@300=0.022
Top@400=115, Precision@400=0.287, Recall@400=0.028

Évaluation du prédicteur : AdamicAdar
 99% (6923806 of 6932834) |################################################################################# | Elapsed Time: 0:00:50 ETA:   0:00:00
Évaluation des performances :
Top@50=22, Precision@50=0.440, Recall@50=0.005
Top@100=39, Precision@100=0.390, Recall@100=0.010
Top@200=69, Precision@200=0.345, Recall@200=0.017
Top@300=97, Precision@300=0.323, Recall@300=0.024
Top@400=122, Precision@400=0.305, Recall@400=0.030

Évaluation sur le graphe : data/data/Tufts18.gml avec une fraction de 0.05 des arêtes supprimées
Nombre d'arêtes supprimées : 12486
Nombre de paires de nœuds non connectés : 22017220

Évaluation du prédicteur : CommonNeighbors
 99% (22008857 of 22017220) |############################################################################### | Elapsed Time: 0:02:52 ETA:   0:00:00
Évaluation des performances :
Top@50=41, Precision@50=0.820, Recall@50=0.003
Top@100=71, Precision@100=0.710, Recall@100=0.006
Top@200=123, Precision@200=0.615, Recall@200=0.010
Top@300=146, Precision@300=0.487, Recall@300=0.012
Top@400=172, Precision@400=0.430, Recall@400=0.014

Évaluation du prédicteur : Jaccard
 99% (22007324 of 22017220) |############################################################################### | Elapsed Time: 0:04:35 ETA:   0:00:00
Évaluation des performances :
Top@50=6, Precision@50=0.120, Recall@50=0.000
Top@100=30, Precision@100=0.300, Recall@100=0.002
Top@200=84, Precision@200=0.420, Recall@200=0.007
Top@300=106, Precision@300=0.353, Recall@300=0.008
Top@400=150, Precision@400=0.375, Recall@400=0.012

Évaluation du prédicteur : AdamicAdar
 99% (22009195 of 22017220) |############################################################################### | Elapsed Time: 0:04:37 ETA:   0:00:00
Évaluation des performances :
Top@50=41, Precision@50=0.820, Recall@50=0.003
Top@100=72, Precision@100=0.720, Recall@100=0.006
Top@200=125, Precision@200=0.625, Recall@200=0.010
Top@300=153, Precision@300=0.510, Recall@300=0.012
Top@400=178, Precision@400=0.445, Recall@400=0.014

Évaluation sur le graphe : data/data/Hamilton46.gml avec une fraction de 0.05 des arêtes supprimées
Nombre d'arêtes supprimées : 4819
Nombre de paires de nœuds non connectés : 2579942

Évaluation du prédicteur : CommonNeighbors
 99% (2574522 of 2579942) |################################################################################# | Elapsed Time: 0:00:19 ETA:   0:00:00
Évaluation des performances :
Top@50=21, Precision@50=0.420, Recall@50=0.004
Top@100=35, Precision@100=0.350, Recall@100=0.007
Top@200=64, Precision@200=0.320, Recall@200=0.013
Top@300=92, Precision@300=0.307, Recall@300=0.019
Top@400=114, Precision@400=0.285, Recall@400=0.024

Évaluation du prédicteur : Jaccard
 99% (2572863 of 2579942) |################################################################################# | Elapsed Time: 0:00:26 ETA:   0:00:00
Évaluation des performances :
Top@50=28, Precision@50=0.560, Recall@50=0.006
Top@100=57, Precision@100=0.570, Recall@100=0.012
Top@200=94, Precision@200=0.470, Recall@200=0.020
Top@300=127, Precision@300=0.423, Recall@300=0.026
Top@400=158, Precision@400=0.395, Recall@400=0.033

Évaluation du prédicteur : AdamicAdar
 99% (2578627 of 2579942) |################################################################################# | Elapsed Time: 0:00:38 ETA:   0:00:00
Évaluation des performances :
Top@50=23, Precision@50=0.460, Recall@50=0.005
Top@100=39, Precision@100=0.390, Recall@100=0.008
Top@200=66, Precision@200=0.330, Recall@200=0.014
Top@300=97, Precision@300=0.323, Recall@300=0.020
Top@400=123, Precision@400=0.307, Recall@400=0.026

Évaluation sur le graphe : data/data/Vassar85.gml avec une fraction de 0.05 des arêtes supprimées
Nombre d'arêtes supprimées : 5958
Nombre de paires de nœuds non connectés : 4591575

Évaluation du prédicteur : CommonNeighbors
 99% (4589715 of 4591575) |################################################################################# | Elapsed Time: 0:00:34 ETA:   0:00:00
Évaluation des performances :
Top@50=22, Precision@50=0.440, Recall@50=0.004
Top@100=40, Precision@100=0.400, Recall@100=0.007
Top@200=69, Precision@200=0.345, Recall@200=0.012
Top@300=92, Precision@300=0.307, Recall@300=0.015
Top@400=110, Precision@400=0.275, Recall@400=0.018

Évaluation du prédicteur : Jaccard
 99% (4582179 of 4591575) |################################################################################# | Elapsed Time: 0:00:47 ETA:   0:00:00
Évaluation des performances :
Top@50=22, Precision@50=0.440, Recall@50=0.004
Top@100=46, Precision@100=0.460, Recall@100=0.008
Top@200=95, Precision@200=0.475, Recall@200=0.016
Top@300=135, Precision@300=0.450, Recall@300=0.023
Top@400=158, Precision@400=0.395, Recall@400=0.027

Évaluation du prédicteur : AdamicAdar
 99% (4583889 of 4591575) |################################################################################# | Elapsed Time: 0:00:59 ETA:   0:00:00
Évaluation des performances :
Top@50=25, Precision@50=0.500, Recall@50=0.004
Top@100=45, Precision@100=0.450, Recall@100=0.008
Top@200=70, Precision@200=0.350, Recall@200=0.012
Top@300=98, Precision@300=0.327, Recall@300=0.016
Top@400=122, Precision@400=0.305, Recall@400=0.020

Évaluation sur le graphe : data/data/Vermont70.gml avec une fraction de 0.05 des arêtes supprimées
Nombre d'arêtes supprimées : 9561
Nombre de paires de nœuds non connectés : 26620522

Évaluation du prédicteur : CommonNeighbors
 99% (26615806 of 26620522) |############################################################################### | Elapsed Time: 0:02:53 ETA:   0:00:00
Évaluation des performances :
Top@50=33, Precision@50=0.660, Recall@50=0.003
Top@100=64, Precision@100=0.640, Recall@100=0.007
Top@200=120, Precision@200=0.600, Recall@200=0.013
Top@300=167, Precision@300=0.557, Recall@300=0.017
Top@400=194, Precision@400=0.485, Recall@400=0.020

Évaluation du prédicteur : Jaccard
 99% (26619896 of 26620522) |############################################################################### | Elapsed Time: 0:04:39 ETA:   0:00:00
Évaluation des performances :
Top@50=19, Precision@50=0.380, Recall@50=0.002
Top@100=45, Precision@100=0.450, Recall@100=0.005
Top@200=94, Precision@200=0.470, Recall@200=0.010
Top@300=120, Precision@300=0.400, Recall@300=0.013
Top@400=162, Precision@400=0.405, Recall@400=0.017

Évaluation du prédicteur : AdamicAdar
 99% (26615466 of 26620522) |############################################################################### | Elapsed Time: 0:04:23 ETA:   0:00:00
Évaluation des performances :
Top@50=35, Precision@50=0.700, Recall@50=0.004
Top@100=61, Precision@100=0.610, Recall@100=0.006
Top@200=117, Precision@200=0.585, Recall@200=0.012
Top@300=161, Precision@300=0.537, Recall@300=0.017
Top@400=198, Precision@400=0.495, Recall@400=0.021

Évaluation sur le graphe : data/data/Rice31.gml avec une fraction de 0.05 des arêtes supprimées
Nombre d'arêtes supprimées : 9241
Nombre de paires de nœuds non connectés : 8157818

Évaluation du prédicteur : CommonNeighbors
 99% (8155842 of 8157818) |################################################################################# | Elapsed Time: 0:01:02 ETA:   0:00:00
Évaluation des performances :
Top@50=45, Precision@50=0.900, Recall@50=0.005
Top@100=77, Precision@100=0.770, Recall@100=0.008
Top@200=136, Precision@200=0.680, Recall@200=0.015
Top@300=192, Precision@300=0.640, Recall@300=0.021
Top@400=246, Precision@400=0.615, Recall@400=0.027

Évaluation du prédicteur : Jaccard
 99% (8156826 of 8157818) |################################################################################# | Elapsed Time: 0:01:41 ETA:   0:00:00
Évaluation des performances :
Top@50=16, Precision@50=0.320, Recall@50=0.002
Top@100=41, Precision@100=0.410, Recall@100=0.004
Top@200=79, Precision@200=0.395, Recall@200=0.009
Top@300=123, Precision@300=0.410, Recall@300=0.013
Top@400=163, Precision@400=0.407, Recall@400=0.018

Évaluation du prédicteur : AdamicAdar
 99% (8157130 of 8157818) |################################################################################# | Elapsed Time: 0:02:05 ETA:   0:00:00
Évaluation des performances :
Top@50=45, Precision@50=0.900, Recall@50=0.005
Top@100=77, Precision@100=0.770, Recall@100=0.008
Top@200=139, Precision@200=0.695, Recall@200=0.015
Top@300=196, Precision@300=0.653, Recall@300=0.021
Top@400=251, Precision@400=0.627, Recall@400=0.027
agnes@agnes-XPS-9315:~/NET4103/Projet/NET4103_Projet$ 

## 5.

## 6.

