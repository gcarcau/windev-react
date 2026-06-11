# Skill — Revue avant commit (Next.js)

## Code

- [ ] `pnpm lint` et `pnpm build` passent.
- [ ] Pas de `console.log`/`debugger` oubliés.
- [ ] Pas de `any` non justifié ; types Prisma générés utilisés.
- [ ] Server/Client Components correctement séparés (`"use client"` minimal).

## Données / sécurité

- [ ] Aucun secret en clair (variables dans `.env`, non committé).
- [ ] Aucun accès Prisma depuis un Client Component.
- [ ] Validation Zod côté serveur (pas seulement côté client) pour toute mutation.
- [ ] Vérification des droits/rôle côté serveur si l'écran est restreint.

## UI / accessibilité

- [ ] Labels et `aria-*` corrects sur les champs de formulaire.
- [ ] Navigation clavier possible.
- [ ] Cohérence avec shadcn/ui et le design system du projet.

## Fidélité fonctionnelle

- [ ] Comparaison avec `origine/screenshoot/` si écran, écarts documentés dans le handoff.
- [ ] Règles métier de `docs/cartographie/regles-metier.md` respectées.

## Tests

- [ ] Tests unitaires (Vitest) pour la logique non triviale (`lib/`).
- [ ] Test E2E (Playwright) pour tout nouveau parcours utilisateur.
- [ ] Tous les tests concernés passent localement.

## Documentation

- [ ] `docs/runbooks/passation.md` mis à jour.
- [ ] `docs/roadmap.md` mis à jour.
- [ ] ADR créé si décision structurante.
