# BBP Solver:
**Bachi , Mihoubi ,Moussaoui, Nouali , Saadi.**

## Description des documents : 
ce repo contient:
- **BPP_Solver.py**  : la classe principale, où on peut instancier un probleme du bin packing et appeler les differentes méthodes de résoulution implémentées.
- **Dossier Exact_Methods**: contient l'ensemble des methodes exactes implementées pour le BPP, et qui sont : 
    - **BB.py** : implemente la methode branch and bound pour resoudre le BPP. 
    - **BBA.py**: implemente une version améliorée du Branch & Bound. 
    - **Exhaustive.py**: implemente une recherch exhaustive. 
    - **DP.py**: résoudre le BPP avec la programmation dynamique. 
  
-  **Instances_generator.py**: fournit une fonction qui permet de generer nos propres instances, et les sauvegarder dans des fichier textes.
 - **Instances_reader.py**: permet de lire un fichier texte d'une instances et récuprer les données (n , c et la liste des objets)
 -  - **Model.py**: contient les classes Bin et Objet à utiliser par les méthodes
