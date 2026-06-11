# wlangage-viewer

Aperçu **coloré** de code WLangage dans le navigateur, aux couleurs exactes de
l'éditeur PC SOFT (thème sombre + clair). Sert à visualiser/copier/exporter du
code WLangage proprement mis en forme.

## Lancer

Le viewer charge le code depuis `code.wl` via `fetch`, ce qui nécessite un
petit serveur HTTP local (sinon, ouvert en double-clic, un exemple de secours
intégré s'affiche).

```powershell
cd wlangage-viewer
python -m http.server 8753
```
Puis ouvrir http://localhost:8753 dans le navigateur.

## Afficher son propre code

Remplacer le contenu de **`code.wl`** par le code WLangage souhaité (brut, sans
échappement), puis recharger la page. Les lignes `//§ Titre` deviennent des
**séparateurs de section** (Procédure locale / globale / interne, Clic,
Sélection, Survol…).

## Fonctions

- Thème **sombre** (palette exacte PC SOFT) / **clair**, bouton **Copier**,
  **Exporter .wl** (sélecteur de fichier), **clic droit → Copier**.
- Numérotation des lignes (repart à 1 par section).
- **Alignement automatique** des déclarations (`est`) et affectations (`=`).
- Chaînes multilignes `[ … ]` rendues sur fond rosé.

## Coloration (déduite sans connaître le projet)

- Mots-clés (orange), fonctions intégrées (bleu, réf. `functions.js`), types
  (violet, réf. `types.js`), constantes (or, réf. `constants.js`).
- Variables locales (vert), globales `g…` (cyan), champs/contrôles, fichiers de
  données HFSQL et rubriques (sarcelle), procédures utilisateur (sarcelle).
- Propriétés d'un type de variable après `.` = couleur de texte par défaut ;
  sous-membres d'un `Variant`/`JSON` et rubriques de fichier = sarcelle.

## Régénérer les référentiels

`constants.js` / `types.js` / `functions.js` sont extraits du corpus de doc
`windev-wlangage` via les scripts `extract_*.py` (Python 3).
