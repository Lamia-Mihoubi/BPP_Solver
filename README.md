# BBP Solver:
**Bachi , Mihoubi ,Moussaoui, Nouali , Saadi.**

## Description des documents : 
Ce repository contient:\
-**BPP_Solver.py**    : la classe principale, où on peut instancier un problème du bin packing et appeler les différentes méthodes de résolution implémentées.\
 
-**Dossier Exact_Methods**  : contient l'ensemble des méthodes exactes implémentées pour le BPP, et qui sont :\
    -**BB.py**  : implemente la methode branch and bound pour résoudre le BPP.\
    -**BBA.py** : implemente une version améliorée du Branch & Bound.\
    -**Exhaustive.py**  : implemente une recherch exhaustive.\
    -**DP.py**  : résoudre le BPP avec la programmation dynamique.\
    
-**Dossier Méthodes_Heuristiques**  : contient l'ensemble des méthodes heuristiques implementées pour le BPP, et qui sont :\
    -**FF_FFD.py**  : implémente les deux méthodes Fisrt Fit, et First Fit Decreasing.\
    -**BF_BFD.py**  :implémente les deux méthodes Best Fit, et Best Fit Decreasing.\
    -**NF_NFD.py**  :implémente les deux méthodes Next Fit, et Next Fit Decreasing.\
     
-**Dossier Méta_heuristiques**  : contient l'ensemble des méthodes Métaheuristiques implémentées pour le BPP, et qui sont :\
    -**AG.py**  : implémente l’Algorithme Génétique.\
    -**Recuit_Sim.py**  :implémente le recuit Simulé.\
    -**WOA.py** :implémente le Whale Optimisation Algorithm.\
    -**ILWOA.py**   : implément le Improved lévy Whale Optimisation Algorithm.\
     
-**Dossier Hybridation**    : contient l'ensemble des méthodes hybrides implémentées pour le BPP, et qui sont:\
    -**HRH_WOA_RS.py**  :Hybridation haut niveau de WOA suivi de RS.\
    -**HRH_ILWOA_RS.py**    :Hybridation haut niveau de ILWOA suivi de RS.\
    -**AG_MIX_RS.py**   : Hybridation de AG, avec plusieurs métaheuristiques pour la génération de la population initiale, et RS pour l'intensification de la solution trouvée.\
    -**AG_RS_RS.py**    : Hybridation de AG, avec l’ajout de l’étape de RS après la mutation, et RS pour l'intensification de la solution trouvée.\
    -**HRH_AG_RS.py**   : Hybridation haut niveau de AG, et RS pour l'intensification de la solution trouvée.\
    -**HLRH_AG.py** : Hybridation de AG,  avec plusieurs métaheuristiques pour la génération de la population initiale.\
    
-**Instances_generator.py** : fournit une fonction qui permet de générer nos propres instances, et les sauvegarder dans des fichier textes.\
 
-**Instances_reader.py**    : permet de lire un fichier texte d'une instances et récupérer les données (n , c et la liste des objets).\
 
-**Model.py**   : contient les classes Bin et Objet à utiliser par les méthodes.\
 
-**Dossier plateforme** : contient le code source de la plateforme du BPP solver (React.JS ,Flask).\
 
-**Dossier Rapport**    : contient le rapport de la conception et des tests du BPP solver. (LateX code).\
 
-**Dossier article**    : contient l’article de la méthode hybride proposée.\
 
-**Tests**  : contient les résultats des tests des différentes méthodes implémentées. \
 
 
 ## Références du code:
- **Métaheuristique WOA:** https://github.com/docwza/woa
