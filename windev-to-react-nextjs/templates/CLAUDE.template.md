# CLAUDE.md — <App>

## Contexte

`<App>` est la migration de l'application WinDev/WebDev/HFSQL `<App-WinDev>` vers **Next.js (App Router) + TypeScript**.

- État d'avancement : `docs/roadmap.md`
- Cartographie de l'app d'origine : `docs/cartographie/`
- Dernier handoff : `docs/runbooks/passation.md` ← **toujours lire en premier**

## Stack technique

- **Framework** : Next.js (App Router), TypeScript
- **UI** : Tailwind CSS + shadcn/ui
- **Validation** : Zod (partagée client/serveur)
- **Données** : Prisma + `<PostgreSQL | SQLite>`
- **Data fetching client** : React Query (TanStack Query) si nécessaire au-delà des Server Components
- **Auth** : `<NextAuth.js | autre | aucune pour l'instant>`
- **Tests** : Vitest (unitaires), Playwright (E2E)
- **Gestionnaire de paquets** : pnpm

## Conventions

- Routes : `app/<segment>/page.tsx`. Routes API : `app/api/<ressource>/route.ts`.
- Server Components par défaut ; `"use client"` uniquement pour l'interactivité (formulaires, état local).
- Mutations : Server Actions (`"use server"`) colocalisées avec la route concernée (`app/<segment>/actions.ts`), ou Route Handlers si appel externe nécessaire.
- Schémas Zod partagés dans `lib/schemas/`.
- Accès données : uniquement via Prisma, jamais depuis un Client Component.
- Composants : `PascalCase`, un composant = un fichier dans `components/<domaine>/`.
- Chaque écran migré référence sa capture d'origine : `origine/screenshoot/<nom-ecran>.png`.

## Commandes

```bash
pnpm install
pnpm dev
pnpm build
pnpm lint
pnpm test                    # unitaires (Vitest)
pnpm exec playwright test     # E2E
pnpm prisma migrate dev
```

## Règles non négociables

1. Tout passe par Git.
2. Chaque commit passe `lint` + `build` + tests concernés.
3. Décision structurante → ADR dans `docs/adr/`.
4. Mettre à jour `docs/runbooks/passation.md` avant de terminer une session.
5. Aucun secret en clair (`.env`, jamais committé).
6. DB accessible uniquement via Server Components / Server Actions / Route Handlers.

## Roadmap

Voir `docs/roadmap.md`.
