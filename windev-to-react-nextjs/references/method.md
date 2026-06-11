# Méthode de migration WinDev → Next.js (playbook condensé)

Version condensée du playbook complet pour piloter un projet de migration avec deux assistants Claude (Cowork = cerveau, Claude Code = mains) et un humain pilote.

## Principes

1. Tout passe par **Git** — pas de code échangé hors dépôt.
2. Chaque commit doit être **testé** (`lint`, `build`, tests).
3. Toute décision structurante → un **ADR** (`docs/adr/`).
4. `docs/runbooks/passation.md` à jour avant chaque pause.
5. **Aucun secret en clair** dans le dépôt.
6. Pour Next.js : la base de données n'est jamais accédée depuis un Client Component — uniquement Server Components, Server Actions, ou Route Handlers.
7. Fidélité fonctionnelle d'abord, esthétique (design system) ensuite.

## Rôles

- **Cowork** : tient la mémoire (`CLAUDE.md`, roadmap, ADR), rédige les prompts, relit (bloquant / nommage / métier).
- **Claude Code** : exécute dans le dépôt, code, teste (`pnpm lint && pnpm build && pnpm test`), committe, pousse, écrit le bilan.
- **Toi** : valides, tranches, fais le pont entre les deux.

## Stack par défaut (sauf décision contraire en ADR)

- **Next.js (App Router) + TypeScript**
- **Tailwind CSS + shadcn/ui**
- **Prisma** + **PostgreSQL** (ou **SQLite** pour petite app mono-utilisateur)
- **Zod** pour la validation (partagée client/serveur)
- **React Query** pour le data-fetching client quand Server Components ne suffisent pas
- **Vitest** (unitaires) + **Playwright** (E2E)
- **pnpm**

## Structure de dépôt type

```
<App>/
├── origine/              # sources WinDev, captures, exports CSV
├── prisma/
│   └── schema.prisma
├── app/                   # Next.js App Router
│   ├── (routes)/...
│   └── api/...
├── components/
├── lib/
├── docs/
│   ├── roadmap.md
│   ├── cartographie/
│   ├── adr/
│   └── runbooks/
└── CLAUDE.md
```

## Parcours de migration

### Étape 0 — Infrastructure (une fois)

Comptes Claude, serveur Git, VM Claude Code, optionnellement VM de test (build + tests E2E nocturnes).

### Étape 1 — Préparer `origine/`

- `origine/code` : WLangage en format texte (export Git WinDev).
- `origine/autres` : script SQL de l'analyse HFSQL.
- `origine/data` : exports CSV des tables.
- `origine/screenshoot` : captures de chaque écran important.
- *(WinDev 2026)* `/init_projet` du Companion IA → fichier de contexte.

### Étape 2 — Cartographie + cadrage (prompt d'init)

Claude Code produit (sous-agents en parallèle) :
- `docs/cartographie/ecrans.md` (un par fenêtre/page → future route/composant)
- `docs/cartographie/entites.md` (analyse HFSQL → modèle Prisma)
- `docs/cartographie/regles-metier.md`
- `docs/cartographie/pieges.md` (+ secrets à révoquer)

Cowork pose les questions structurantes restantes (architecture précise, auth, hébergement) et enregistre les choix en ADR. Génère `CLAUDE.md` et `docs/roadmap.md`.

### Étape 3 — Boucle de travail

Pour chaque item de la roadmap :
1. Cowork rédige un prompt (lit `CLAUDE.md` + dernier handoff + fiche cartographie + référence visuelle si écran).
2. Claude Code exécute, teste, committe, pousse, écrit le handoff.
3. Tu fais `git pull`.
4. Cowork relit (bloquant / nommage / métier), met à jour roadmap/ADR.

### Étape 4 — VM de test (si possible)

Pipeline nocturne : `git pull` → `pnpm install` → `pnpm build` → `prisma migrate` → tests unitaires + Playwright → rapport horodaté.

### Étape X — Migration des données réelles

Voir `references/data-mapping.md` — export CSV → script de seed Prisma → validation par échantillonnage.

### Étape finale — Production

Front + API Next.js sur Vercel/Node, base PostgreSQL managée ou auto-hébergée. ADR pour les choix d'hébergement et d'authentification (NextAuth.js, etc.).

## Roadmap type (ordre conseillé)

1. Socle : projet Next.js + Tailwind/shadcn + Prisma + CI (lint/build/test).
2. Authentification (si présente dans l'app d'origine) — souvent bloquant.
3. Écrans cœur de métier, un par un (le plus utilisé d'abord).
4. Écrans secondaires / administration.
5. Migration des données réelles.
6. Tests E2E des parcours critiques.
7. Déploiement.
