# 04 — Mémoire projet (anatomie)

La qualité de la migration dépend de la **mémoire persistante** du projet : ce que Claude Code lit avant chaque tâche, et ce que Cowork relit après.

## `CLAUDE.md` (racine du dépôt)

Le fichier que Claude Code lit en premier. Doit contenir :

- **Vue d'ensemble** : nom de l'app, objectif, état d'avancement (lien vers la roadmap).
- **Stack** : React (Vite/Next.js), TypeScript, design system choisi, state management, backend/API, base de données.
- **Conventions** : structure des dossiers (`apps/web/src/...`), conventions de nommage des composants, gestion des routes, gestion des appels API (ex: hooks `useXxxQuery`).
- **Commandes** : `pnpm dev`, `pnpm build`, `pnpm lint`, `pnpm test`, `pnpm exec playwright test`.
- **Règles non négociables** : pas d'accès DB direct depuis le front, pas de secrets en clair, etc. (cf. `01-principes-et-roles.md`).
- **Pointeurs** : vers `docs/roadmap.md`, `docs/adr/`, `docs/runbooks/passation.md`.

Généré une première fois à l'étape 2, puis **mis à jour à chaque étape majeure**.

## `docs/`

```
docs/
├── roadmap.md              # liste des étapes, statut (à faire / en cours / fait)
├── cartographie/            # fiches de synthèse de l'étape 2
│   ├── ecrans.md
│   ├── entites.md
│   ├── regles-metier.md
│   └── pieges.md
├── adr/
│   ├── 0001-architecture-front.md
│   ├── 0002-choix-design-system.md
│   └── ...
└── runbooks/
    ├── passation.md         # dernier handoff (toujours à jour)
    └── rapport-<date>.md    # rapports VM de test
```

### Cartographie (`docs/cartographie/`)

Produite à l'étape 2 par des sous-agents Claude Code en parallèle, à partir de `origine/` :

- **`ecrans.md`** : une fiche par fenêtre/page WinDev → future page/route React + composants. Inclut un lien vers la capture d'écran correspondante.
- **`entites.md`** : structure des données HFSQL → modèle de données cible (tables/entités API).
- **`regles-metier.md`** : traitements WLangage importants (calculs, validations, workflows).
- **`pieges.md`** : spécificités délicates (fichiers liés, requêtes complexes, comportements non standards) + secrets identifiés à révoquer.

### ADR (Architecture Decision Records)

Un fichier par décision structurante : contexte, options considérées, décision, conséquences. Exemples typiques pour ce type de migration : choix Vite vs Next.js, choix du design system, stratégie de migration des données, stratégie d'authentification.

### Handoff (`docs/runbooks/passation.md`)

Écrit par Claude Code à la fin de chaque session :

- Ce qui a été fait (commits, fichiers touchés).
- Résultat des tests (build, lint, unitaires, E2E).
- Ce qui reste à faire / points bloquants.
- Questions ouvertes pour Cowork/toi.

Cowork **commence toujours** par lire ce fichier + `CLAUDE.md` avant de rédiger le prochain prompt.

## Skills et hooks (optionnel)

- **Skill de revue** (`templates/skill-revue.md`) : check-list que Claude Code applique avant de committer (lint OK, build OK, pas de `console.log` oublié, composants accessibles, pas de secrets).
- **Hooks Git** (pre-commit) : lint + typecheck automatiques pour éviter les commits cassés.
