# Template — Prompt d'étape (Cowork → Claude Code)

---

Avant de commencer :
- Lis `CLAUDE.md`.
- Lis `docs/runbooks/passation.md`.
- Lis la fiche de cartographie concernée : `docs/cartographie/<fichier>.md`.

## Contexte

<Rappel de l'étape de roadmap et de l'existant.>

## Référence visuelle

<Si écran : `origine/screenshoot/<nom-ecran>.png`. Niveau de fidélité attendu : <pixel-perfect | comportement équivalent avec shadcn/ui>.>

## Tâche

<Description précise. Ex :
- Créer `app/clients/[id]/page.tsx` (Server Component) affichant la fiche client.
- Créer `components/clients/ClientForm.tsx` (Client Component) avec react-hook-form + Zod.
- Créer `app/clients/actions.ts` (Server Action `saveClient`) avec création/mise à jour Prisma.
- Champs : <liste, mapping depuis `docs/cartographie/entites.md`>.
- Règle métier : <référence à `docs/cartographie/regles-metier.md`>.>

## Critères d'acceptation

- [ ] <critère fonctionnel 1>
- [ ] <critère fonctionnel 2>
- [ ] Validation Zod côté serveur (Server Action) en plus du client
- [ ] Composant accessible (labels, focus, navigation clavier)
- [ ] Cohérent avec shadcn/ui et `CLAUDE.md`

## Clôture

- `pnpm lint && pnpm build` (et `pnpm prisma migrate dev` si schéma modifié).
- Tests unitaires/E2E pertinents.
- Commit + push.
- Mettre à jour `docs/runbooks/passation.md` (utiliser `templates/passation.template.md`).
- Mettre à jour `docs/roadmap.md`.
