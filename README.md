# vulnera
Tout d'abord vous pouvez télécharger le fichier ou copier le code puis l'enregistrer dans un fichier avec le nom que vous voulez mais avec l'extension ` .py`

`Lien du fichier vulnera.py`

https://github.com/meridimm/vulnera/blob/main/vulnera.py
.
.
.
```markdown
# Analyse de vulnérabilités

Ce programme est conçu pour effectuer une analyse de vulnérabilités sur une adresse IP spécifique en utilisant l'outil Nmap.

## Installation

- Assurez-vous d'avoir Python installé sur votre système.
- Installez les bibliothèques nécessaires en exécutant les commandes suivantes :

  ```
  pip install python-nmap
  ```

## Utilisation

1. Clonez ce référentiel sur votre ordinateur ou téléchargez simplement le fichier `vulnera.py`.

2. Exécutez le programme en exécutant la commande suivante :

   ```
   python vulnera.py
   ```

3. Une fenêtre graphique s'ouvrira. Entrez l'adresse IP que vous souhaitez analyser dans le champ de saisie.

4. Cliquez sur le bouton "Analyser" pour lancer l'analyse de vulnérabilités.

5. Les résultats de l'analyse, y compris les informations sur les ports, les services et les versions, seront affichés dans la console.

## Exemple

Voici un exemple d'utilisation du programme :

1. Exécutez le programme en suivant les étapes ci-dessus.

2. Entrez l'adresse IP `192.168.0.1` dans le champ de saisie.

3. Cliquez sur le bouton "Analyser".

4. Les résultats de l'analyse s'afficheront dans la console, montrant les ports ouverts, les services actifs et les versions correspondantes.

   ```
   Host: 192.168.0.1
   Port: 80     Service: HTTP      State: open      Version: Apache/2.4.29 (Ubuntu)
   Port: 443    Service: HTTPS     State: open      Version: OpenSSL 1.1.1g  21 Apr 2020
   Port: 22     Service: SSH       State: closed    Version: N/A
   ```

## Contribuer

Les contributions à ce projet sont les bienvenues ! N'hésitez pas à ouvrir une demande d'extraction pour proposer des améliorations ou signaler des problèmes.

## Licence

Ce projet est sous licence MIT. Veuillez consulter le fichier [LICENSE](LICENSE) pour plus de détails.

```
