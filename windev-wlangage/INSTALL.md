# Installation — skill `windev-wlangage`

Skill de référence WLangage (dictionnaire Markdown). Aucune dépendance à
installer : la consultation se fait par lecture/recherche dans les fichiers
Markdown.

## Installer comme skill Claude Code

Copie ce dossier (nommé `windev-wlangage`) dans l'un de ces emplacements :

- **Global (tous projets)** :
  `~/.claude/skills/windev-wlangage/`
  (Windows : `%USERPROFILE%\.claude\skills\windev-wlangage\`)
- **Projet** :
  `<projet>/.claude/skills/windev-wlangage/`

Le fichier `SKILL.md` (avec son frontmatter `name` / `description`) doit se
trouver à la racine de ce dossier.

## Vérifier

1. Lance Claude Code dans un projet.
2. Le skill `windev-wlangage` doit apparaître (commande `/`).
3. Pose une question, par ex. « quelle est la syntaxe de HExécuteRequêteSQL ? » :
   le skill ouvre la rubrique correspondante dans `pages/`.

## Utilisation

Voir [`README.md`](README.md) pour la structure et la procédure de recherche,
ou directement [`INDEX.md`](INDEX.md) (sommaire et index principaux).

## Viewer de code coloré (inclus)

Le sous-dossier [`viewer/`](viewer/) contient un visualiseur HTML qui affiche du
code WLangage **coloré** aux couleurs de l'éditeur PC SOFT (utile pour relire un
code généré). Lancement :

```powershell
cd windev-wlangage/viewer
python -m http.server 8754
```
Puis ouvrir http://localhost:8754. Voir [`viewer/README.md`](viewer/README.md).
