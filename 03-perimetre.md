# 03 — Périmètre

Ce chapitre distingue ce que **ce guide impose** (pour garder une méthode cohérente d'un projet à l'autre) et ce qu'il **te laisse décider** (propre à chaque projet).

## Ce que le guide impose

- **Méthode** : cycle Cowork (cerveau) / Claude Code (mains) / toi (pilote), boucle de prompts, handoffs, ADR.
- **Git** comme unique canal d'échange de code.
- **Séparation front/back stricte** : le front React consomme une API, jamais d'accès direct à la base de données.
- **Tests réels à chaque étape** : pas de commit non testé.
- **Mémoire projet** : `CLAUDE.md`, `docs/adr/`, `docs/runbooks/passation.md`, roadmap.
- **Aucun secret en clair** dans le dépôt.

## Ce que le guide te laisse choisir (à trancher étape 2)

### Architecture front

- **SPA** (Vite + React Router) — simple, déploiement statique.
- **Next.js** (App Router) — si SEO, SSR, ou routes API intégrées sont utiles.

### Backend / API

- **Nouvelle API dédiée** (Node/Express/Fastify, .NET, autre) — recommandé pour une séparation propre.
- **Réutilisation/portage** d'un back existant si une migration .NET ou autre a déjà été entamée.
- **Style d'API** : REST, GraphQL, ou tRPC (si full TypeScript monorepo).

### Design system / UI

- **Tailwind CSS + shadcn/ui** — flexible, rapide à styliser.
- **MUI / Ant Design** — composants riches « out of the box », utile si l'appli WinDev a beaucoup de tableaux/formulaires complexes.
- **Maquettes custom** — si une refonte UX est aussi à l'ordre du jour.

### State management

- **Context API + hooks** — pour des états globaux simples (utilisateur, thème).
- **React Query / TanStack Query** — quasi systématique pour les données serveur (cache, revalidation).
- **Zustand / Redux Toolkit** — si état client complexe (formulaires multi-étapes, éditeurs).

### Périmètre fonctionnel

- Web uniquement, ou aussi PWA / **React Native** (Expo) pour reprendre les écrans WinDev Mobile.
- Migration **big bang** vs **par modules** (un module métier à la fois, avec coexistence temporaire de l'ancien WinDev).

### Base de données cible

- Voir `08-donnees.md` : SQLite, PostgreSQL, SQL Server… exposée via l'API.

## Comment ces choix sont pris

Toutes ces questions sont posées par Cowork lors de l'**étape 2 (prompt d'initialisation)**, sur la base de la cartographie produite par Claude Code. Chaque choix devient un **ADR** dans `docs/adr/`.
