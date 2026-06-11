# Playbook — Fullstack React avec Next.js (Option A)

Ce dépôt décrit la méthode recommandée pour migrer une application WinDev/HFSQL vers une stack **Next.js fullstack** : front React, API routes intégrées, et partage de types au sein d'un monorepo.

## Pourquoi choisir l'Option A ?

- **Front + API ensemble** : une seule base de code, un seul déploiement.
- **Partage de types** facile entre pages, API et logique métier.
- **SSR/SSG** disponibles si l'application en a besoin.
- **Déploiement simplifié** sur Vercel, Netlify (Next.js) ou un serveur Node.
- **Structure claire** pour migrer écran par écran dans un projet React.

## Ce que couvre ce playbook

- le cadre de migration WinDev → React
- la méthode de travail avec Cowork / Claude Code
- les étapes indispensables : cartographie, prompt d'initialisation, roadmap, ADR, passation
- les bonnes pratiques pour garder une séparation front/API solide et éviter tout accès DB direct depuis le navigateur

## Choix techniques recommandés

- Front : **Next.js + React + TypeScript**
- Back : **API routes Next.js** ou **API intégrée dans le même monorepo**
- DB cible : **PostgreSQL / SQLite / SQL Server** exposée via API REST ou GraphQL
- ORM : **Prisma** ou **Drizzle**
- Tests : **Vitest/Jest** pour le code, **Playwright** pour les parcours
- Gestion de l'état : **React Query** pour les données serveur, **Context / Zustand / Redux Toolkit** pour l'état applicatif local

## Structure recommandée

```
origine/          # sources WinDev, captures, exports
templates/        # prompts, ADR, passation, skills
docs/             # roadmap, ADR, runbooks, cartographie
apps/
  web/            # front Next.js + pages/routes
  api/            # API partagée ou API routes Next.js
packages/         # types et utilitaires partagés
```

## Débuter la migration

1. Prépare le dossier `origine/` avec le code WLangage en texte, les scripts SQL, les exports de données et les captures d'écran.
2. Remplis `templates/PromptInit.md` pour cadrer le projet et lancer la cartographie.
3. Crée les premiers ADR dans `docs/adr/` : choix d'architecture, design system, base de données.
4. Génère `CLAUDE.md` et `docs/roadmap.md` pour suivre l'état d'avancement.
5. Pour chaque étape : prompt, implémentation, tests, commit, push, puis passation.

## Commandes type

```bash
pnpm install
pnpm dev      # si la configuration Next.js fullstack est en place
pnpm build
pnpm lint
pnpm test
pnpm exec playwright test
```

## Annexe

Voir `00-prerequis-et-installation.md`, `01-principes-et-roles.md`, `02-infrastructure.md`, `03-perimetre.md`, `04-memoire-projet-claude.md`, `05-boucle-de-travail.md`, `06-demarrage-de-zero.md`, `07-perspectives.md`, et `08-donnees.md` pour la méthode complète.

## L'idée en une phrase

> Deux IA, deux rôles : **Claude Cowork = le cerveau** (architecte / chef de projet / relecteur qui travaille avec toi), **Claude Code = les mains** (exécute dans le dépôt, code, teste, committe). **Tu valides à chaque étape.** Ce n'est pas magique : c'est une chaîne d'ingénierie où la **structure prime sur le prompt**.

## Différences clés par rapport à la version .NET

| Aspect | Version .NET | Version React |
| --- | --- | --- |
| Cible | App desktop/web .NET (front + back unifiés) | **Front React (SPA/Next.js)** + **API séparée** (Node/.NET/autre, à choisir) |
| UI WinDev (fenêtres/pages) | Mappées vers Razor/Blazor/MAUI | Mappées vers **composants React** (un écran WinDev ≈ une page/route + composants) |
| WLangage (code métier) | Porté en C# | Porté en **TypeScript** (logique partagée front, ou service API) |
| HFSQL | SQLite/PostgreSQL/SQL Server via EF Core | SQLite/PostgreSQL/SQL Server, exposé via **API REST/GraphQL** consommée par React (jamais d'accès DB direct depuis le front) |
| Style/skin WinDev | Thèmes .NET MAUI/Blazor | **Design system** (Tailwind, MUI, shadcn/ui…) à choisir à l'étape 2 |
| État applicatif (variables globales WLangage) | Services .NET / DI | **State management** React (Context, Zustand, Redux selon complexité) |

## Les rôles : deux IA + toi

| **Cowork** — le cerveau | **Claude Code** — les mains | **Toi** — le pilote |
| --- | --- | --- |
| cadre, architecture, **rédige les prompts**, **relit**, tient la roadmap et la mémoire | code front (React) + back (API) dans le dépôt (sur sa VM), **teste**, committe, pousse, écrit le **bilan** | **valides** chaque étape, **tranches** les décisions, fais le **pont** (copier-coller des prompts, `git pull`) |

Cowork tourne dans l'app Claude **sur ton poste** ; Claude Code **sur sa VM dédiée** ; **toi**, tu fais le lien entre les deux.

## Le parcours : de ton appli WinDev à l'appli React

### Étape 0 — L'infrastructure *(une fois)*

Comptes, **serveur Git**, **VM Claude Code**, et une **VM de test** (qui lance build front + build API + tests). Voir `00-prerequis-et-installation.md`.

### Étape 1 — Préparer les sources *(le dossier `origine/`)*

Crée le dépôt du projet, déposes-y `templates/` et un dossier `origine/` :

| sous-dossier | contenu | comment l'obtenir |
| --- | --- | --- |
| `origine/code` | code source WLangage **en texte** | format de sauvegarde texte (requis Git) |
| `origine/autres` | structure SQL, specs | script SQL généré depuis l'analyse HFSQL |
| `origine/data` | données réelles | export CSV des tables |
| `origine/screenshoot` | captures des écrans WinDev | une capture par fenêtre/page (essentiel pour reproduire l'UI en composants React) |

> *Astuce WinDev 2026* : le **Companion IA** propose `/init_projet` → fichier de contexte projet, à déposer dans `origine/`.

### Étape 2 — Le prompt d'initialisation *(cadrage)*

Ouvre **Claude Cowork**, remplis `templates/PromptInit.md`. Cowork commande une **cartographie** (entités, écrans, règles métier, navigation, pièges, secrets à révoquer), te pose les questions structurantes propres au front :

- **Architecture** : SPA (Vite + React Router) vs Next.js (SSR/SSG) ?
- **Backend** : nouvelle API dédiée, ou réutilisation/portage d'un back existant ?
- **Design system** : Tailwind + shadcn/ui, MUI, Ant Design, ou maquettes custom ?
- **State management** : Context API simple, Zustand, Redux Toolkit, React Query pour les données serveur ?
- **Périmètre** : web only, ou aussi PWA/mobile (React Native) pour les écrans WinDev Mobile ?

Puis met en place `CLAUDE.md`, l'arbo `docs/` et la **roadmap** (généralement : socle API → écrans cœur de métier → écrans secondaires → tests E2E).

### Étape 3 — La boucle de prompts *(aller-retour, le cœur du travail)*

1. **Cowork rédige un prompt** (préambule « lis le handoff + `CLAUDE.md` » → clôture « commit + push + mets à jour le handoff »).
2. **Tu le colles dans Claude Code** (VM de dev) : il exécute, **teste pour de vrai** (build + lint + tests unitaires/E2E), committe, pousse, écrit son **bilan** dans `docs/runbooks/passation.md`.
3. **Tu fais `git pull`** → Cowork relit la version à jour.
4. **Cowork relit** en 3 catégories (bloquant / nommage / métier) — pour React, vigilance particulière sur : fidélité visuelle vs capture WinDev, accessibilité, cohérence du design system, gestion d'état et appels API.
5. **Chaque décision → un ADR** ; statut de l'étape à jour. On enchaîne.

### Étape 4 — La VM de test *(si possible)*

Une machine qui rejoue tout chaque nuit : build front, build/lancement API, migrations DB, tests E2E (Playwright/Cypress) — pousse un rapport horodaté.

### Étape X — L'application React produite

Au bout de la roadmap : front React + API, testés, déployables (build statique + conteneur API, ou Next.js sur Node).

## Sommaire

| Chapitre | Contenu |
| --- | --- |
| [00 — Prérequis & installation](00-prerequis-et-installation.md) | Comptes, logiciels (Node, gestionnaire de paquets), serveur Git, VM Claude Code |
| [01 — Principes & rôles](01-principes-et-roles.md) | Philosophie, les deux IA, ce qui est non négociable |
| [02 — Infrastructure](02-infrastructure.md) | Serveur Git, VM dev/test, pipelines build front+back |
| [03 — Périmètre](03-perimetre.md) | Outils + règles imposés, vs choix laissés (archi front, design system, séquence) |
| [04 — Mémoire projet](04-memoire-projet-claude.md) | `CLAUDE.md`, `docs/`, ADR, runbooks, handoff, skills, hooks |
| [05 — Boucle de travail](05-boucle-de-travail.md) | Roadmap, cycle d'une étape, bilans, revue, décisions |
| [06 — Démarrer un projet](06-demarrage-de-zero.md) | Le parcours détaillé : infra → cartographie → cadrage → boucle |
| [07 — Perspectives (annexe)](07-perspectives.md) | Authentification (remplacer le système WinDev), notifications, déploiement |
| [08 — Données](08-donnees.md) | Choisir API + base cible : SQLite/PostgreSQL/SQL Server derrière une API REST/GraphQL |
| `templates/` | `CLAUDE.template.md`, `PromptInit.md`, `ADR.template.md`, `passation.template.md`, `PromptEtape.template.md`, `skill-revue.md` |

## Public

Tout développeur **WinDev / WebDev / WinDev Mobile** qui veut **migrer un projet vers une stack React (+ API) avec Claude Code**.

## Notations

Les valeurs propres à un projet sont notées entre chevrons : `<App>`, `<url-gitea>`, `<base>`, etc. — remplace-les à l'usage.

