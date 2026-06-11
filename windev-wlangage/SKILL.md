---
name: windev-wlangage
description: >-
  Dictionnaire de référence WLangage (PC SOFT 2025 — WINDEV, WEBDEV, WINDEV
  Mobile) au format Markdown : 11 666 rubriques dont 5 950 fonctions,
  1 051 propriétés, 399 types de variables, 31 mots réservés, 414 exemples de
  code, 148 syntaxes préfixées et 76 fonctions de langage externe. À utiliser
  pour rechercher la signature exacte, les paramètres, les constantes, les
  remarques et des exemples d'une fonction, propriété, type de variable, mot
  réservé ou champ du WLangage, ou pour vérifier la disponibilité d'un élément
  par plateforme. Renvois croisés navigables (~99,95 %), index des signatures
  et regroupement par famille. Déclencheurs : syntaxe/paramètres d'une fonction
  Hxxx, gxxx, fonctions chaîne/date/HFSQL/REST, propriété de champ, constante,
  ou « est-ce dispo en WEBDEV/Android ».
---

# Dictionnaire WLangage 2025 (WINDEV / WEBDEV / WINDEV Mobile)

Référence Markdown du WLangage, en français. Sert de **source de référence**
pour la signature exacte, les paramètres, les constantes et les exemples du
WLangage. À combiner avec un skill d'écriture de code WLangage.

## Contenu

- **11 666 rubriques**, dont 5 950 fonctions, 1 051 propriétés, 399 types de
  variables, 414 exemples, 31 mots réservés, ainsi que des champs et concepts.
- Une rubrique = un fichier `pages/<id>.md`.
- Couverture WINDEV / WEBDEV / WINDEV Mobile 2025 (le frontmatter `source_help`
  indique, par rubrique, les produits concernés).

## Comment chercher (procédure)

1. **POINT D'ENTRÉE n°1 — `index/lookup.tsv`** : un seul fichier, **une ligne par
   rubrique**, colonnes TAB `id  type  nom_FR  nom_EN  module  signature`. Faire
   **un seul grep** dessus (nom FR **ou** anglais) pour trouver n'importe quelle
   fonction/propriété/type/constante/mot-clé, récupérer son **id** (et la
   signature pour les fonctions) sans parcourir `pages/`.
   Exemple : `grep -i "HLitPremier" index/lookup.tsv`.
2. **Lire le détail** : ouvrir `pages/<id>.md` (depuis l'id obtenu en 1) seulement
   si la signature/desc du lookup ne suffit pas. Ne jamais charger tout `pages/`.
3. **Vérifier qu'un nom existe** (rapide) : `viewer/functions.js`,
   `viewer/constants.js`, `viewer/types.js` (sets compacts).
4. **Par domaine / famille** : [`index/categories.md`](index/categories.md) ;
   index dédiés [signatures](index/signatures.md), [fonctions](index/fonctions.md),
   [propriétés](index/proprietes.md), [types](index/types.md),
   [mots réservés](index/mots-reserves.md).

> Astuce perf : grouper plusieurs noms en un seul grep — `grep -iE "(NomA|NomB)" index/lookup.tsv`.

## Générer du code WLangage

- **Lire d'abord [`GUIDE.md`](GUIDE.md)** : charte de nommage, règles de formatage
  (déclarations en tête, corps colonne 0, alignement `est`/`=`,
  `PROCÉDURE LOCAL/GLOBAL`), bonnes pratiques (SQL paramétré anti-injection,
  gestion d'erreurs/exceptions) et **patterns vérifiés** prêts à adapter (HFSQL,
  REST/JSON, e-mail, socket, SELON, procédure interne, chaîne multiligne…).
- **[`index/cheatsheet.md`](index/cheatsheet.md)** : fonctions courantes par
  famille avec leur signature — pour coder sans recherche dans les cas usuels.
- Toujours **vérifier les identifiants** (fonctions/propriétés/constantes/types)
  dans `index/lookup.tsv` avant de les écrire.

## Structure d'une page

Frontmatter YAML exploitable pour filtrer :

```yaml
title: "ChaîneCommencePar (Fonction)"
english: "StringStartsWith"
type: "Fonction"          # Fonction | Propriété | Type de variable | Exemple | Mot réservé | ...
id: "1000018827"
module: "WDLang1"
category: "fonctions_chaine"
source_help: ["WINDEV", "WEBDEV", "WINDEV Mobile"]   # produits où la rubrique existe
```

Corps type d'une fonction : ligne **Disponible** (plateformes), Description,
**Exemple** (bloc ```` ```wlangage ````), **Syntaxe** (une section `####` par
variante + paramètres en `` `<param>` *Type* `` suivis d'une citation), tables
de **constantes**, **Remarques**, Composante, **Voir Aussi**.

## Conventions

- **Renvois croisés** : les liens `[Texte](<id>.md)` pointent vers une autre
  rubrique du dictionnaire. ~99,95 % résolvent.
- **Disponibilité plateforme** : la ligne `> **Disponible :**` liste, par
  produit, les cibles actives (Windows, Linux, Android, iPhone/iPad, PHP,
  Code Navigateur, Procédures stockées...). Un bloc `> _(...)_` en cours de
  page signale une restriction locale (ex. constante indisponible sur certaines
  cibles).
- **Code** : les blocs sont balisés ```` ```wlangage ````, mots-clés en
  français (`SI`, `POUR TOUT`, `RENVOYER`).

## Notes

- Langue : français. Version : 2025.
- À utiliser comme référence ; expliquer avec ses propres mots plutôt que de
  recopier de longs extraits.
