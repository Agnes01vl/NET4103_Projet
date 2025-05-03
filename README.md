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

> Oui, tous ces réseaux sont peu denses, particulièrement MIT et Johns Hopkins (densité ≈ 1–2%). 

Clustering global/local mesure la tendance des voisins d’un sommet à aussi être voisins entre eux, donc la présence de triangles (groupes d'amis mutuels).

Caltech a les meilleurs scores de clustering :
- Global Clustering : 0.2913 (assez élevé)
- Mean Local Clustering : 0.4091

MIT et Johns Hopkins ont un clustering plus bas :
- Environ 0.18–0.19 global, et 0.27 en local.

> Cela suggère que Caltech a une structure fortement communautaire : des petits groupes très connectés, même si globalement le réseau reste peu dense. et le MIT et Johns Hopskins sont pus "diffuses" : il y a des liens, mais moins de triangles fermés, donc moins de petits groupes très soudés.

### (c) diagramme de dispersion

#### Caltech (avec 762 nœuds dans la LCC)
![Caltech Degree Distribution](degree_clustering_plots/Caltech_degree_vs_clustering.png)

#### MIT(qui a 6402 nœuds dans la LCC)
![MIT Degree Distribution](degree_clustering_plots/MIT_degree_vs_clustering.png)

#### Johns Hopkins (qui a 5157 nœuds dans la LCC)
![Johns Hopkins Degree Distribution](degree_clustering_plots/Johns_Hopkins_degree_vs_clustering.png)


des conclusions sur les similitudes ou les différences entre les réseaux d'arbres ? Quelles autres observations pouvez-vous faire ?

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


## 4. Link Prediction 

Dans cette section, nous avons évalué les performances de trois métriques de prédiction de liens sur 12 graphes issus du dataset Facebook100 :

* **Common Neighbors**
* **Jaccard**
* **Adamic/Adar**

On a annalyser les 12 graphes suivants:
- Princeton12.gml,
- Caltech36.gml,
- Oberlin44.gml,
- Johns Hopkins55.gml,
- Lehigh96.gml,
- Bowdoin47.gml,
- Mich67.gml, 
- Tufts18.gml, 
- Hamilton46.gml, 
- Vassar85.gml, 
- Vermont70.gml,  
- Rice31.gml,

Les prédictions ont été réalisées pour plusieurs valeurs de `k`, avec une fraction de test de 0.5. Les résultats sont stockés dans `Q4_prediction.csv` et analysés via le script `analyse_Q4_prediction.py`.

### Résultats globaux

| Prédicteur      | Précision moyenne | Recall moyen |
| --------------- | ----------------- | ------------ |
| AdamicAdar      | **0.468**         | **0.0177**   |
| CommonNeighbors | 0.463             | 0.0173       |
| Jaccard         | 0.343             | 0.0150       |

>  Adamic/Adar est légèrement meilleur, suivi de très près par Common Neighbors. Jaccard, en revanche, montre des performances sensiblement plus faibles, particulièrement en précision.

| Prédicteur      | Écart-type Précision | Écart-type Recall |
| --------------- | -------------------- | ----------------- |
| AdamicAdar      | 0.147                | 0.021             |
| CommonNeighbors | 0.153                | 0.020             |
| Jaccard         | **0.100**            | **0.017**         |

> Jaccard montre des performances plus stables mais plus faibles, tandis qu’Adamic/Adar et Common Neighbors ont des variations plus fortes, mais atteignent de meilleures précisions.

### Diagrammes et interprétations

#### Précision (Boxplot)
![moustache précision](annalyse_link_prediction/Distribution_precision.png)

* Adamic/Adar et Common Neighbors ont des distributions similaires, bien centrées et relativement étroites.
* Jaccard présente une précision nettement inférieure, notamment pour les petites valeurs de k (où la précision est cruciale).

> Pour des petits k, Adamic/Adar et Common Neighbors sont préférables.

#### Recall (Boxplot)
![moustache recall](annalyse_link_prediction/Distribution_recall_sans_outliers.png)

* Le recall augmente globalement avec k, pour tous les prédicteurs et Les boîtes s’élargissent avec k, traduisant une variabilité croissante.
* Jaccard montre une plus grande dispersion, sans compenser par une meilleure performance.

> L’augmentation du recall avec k est attendue, mais elle n’est pas suffisante pour compenser la faiblesse du prédicteur Jaccard.

#### Densité – Rappel
![densité recall](annalyse_link_prediction/Densité_Recall_Prédicteur.png)

* Les trois prédicteurs montrent une forme de distribution similaire.
* Adamic/Adar et Common Neighbors ont une densité légèrement plus concentrée autour de meilleurs scores.

#### Densité – Précision
![densité précision](annalyse_link_prediction/Densité_Precision_Prédicteur.png)

* La densité de **Jaccard** est fortement concentrée autour de **valeurs basses**, ce qui confirme ses faibles performances.
* Adamic/Adar et Common Neighbors présentent une **plus large gamme de précision**, incluant des scores plus élevés (jusqu’à 1.2), signe de meilleures prédictions ponctuelles.

---

>* **Adamic/Adar** et **Common Neighbors** sont **globalement comparables**, avec un léger avantage pour Adamic/Adar.
>* **Jaccard** est **nettement moins performant**, bien qu’un peu plus stable.
>* Pour de **petits `k`**, la **précision** est cruciale : Adamic/Adar est ici le plus fiable.
>* À mesure que `k` augmente, les trois prédicteurs gagnent en stabilité, mais leurs performances relatives restent constantes.

## 4. LinkPrediction



### (b) 
Voir sol_Q4.py où l'on trouve:

- class CommonNeighbors(LinkPrediction):
- class Jaccard(LinkPrediction):
- class AdamicAdar(LinkPrediction):



 Voici un diagramme moutache qui annalyse la précision: 
 ![moustache](annalyse_link_prediction/Distribution_precision.png)


On observe que Common Neighbors et Adamic-Adar sont très proches en termes de performance et assez stables pour tout les K.Jaccard a des performances nettement inférieures, surtout pour K faible (où la précision est cruciale).

> Cela confirme que Jaccard est un moins bon prédicteur.


Les boîtes (IQR) de CommonNeighbors et AdamicAdar sont plus larges pour K faibles, ce qui indique une plus grande variabilité. À mesure que K augmente, les prédicteurs semblent se stabiliser autour d’une précision plus faible, mais plus homogène. Surtout Jaccard qui est bien plus stable mais pour de moins résultat que les deux autre prédicteurs.

> Cela suggère que pour K élevé, les prédicteurs deviennent plus prévisibles, mais moins efficaces.

 Voici le diagramme moutache qui annalyse du recall: 
 ![moustache](annalyse_link_prediction/Distribution_recall_sans_outliers.png)

 On obserse ici que les boites sont vraiment toute petite pour k faible et augmente en taille avec la valeur de K.
 On voit en général que jaccard à des boites plus grandes que Common Neighbors ou Adamicar. Les valeurs sont plus répartie pour lui.
 Toute les valeurs moyenne augement vec le K celle de Jaccard et toujours plus petite que ces deux voisins.

Et Voici une annalyse de la densité du recall : 
 ![densité prédicteur](annalyse_link_prediction/Densité_Recall_Prédicteur.png)

Ici pour la sensité du recall pour les trois prédicteirs ils ont à peux prés la même forme avec une densité un peu plus haute pour 
la densité du 
![densité prédicteur](annalyse_link_prediction/Densité_Precision_Prédicteur.png)

  on voit ici pour jaccar une desité bien plus haute et très différente de celle des deux autre prédicteurs avec unes moyenne bien plus basse du recall et le recall fini à une valeur de 0.7 alors que pour les deux autres : cela va jusqu'à 1.2 !



## 5. Label Propagation

On a commencer par annalyser un petit graphe:Caltech à seulement 768 noeuds.

| Fraction enlevée | Dorm  | Major | Gender |
| ---------------- | ----- | ----- | ------ |
| 0.10             | 0.347 | 0.262 | 0.425  |
| 0.20             | 0.325 | 0.267 | 0.435  |
| 0.30             | 0.334 | 0.261 | 0.429  |

**Tableau 1 : Accuracy de l’algorithme de Label Propagation**

| Fraction enlevée | Dorm  | Major | Gender |
| ---------------- | ----- | ----- | ------ |
| 0.10             | 14.99 | 14.34 | 0.578  |
| 0.20             | 15.12 | 14.47 | 0.576  |
| 0.30             | 15.11 | 14.31 | 0.579  |

**Tableau 2 : MAE (Mean Absolute Error) du Label Propagation**


1. **Gender** :
  - Donne les meilleurs résultats parmi les trois attributs.
   * L'accuracy reste relativement stable (entre 0.425 et 0.435), même quand on augmente la proportion de données manquantes.
   * L'erreur MAE est très faible (proche de 0.57), ce qui indique que les classes sont bien préservées même en cas de données absentes.

2. **Dorm** :
  - Affiche une précision plus élevée que "major", mais moins bonne que "gender".
   * L'accuracy chute légèrement de 0.347 à 0.325 puis se stabilise à 0.334, ce qui peut indiquer que certaines structures communautaires du graphe aident à la prédiction.
   * L’erreur MAE est plus élevée (≈15), ce qui suggère qu’il y a beaucoup de classes ou que les classes sont déséquilibrées.

3. **Major** :
  - C’est l’attribut le plus difficile à prédire. L’accuracy est faible (\~0.26) et très peu influencée par le taux de données manquantes.
   * Cela suggère que cet attribut est moins corrélé à la structure du graphe (moins homophilique).


Le label propagation est plus efficace pour prédire les attributs fortement **corrélés à la structure du graphe**, comme le **genre**, souvent associé à des clusters clairs (e.g., fraternités/sororités, groupes d’intérêt). En revanche, des attributs comme la spécialisation universitaire (**major**) semblent moins bien structurés dans le graphe, d'où les résultats plus faibles.

Nous pouvons annalyser ce graphe aussi pour un grand nombre de graphes: 
- Princeton12.gml,
- Caltech36.gml,
- Oberlin44.gml,
- Johns Hopkins55.gml,
- Lehigh96.gml,
- Bowdoin47.gml,
- Mich67.gml, 
- Tufts18.gml, 
- Hamilton46.gml, 
- Vassar85.gml, 
- Vermont70.gml,  
- Rice31.gml,

### 1. Graphique du MAE par attribut et fraction de labels supprimés 
![MAEattribut](analyse_label_propagation/boxplot_mae_par_attribut.png)

Ce graphique montre la **distribution du MAE** (erreur absolue moyenne) pour trois attributs (`dorm`, `major`, `gender`) à différents niveaux de suppression de labels (`0.1`, `0.2`, `0.3`).On constate que:

  - **`major`** a des MAE très élevés, de l’ordre de 10 à plus de 40, ce qui suggère qu’il est beaucoup plus difficile à prédire correctement (boite très large), même avec peu de labels manquants.
  - **`dorm`** a des MAE intermédiaires, généralement entre 2 et 17.
  - **`gender`** est très bas (MAE proche de 0), ce qui est logique car c’est un attribut binaire (fille garçon): la prédiction est plus facile.

### 2. Graphique de l’Accuracy par attribut et fraction de labels supprimés 
![MAEattribut](analyse_label_propagation/boxplot_accuracy_par_attribut.png)


Ce graphique représente la **précision de la prédiction** (accuracy) pour les mêmes attributs et fractions de suppression. On constate que:

  - **`gender`** a les meilleurs résultats (entre \~0.45 et 0.7), ce qui renforce l'idée qu’il est plus facile à prédire.
  - **`dorm`** est moyen (\~0.3 à 0.5), ce qui est cohérent avec ses MAE modérés.
  - **`major`** est difficile à prédire (accuracy \~0.1 à 0.3).
On observe aussi un comportement assez stable dans ce graphe. Les performances se dégradent peu entre les niveaux 0.1, 0.2 et 0.3, surtout pour `gender`, ce qui indique une **robustesse à la suppression** des labels pour cet attribut.


### 3. Visualisation de la densité de l'Accuracy
![Densité Accuracy](analyse_label_propagation/densite_accuracy_par_attribut_moyenne.png)

Le graphique ci-dessus montre la densité de l’accuracy pour chaque attribut (`dorm`, `gender`, `major`) avec les lignes pointillées indiquant la moyenne :

* La courbe bleue (`gender`) est centrée autour de 0.51, ce qui confirme qu’il est globalement bien prédit.
* La courbe verte (`dorm`) est centrée autour de 0.35, avec une répartition plus large.
* La courbe orange (`major`) est concentrée autour de 0.17, avec une distribution très basse, confirmant une performance médiocre.

> Ce graphe souligne visuellement que plus l’attribut est simple (moins de classes, mieux défini), meilleures sont les performances.

###
> Finalement le plus facile à prédir est le  `gender` ensuite `dorm` et finalement `major` est le plus difficile. de plus on peut dire que `gender` n’ait que 2 classes, `dorm` un nombre modéré, et `major` un très grand nombre, expliquant ces différences.

