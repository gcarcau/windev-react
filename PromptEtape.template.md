# Template — Prompt d'étape (Cowork → Claude Code)

> Modèle à copier/adapter par Cowork pour chaque tâche de la boucle de travail.

---

Avant de commencer :
- Lis `CLAUDE.md`.
- Lis `docs/runbooks/passation.md` (dernier handoff).
- Lis la fiche de cartographie concernée : `docs/cartographie/<fichier>.md`.

## Contexte

<Rappel bref de l'étape de roadmap, et de ce qui existe déjà.>

## Référence visuelle

<Si écran : `origine/screenshoot/<nom-ecran>.png` — capture de l'écran WinDev d'origine. Niveau de fidélité attendu : <pixel-perfect | comportement équivalent avec le design system choisi>.>

## Tâche

<Description précise et actionnable. Ex :
- Créer la route `/clients` (apps/web) affichant la liste des clients.
- Créer l'endpoint `GET /api/clients` (apps/api) avec pagination.
- Réutiliser le composant `<DataTable>` existant si présent.
- Champs à afficher : <liste, avec mapping depuis `docs/cartographie/entites.md`>.
- Règle métier à respecter : <référence à `docs/cartographie/regles-metier.md`>.>

## Critères d'acceptation

- [ ] <critère fonctionnel 1>
- [ ] <critère fonctionnel 2>
- [ ] Composant accessible (labels, navigation clavier de base)
- [ ] Cohérent avec le design system du projet

## Clôture

- Lance `pnpm lint`, `pnpm build` (front + API concernés), tests unitaires et E2E pertinents.
- Corrige jusqu'à ce que tout passe.
- Commit + push.
- Mets à jour `docs/runbooks/passation.md` (utiliser `templates/passation.template.md`).
- Mets à jour le statut de l'étape dans `docs/roadmap.md`.
