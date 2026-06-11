# Prompt d'initialisation — <App>

> À remplir puis coller dans **Claude Cowork** pour démarrer le projet.

## Infos projet

- **Nom de l'application** : <App>
- **Nom dans WinDev** : <App-WinDev>
- **Type d'origine** : `<WinDev (desktop) | WebDev | WinDev Mobile | mix>`
- **Objectif** : <ex: remplacer une appli desktop vieillissante, ouvrir l'accès web/mobile...>
- **Contraintes connues** :
  - Volumétrie données : <ordre de grandeur>
  - Utilisateurs simultanés : <ordre de grandeur>
  - Systèmes tiers à interfacer : <ou "aucun">
  - Calendrier : <ou "aucune contrainte">
  - Hébergement : <Vercel / on-premise / autre>

## Sources disponibles dans `origine/`

- [ ] `origine/code` — WLangage en format texte
- [ ] `origine/autres` — script SQL de l'analyse HFSQL
- [ ] `origine/data` — exports CSV
- [ ] `origine/screenshoot` — captures des écrans
- [ ] `origine/init_projet` — contexte généré par `/init_projet` (WinDev 2026), si disponible

## Demande à Cowork

1. Lance une **cartographie** via Claude Code (sous-agents en parallèle si volumineux) :
   - `docs/cartographie/ecrans.md` — un par fenêtre/page, avec proposition de mapping route/composant Next.js
   - `docs/cartographie/entites.md` — modèle de données → proposition de `schema.prisma`
   - `docs/cartographie/regles-metier.md`
   - `docs/cartographie/pieges.md` (incl. secrets à révoquer)

2. Pose-moi les questions structurantes :
   - PostgreSQL ou SQLite ?
   - Stratégie d'authentification (NextAuth.js, autre, aucune dans un premier temps) ?
   - Hébergement cible (Vercel, conteneur, on-premise) ?
   - Périmètre : web seul, ou aussi PWA/React Native pour les écrans WinDev Mobile ?
   - Séquencement : big bang ou module par module ?

3. Enregistre les réponses en **ADR** (`docs/adr/`).

4. Génère/complète `CLAUDE.md` (depuis `templates/CLAUDE.template.md`) et `docs/roadmap.md`.
