# 06 — Démarrer un projet (de zéro)

Récapitulatif séquentiel pour lancer une nouvelle migration WinDev → React.

## 1. Infrastructure (une fois — voir `00` et `02`)

- Comptes Claude, serveur Git, VM Claude Code, (optionnel) VM de test.

## 2. Créer le dépôt projet

```bash
mkdir <App> && cd <App>
git init
mkdir -p origine/{code,autres,data,screenshoot} templates docs/{adr,runbooks,cartographie}
```

- Copier `templates/` depuis ce playbook.
- Déposer dans `origine/` : code WLangage en texte, script SQL, exports CSV, captures d'écran.

## 3. Préparer les sources côté WinDev

- Passer le projet en **format texte** (Git).
- Générer le **script SQL** depuis l'analyse HFSQL.
- *(WinDev 2026)* `/init_projet` du Companion IA → fichier de contexte, à déposer dans `origine/`.
- Capturer **chaque écran** important (`origine/screenshoot/`).

## 4. Prompt d'initialisation (Cowork)

- Ouvrir Claude Cowork, remplir `templates/PromptInit.md` (infos projet : nom, objectif, contraintes connues).
- Coller le prompt. Cowork :
  1. commande une **cartographie** à Claude Code (sous-agents en parallèle) → `docs/cartographie/`.
  2. te pose les questions structurantes (cf. `03-perimetre.md`) : architecture front, backend, design system, state management, périmètre, base cible.
  3. enregistre tes choix en **ADR**.
  4. génère `CLAUDE.md`, `docs/roadmap.md`.

## 5. Initialiser le socle technique

Premier prompt vers Claude Code, typiquement :

- monorepo `pnpm` avec `apps/web` (Vite ou Next.js + TypeScript) et `apps/api` ;
- design system installé et configuré (ex: Tailwind + shadcn/ui) ;
- API minimale (health check, connexion DB locale) ;
- CI : lint + build + tests sur chaque push ;
- README de démarrage (`pnpm install && pnpm dev`).

→ commit, push, handoff.

## 6. Boucle de travail (voir `05`)

Itérer écran par écran / module par module selon la roadmap, en suivant le cycle prompt → exécution → relecture → ADR/roadmap.

## 7. VM de test (si possible)

Configurer le pipeline nocturne (build front + API, migrations, tests E2E) dès que le socle est en place — plus tôt il tourne, plus tôt les régressions sont détectées.

## 8. Migration des données

Quand les écrans cœur de métier sont stables : exporter les données réelles HFSQL (CSV) vers la base cible, via un script de migration versionné dans `apps/api/scripts/migration/`. Voir `08-donnees.md`.

## 9. Vers la production

- Choisir l'hébergement (front statique sur Vercel/Netlify ou conteneur ; API en conteneur/VPS ; base managée ou auto-hébergée) — ADR dédié.
- Mettre en place CI/CD de déploiement.
- Recette finale avec l'utilisateur métier, écran par écran, en s'appuyant sur les captures `origine/screenshoot/` comme référence.

## Annexes

- Pour remplacer les dernières briques PC SOFT (auth, télémétrie, distribution) : `07-perspectives.md`.
- Pour le choix de la base cible : `08-donnees.md`.
