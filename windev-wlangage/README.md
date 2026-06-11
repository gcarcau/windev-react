# windev-wlangage

Dictionnaire de référence du **WLangage** (PC SOFT 2025 — WINDEV, WEBDEV,
WINDEV Mobile) au format Markdown, prêt à servir de skill.

> **Installation** : voir [`INSTALL.md`](INSTALL.md).

## Contenu

- **11 666 rubriques** : 5 950 fonctions, 1 051 propriétés, 399 types de
  variables, 414 exemples, 148 syntaxes préfixées, 76 fonctions de langage
  externe, 31 mots réservés, plus champs et concepts.
- Renvois croisés navigables entre rubriques (~99,95 % résolus).

## Arborescence

```
windev-wlangage/
├── SKILL.md            Définition du skill (frontmatter + mode d'emploi)
├── GUIDE.md            Guide de génération de code (charte, format, patterns vérifiés)
├── INSTALL.md          Installation
├── INDEX.md            Sommaire global + statistiques
├── index/
│   ├── lookup.tsv      Index unique (1 ligne/rubrique : id, type, nom FR/EN, module, signature) — recherche en 1 grep
│   ├── cheatsheet.md   Fonctions courantes par famille (signatures)
│   ├── signatures.md   Signatures condensées des 5 950 fonctions
│   ├── fonctions.md    Index alphabétique des fonctions (FR + anglais)
│   ├── categories.md   Fonctions regroupées par famille
│   ├── proprietes.md   Propriétés
│   ├── types.md        Types de variables
│   ├── mots-reserves.md  Mots réservés
│   └── <module>.md     Un index par module (groupé par catégorie)
├── pages/
│   └── <id>.md         Une rubrique par fichier
└── viewer/             Visualiseur de code WLangage coloré (HTML) — voir viewer/README.md
```

## Procédure de recherche

1. **Signature rapide** : `index/signatures.md` (syntaxe + description courte).
2. **Par nom** : `index/fonctions.md`, ou `grep` dans `pages/` (nom FR ou
   anglais), ex. `grep -rl "HLitPremier" pages/`.
3. **Par famille** : `index/categories.md` (chaîne, date, HFSQL, REST, JSON…).
4. **Lire la rubrique** : ouvrir le `pages/<id>.md` trouvé.

## Format d'une page

Frontmatter YAML (`title`, `english`, `type`, `id`, `module`, `category`,
`source_help`) puis le contenu : disponibilité par plateforme, description,
exemple(s) de code (```` ```wlangage ````), syntaxe(s) et paramètres, tables de
constantes, remarques, et « Voir Aussi » (liens internes).
