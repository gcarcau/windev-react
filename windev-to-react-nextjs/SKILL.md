---
name: windev-to-react-nextjs
description: Use this skill whenever the user wants to migrate, port, rewrite, or modernize a WinDev, WebDev, WinDev Mobile, or HFSQL application toward React and/or Next.js. Trigger on mentions of "WinDev", "WebDev", "HFSQL", "WLangage", "PC SOFT", or on requests to migrate a legacy desktop/web app to React/Next.js, even if phrased loosely (e.g. "moderniser mon appli WinDev", "convertir cette fenêtre WinDev en composant React", "remplacer HFSQL par une API"). Covers the full methodology (cartography, architecture decisions, project memory, work loop) as well as concrete conversion: WLangage code → TypeScript, HFSQL schema/queries → Prisma/PostgreSQL or SQLite, WinDev windows/pages → React/Next.js components and routes, WDD/WWH analysis → data model, and HFSQL stored procedures/treatments → API route handlers.
---

# WinDev → React/Next.js Migration

This skill helps migrate a WinDev / WebDev / WinDev Mobile / HFSQL application to a modern **Next.js (App Router) + TypeScript** stack, with a separate or co-located API layer and a relational database (PostgreSQL or SQLite via Prisma).

It covers two complementary modes:

1. **Method / project setup mode** — bootstrapping the migration project itself (cartography, `CLAUDE.md`, roadmap, ADRs, work loop). Use this when the user is starting a new migration project or asking "how do I organize this migration".
2. **Conversion mode** — directly converting WinDev artifacts (windows, WLangage code, HFSQL analysis) the user provides into Next.js/TypeScript/Prisma code. Use this when the user pastes WLangage code, describes a WinDev window, or uploads an HFSQL analysis/export and wants the React/Next.js equivalent.

These modes are not exclusive — a real migration uses both, but a single chat turn ("convert this WLangage procedure to a Next.js API route") only needs mode 2.

## Quick decision guide

- User says "I have a whole WinDev app, help me plan/start the migration" → **Method mode**: read `references/method.md`, then follow `templates/PromptInit.md` to run a cartography and set up `CLAUDE.md` + roadmap.
- User pastes WLangage code / a window description / HFSQL schema and wants React/Next.js output → **Conversion mode**: read the relevant mapping reference(s) below, then produce code directly.
- User asks "how do I convert X (a specific WinDev concept) to Next.js" → read `references/conversion-map.md` for the relevant section, answer directly, with code.

## Conversion mode — workflow

1. **Identify what's being converted**: a window/page (UI), a WLangage procedure/treatment (logic), an HFSQL analysis (data model), or a query (data access).
2. **Load the right reference**:
   - UI (windows/pages, controls, navigation) → `references/ui-mapping.md`
   - WLangage language constructs (loops, strings, dates, error handling) → `references/wlangage-mapping.md`
   - HFSQL data model & queries → `references/data-mapping.md`
3. **Produce idiomatic Next.js/TypeScript**, not a literal transliteration:
   - WinDev windows/pages → React Server Components for display, Client Components (`"use client"`) for interactive forms/state.
   - WLangage procedures with DB access or business rules → Next.js Route Handlers (`app/api/.../route.ts`) or Server Actions.
   - HFSQL analysis (`.wda`/exported SQL) → Prisma schema (`schema.prisma`).
   - HFSQL queries (`HExecuteQuery`, `HReadFirst`, etc.) → Prisma Client calls or raw SQL via Prisma.
4. **Always flag assumptions**: WLangage is dynamically typed and has implicit behaviors (auto-save via `HModifie`, implicit links via `HLitRecherche`, global variables/contexts). When the source isn't fully visible, state the assumption explicitly and propose the React/Next.js equivalent (state, props, server-side session, etc.) rather than silently guessing.
5. **Match the project's existing conventions** if a `CLAUDE.md`, `schema.prisma`, or existing `apps/web` structure is visible in the repo — read it first (`view`) before generating new code so naming/style stay consistent.
6. **Reference screenshots**: if the user provides a screenshot of the WinDev window, compare the generated component's layout against it for fidelity (spacing, field order, button placement) before finalizing.

## Method mode — workflow

For project-level migration setup (new project, planning, roadmap, infrastructure):

1. Read `references/method.md` for the full playbook (principles, roles, infrastructure, project memory, work loop).
2. Use `templates/CLAUDE.template.md` to generate the project's `CLAUDE.md`.
3. Use `templates/PromptInit.md` as the cartography/init prompt structure.
4. Use `templates/ADR.template.md`, `templates/passation.template.md`, `templates/PromptEtape.template.md`, `templates/skill-revue.md` for ongoing project memory artifacts.
5. Default architecture choices for this skill (unless the user specifies otherwise): **Next.js App Router + TypeScript**, **Tailwind CSS + shadcn/ui**, **Prisma**, **PostgreSQL** (or **SQLite** for small/single-user apps), **React Query (TanStack Query)** for client-side data fetching where Server Components aren't sufficient, **Vitest** + **Playwright** for tests.

## Key technology mapping (cheat sheet)

| WinDev / HFSQL | React / Next.js equivalent |
|---|---|
| Fenêtre / Page WebDev | Route + page component (`app/<route>/page.tsx`) |
| Composant interne (volet, fenêtre interne) | React component (`components/...`) |
| Champ de saisie (Edit, Combo, RadioButton, Table) | Form input / `<select>` / shadcn `<Table>` + React Hook Form |
| Bouton + code clic | `<Button onClick={...}>` (client) or form submit → Server Action |
| Traitement WLangage (procédure globale/locale) | TypeScript function — shared util, Server Action, or API route handler |
| Fichier de données HFSQL (table) | Prisma model |
| Liaison HFSQL (clé étrangère implicite) | Prisma relation (`@relation`) |
| `HLitPremier` / `HLitRecherche` / boucle `HLitSuivant` | `prisma.model.findFirst` / `findMany` with `where` |
| `HAjoute` / `HModifie` / `HSupprime` | `prisma.model.create` / `update` / `delete` |
| `HExecuteRequete` (requête SQL/HFSQL) | `prisma.$queryRaw` or Prisma query builder |
| Variables globales de projet | Server-side: env/config or DB; Client-side: React Context / Zustand |
| Session utilisateur (gestion des droits WinDev) | NextAuth.js / custom session + middleware route protection |
| États d'impression (WDDoc) | Server-side PDF generation (e.g. `@react-pdf/renderer` or Puppeteer) |
| Configuration multi-postes / GDS | Git monorepo + environment variables |

For details and code examples, see `references/conversion-map.md`, `references/ui-mapping.md`, `references/wlangage-mapping.md`, and `references/data-mapping.md`.

## Output conventions

- Default project structure: `app/` (Next.js App Router), `prisma/schema.prisma`, `lib/` (shared logic), `components/` (UI).
- Use TypeScript everywhere, strict types — never emit `any` for data coming from Prisma (use generated types).
- For each converted window/page, briefly note in prose: original WinDev element → produced file(s), and any behavior that needs human validation (complex WLangage logic, ambiguous data relationships).
- If generating multiple files for a non-trivial conversion, create actual files under `/mnt/user-data/outputs` (or the project repo if working in one) rather than just inlining everything in chat — but for small snippets (a single function/component), inline code in the response is fine.
