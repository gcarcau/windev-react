# 01 — Principes & rôles

## Philosophie

Migrer une application WinDev/HFSQL vers React n'est pas une **traduction ligne à ligne** du WLangage. C'est une **réécriture pilotée par la compréhension** : on documente ce que fait l'application (écrans, règles métier, données), puis on la **reconstruit** avec les idiomes React/TypeScript.

> La **structure prime sur le prompt**. Un bon `CLAUDE.md`, une roadmap claire et des handoffs à jour valent mieux qu'un prompt « magique ».

## Les deux IA

### Cowork — le cerveau

- Tient la **mémoire du projet** (`CLAUDE.md`, `docs/`, ADR, roadmap).
- **Rédige les prompts** envoyés à Claude Code (contexte + tâche + critères d'acceptation).
- **Relit** le travail produit (diff, bilan de passation) en 3 catégories : bloquant / nommage / métier.
- Ne touche jamais directement au dépôt.

### Claude Code — les mains

- Travaille **dans le dépôt**, sur sa VM dédiée.
- Écrit le code front (composants React, routes, hooks, styles) et le code API/back.
- **Teste pour de vrai** : `pnpm build`, `pnpm lint`, tests unitaires, tests E2E.
- Committe, pousse, et écrit un **bilan de passation**.

### Toi — le pilote

- **Valides** chaque étape (architecture, design, séquence).
- **Tranches** quand Cowork pose une question structurante.
- Fais le **pont** : copies les prompts de Cowork vers Claude Code, et vice-versa pour les retours ; lances `git pull` côté Cowork.

## Ce qui est non négociable

1. **Tout passe par Git.** Pas de code échangé hors dépôt.
2. **Chaque étape produit un commit testé.** Pas de « ça compile, on verra plus tard ».
3. **Chaque décision structurante → un ADR** (Architecture Decision Record).
4. **Le handoff (`docs/runbooks/passation.md`) est à jour avant chaque pause.**
5. **Aucun secret en clair** (clés API, mots de passe HFSQL…) — révoqués/rotés dès la cartographie, jamais committés.
6. **Le front React ne parle jamais directement à la base de données.** Toujours via l'API.
7. **Fidélité fonctionnelle d'abord, esthétique ensuite** : on reproduit le comportement métier avant d'optimiser le design (le design system peut être appliqué après coup, écran par écran).

## Pourquoi cette boucle fonctionne

- Elle force la **traçabilité** (Git, ADR, handoffs) → le projet reste compréhensible même après des semaines de pause.
- Elle évite la **dérive de contexte** : Claude Code relit toujours `CLAUDE.md` + le dernier handoff avant d'agir.
- Elle garde un **humain dans la boucle** sur les décisions qui comptent (archi, UX, séquencement), sans le noyer dans le code généré.
