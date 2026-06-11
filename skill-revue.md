# Skill — Revue avant commit (React)

> Check-list que Claude Code applique avant de committer toute modification.

## Code

- [ ] `pnpm lint` passe sans erreur ni nouveau warning.
- [ ] `pnpm --filter web build` et `pnpm --filter api build` (selon ce qui est touché) passent.
- [ ] Pas de `console.log`/`debugger` oubliés.
- [ ] Pas de `any` non justifié (TypeScript).
- [ ] Composants nommés en `PascalCase`, hooks en `useXxx`.

## Données / sécurité

- [ ] Aucun secret, token, ou identifiant en clair dans le code ou les fichiers committés.
- [ ] Le front n'effectue aucun accès direct à la base de données (tout passe par l'API).
- [ ] Les entrées utilisateur sont validées côté API (pas seulement côté front).

## UI / accessibilité

- [ ] Les éléments interactifs ont des labels/`aria-*` appropriés.
- [ ] Navigation au clavier possible (focus visible, ordre logique).
- [ ] Cohérence avec le design system du projet (pas de styles ad-hoc dupliqués si un composant existe déjà).

## Fidélité fonctionnelle

- [ ] Si un écran d'origine existe (`origine/screenshoot/`), le rendu/comportement a été comparé et les écarts volontaires sont documentés dans le handoff.
- [ ] Les règles métier identifiées dans `docs/cartographie/regles-metier.md` pour cet écran sont respectées.

## Tests

- [ ] Tests unitaires ajoutés/mis à jour pour la logique non triviale.
- [ ] Test E2E ajouté/mis à jour si un nouveau parcours utilisateur est introduit.
- [ ] Tous les tests concernés passent localement.

## Documentation

- [ ] `docs/runbooks/passation.md` mis à jour.
- [ ] `docs/roadmap.md` mis à jour si le statut d'une étape change.
- [ ] ADR créé si une décision structurante a été prise.
