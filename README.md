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

## (c) diagramme de dispersion

(1 point) Pour chaque réseau, dessinez également un diagramme de dispersion du degré en fonction du coefficient de regroupement local. Sur la base de ces calculs et des précédents, êtes-vous en mesure de tirer des conclusions sur les similitudes ou les différences entre les réseaux d'arbres ? Quelles autres observations pouvez-vous faire ?

