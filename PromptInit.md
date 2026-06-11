# Prompt d'initialisation — <App>

> À remplir puis coller dans **Claude Cowork** pour démarrer le projet.

## Infos projet

- **Nom de l'application** : <App>
- **Nom dans WinDev** : <App-WinDev>
- **Type d'origine** : `<WinDev (desktop) | WebDev | WinDev Mobile | mix>`
- **Objectif de la migration** : <ex: remplacer une appli desktop vieillissante par une appli web moderne, ouvrir l'accès mobile, faciliter la maintenance...>
- **Contraintes connues** :
  - Volumétrie des données : <ordre de grandeur>
  - Nombre d'utilisateurs simultanés : <ordre de grandeur>
  - Système(s) tiers à interfacer (ERP, compta, etc.) : <ou "aucun">
  - Contraintes de calendrier : <ou "aucune">
  - Contraintes d'hébergement : <ex: doit rester on-premise / cloud imposé / pas de contrainte>

## Sources disponibles dans `origine/`

- [ ] `origine/code` — code WLangage en format texte
- [ ] `origine/autres` — script SQL de l'analyse HFSQL, specs
- [ ] `origine/data` — exports CSV des tables principales
- [ ] `origine/screenshoot` — captures des écrans principaux
- [ ] `origine/init_projet` — fichier de contexte généré par `/init_projet` (WinDev 2026), si disponible

## Demande à Cowork

1. Lance une **cartographie** de `origine/` via Claude Code (sous-agents en parallèle si volumineux) :
   - `docs/cartographie/ecrans.md` (un par fenêtre/page)
   - `docs/cartographie/entites.md` (modèle de données)
   - `docs/cartographie/regles-metier.md`
   - `docs/cartographie/pieges.md` (y compris secrets/identifiants à révoquer)

2. Une fois la cartographie disponible, **pose-moi les questions structurantes** pour cadrer la cible :
   - Architecture front : SPA (Vite) ou Next.js ?
   - Backend/API : nouvelle API dédiée ou réutilisation d'un existant ? Style (REST/GraphQL/tRPC) ?
   - Design system : Tailwind+shadcn/ui, MUI, Ant Design, ou autre ?
   - State management côté front (au-delà de React Query) ?
   - Base de données cible (voir `08-donnees.md`) ?
   - Périmètre : web seul, ou aussi PWA/React Native pour les écrans mobiles ?
   - Stratégie de séquencement : big bang ou module par module ?

3. Enregistre mes réponses sous forme d'**ADR** dans `docs/adr/`.

4. Génère/complète `CLAUDE.md` (à partir de `templates/CLAUDE.template.md`) et `docs/roadmap.md` avec la séquence d'étapes proposée.
