# 05 — Boucle de travail

## La roadmap

`docs/roadmap.md` découpe la migration en étapes, généralement dans cet ordre :

1. **Socle** : monorepo, config Vite/Next.js + API, CI, base de données locale, design system installé.
2. **Authentification** (si l'app WinDev en avait une) — souvent en premier car bloquant pour le reste.
3. **Écrans cœur de métier** — un par un, dans l'ordre d'usage réel (le plus utilisé d'abord).
4. **Écrans secondaires / administration**.
5. **Migration des données réelles** (export HFSQL → base cible).
6. **Tests E2E des parcours critiques**.
7. **Déploiement** (front + API + base) sur l'environnement cible.

Chaque étape a un statut : `à faire`, `en cours`, `fait`, `bloqué`.

## Le cycle d'une étape

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Cowork rédige un prompt                                    │
│    - lit CLAUDE.md + dernier handoff + fiche cartographie     │
│    - préambule : contexte, capture d'écran de référence       │
│    - tâche précise + critères d'acceptation                   │
│    - clôture : "lance build/lint/tests, commit, push,         │
│      mets à jour passation.md"                                │
└─────────────────────────────────────────────────────────────┘
                          │ tu copies-colles
                          ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. Claude Code exécute (VM dev)                               │
│    - implémente le composant/la route/l'endpoint              │
│    - pnpm lint && pnpm build && pnpm test                     │
│    - tests E2E si pertinent                                    │
│    - commit + push                                            │
│    - écrit le bilan dans docs/runbooks/passation.md           │
└─────────────────────────────────────────────────────────────┘
                          │ tu fais git pull
                          ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. Cowork relit                                               │
│    - lit le diff + passation.md                               │
│    - classe les retours en 3 catégories :                     │
│      • bloquant (bug, écart fonctionnel majeur)                │
│      • nommage (convention, lisibilité)                        │
│      • métier (règle mal interprétée, à clarifier avec toi)    │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. Décisions                                                  │
│    - décision structurante → ADR                               │
│    - statut de l'étape mis à jour dans roadmap.md              │
│    - si bloquant : nouveau prompt correctif (retour à 1)       │
│    - sinon : étape suivante                                     │
└─────────────────────────────────────────────────────────────┘
```

## Ce qui change concrètement par rapport à la version .NET

- **Critères d'acceptation visuels** : pour un écran, le prompt référence systématiquement la **capture d'écran WinDev** correspondante (`origine/screenshoot/...`) — Claude Code compare son rendu à l'original.
- **Tests** : en plus des tests unitaires, les **tests E2E (Playwright)** jouent un rôle central pour valider les parcours utilisateurs (formulaires, navigation), souvent plus fragiles à migrer que la logique pure.
- **Découplage front/API** : une étape « écran » peut nécessiter deux sous-tâches (endpoint API + composant front) — le prompt précise les deux, ou les sépare en deux prompts successifs si gros écran.

## Bonnes pratiques de prompts (Cowork → Claude Code)

- Toujours rappeler : *« Lis `CLAUDE.md` et `docs/runbooks/passation.md` avant de commencer. »*
- Donner le **chemin exact** des fichiers concernés (composants existants à réutiliser, types partagés).
- Préciser le **niveau de fidélité attendu** (pixel-perfect vs comportement équivalent).
- Toujours terminer par : *« Build, lint, tests, commit, push, mets à jour le handoff. »*
