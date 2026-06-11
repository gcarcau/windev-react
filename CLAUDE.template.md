# CLAUDE.md — <App>

## Contexte

`<App>` est la migration de l'application WinDev/WebDev/HFSQL `<App-WinDev>` vers une stack **React + API**.

- État d'avancement : voir `docs/roadmap.md`
- Cartographie de l'app d'origine : `docs/cartographie/`
- Dernier handoff : `docs/runbooks/passation.md` ← **toujours lire en premier**

## Stack technique

- **Front** : React + TypeScript, `<Vite | Next.js>`, routing : `<React Router | Next App Router>`
- **Design system** : `<Tailwind + shadcn/ui | MUI | Ant Design | autre>`
- **State management** : `<React Query pour les données serveur> + <Context | Zustand | Redux Toolkit>`
- **Backend / API** : `<Node/Express | Node/Fastify | autre>`, style `<REST | GraphQL | tRPC>`
- **Base de données** : `<SQLite | PostgreSQL | SQL Server>` via `<Prisma | Drizzle>`
- **Tests** : `<Vitest/Jest>` (unitaires), `<Playwright>` (E2E)
- **Gestionnaire de paquets** : `pnpm`

## Structure du dépôt

```
<App>/
├── apps/
│   ├── web/        # front React
│   └── api/        # API
├── packages/        # types/utils partagés (si monorepo)
├── origine/          # sources WinDev, captures, specs
├── docs/
└── CLAUDE.md
```

## Conventions

- Composants : `PascalCase`, un composant = un dossier (`ComponentName/index.tsx` + styles si besoin).
- Appels API côté front : hooks dédiés (`useXxxQuery`, `useXxxMutation`) avec React Query, jamais de `fetch` direct dans les composants.
- Routes API : `<convention REST: /api/<ressource> | resolvers GraphQL dans .../resolvers>`
- Pas d'accès DB direct depuis `apps/web`.
- Chaque écran migré référence sa capture d'origine : `origine/screenshoot/<nom-ecran>.png`.

## Commandes

```bash
pnpm install
pnpm dev              # lance front + API en parallèle
pnpm --filter web build
pnpm --filter api build
pnpm lint
pnpm test             # unitaires
pnpm exec playwright test   # E2E
```

## Règles non négociables

1. Tout passe par Git — pas de code échangé hors dépôt.
2. Chaque commit doit passer `lint` + `build` + tests concernés.
3. Toute décision structurante → ADR dans `docs/adr/`.
4. Mettre à jour `docs/runbooks/passation.md` avant de terminer une session.
5. Aucun secret en clair (utiliser `.env`, jamais committé — voir `.env.example`).
6. Front ↔ DB : toujours via l'API.

## Roadmap

Voir `docs/roadmap.md` pour l'étape en cours et les prochaines.
