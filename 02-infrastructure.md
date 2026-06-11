# 02 — Infrastructure

## Vue d'ensemble

```
┌─────────────────┐      git push/pull      ┌──────────────────┐
│  Toi (poste)     │ <──────────────────────> │  Serveur Git      │
│  + Claude Cowork │                           │  (Gitea/GitLab)   │
└─────────────────┘                           └──────────────────┘
                                                       │
                                          git pull/push│
                                                       ▼
                                              ┌──────────────────┐
                                              │  VM Claude Code   │
                                              │  (dev)            │
                                              │  - apps/web (React)│
                                              │  - apps/api        │
                                              └──────────────────┘
                                                       │
                                          (nuit) git pull, build, tests
                                                       ▼
                                              ┌──────────────────┐
                                              │  VM de test       │
                                              │  - build front    │
                                              │  - build/run API  │
                                              │  - migrations DB  │
                                              │  - tests E2E       │
                                              │  - rapport horodaté│
                                              └──────────────────┘
```

## Serveur Git

- Héberge le dépôt unique du projet (monorepo conseillé) :

```
<App>/
├── origine/          # sources WinDev, specs, captures (souvent gitignored si lourd)
├── templates/         # copié depuis ce playbook
├── apps/
│   ├── web/           # application React (Vite ou Next.js)
│   └── api/           # API REST/GraphQL
├── packages/          # code partagé (types, utils) si monorepo pnpm/turborepo
├── docs/
└── CLAUDE.md
```

- Mise à jour auto : webhook ou tâche planifiée déclenchant le pipeline de la VM de test après chaque push sur `main`.

## VM de dev (Claude Code)

- Node.js LTS, `pnpm`, Git, `claude` CLI configuré.
- Variables d'environnement (`.env`) **jamais committées** — un `.env.example` documente les clés attendues.
- Lance localement : `pnpm dev` (front), `pnpm dev` ou équivalent (API), base de données locale (SQLite ou conteneur Postgres).

## VM de test *(si possible)*

Pipeline nocturne type :

1. `git pull origin main`
2. `pnpm install --frozen-lockfile`
3. `pnpm --filter web build` (vérifie que le front compile)
4. `pnpm --filter api build` + lancement + migrations DB
5. `pnpm --filter web test` (unitaires) + `pnpm exec playwright test` (E2E sur l'API + front buildés)
6. Écrit `docs/runbooks/rapport-<date>.md` avec le résultat (succès/échecs, logs pertinents) et le pousse sur Git.

C'est le **filet de sécurité** : si une régression apparaît, elle est détectée avant la prochaine session de travail.

## Synchronisation entre les deux IA

- **Cowork** ne modifie jamais le dépôt directement : il rédige des prompts.
- **Claude Code** modifie, teste, committe, pousse, et écrit le bilan.
- **Toi** : colles le prompt de Cowork dans Claude Code ; après exécution, fais `git pull` côté Cowork (ou colles le bilan) pour qu'il relise.

## Choix d'hébergement (à trancher étape 2, pas ici)

Cette étape ne fige **que l'infrastructure de développement**. L'hébergement de production (Vercel/Netlify pour le front, conteneur/VPS pour l'API, base managée ou auto-hébergée) est une décision produit, traitée à l'étape 2 (cadrage) et documentée dans un ADR.
