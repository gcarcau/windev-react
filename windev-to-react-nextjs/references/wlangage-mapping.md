# WLangage → TypeScript : correspondances de langage

Ce document liste les constructions WLangage les plus courantes et leur équivalent TypeScript idiomatique. Objectif : **réécrire dans l'esprit de TypeScript**, pas transcrire littéralement.

## Variables et types

| WLangage | TypeScript |
|---|---|
| `MaVariable est une chaîne` | `let maVariable: string` |
| `MaVariable est un entier` | `let maVariable: number` |
| `MaVariable est un booléen` | `let maVariable: boolean` |
| `MaDate est une date` | `let maDate: Date` (ou `string` au format ISO si transmis via API/JSON) |
| `MonTableau est un tableau de chaînes` | `let monTableau: string[]` |
| `MaStructure est une structure` (membres) | `interface MaStructure { ... }` |
| Variable globale de projet | Selon usage : config (`process.env`), état serveur (DB/session), ou état client (Context/Zustand) — **jamais** une simple variable globale JS |

## Structures de contrôle

| WLangage | TypeScript |
|---|---|
| `SI ... ALORS ... SINON ... FIN` | `if (...) { ... } else { ... }` |
| `POUR i = 1 À N ... FIN` | `for (let i = 1; i <= n; i++) { ... }` |
| `POUR TOUT élément DE collection ... FIN` | `for (const element of collection) { ... }` ou `.forEach`/`.map` |
| `TANT QUE ... FIN` | `while (...) { ... }` |
| `SELON expression ... CAS valeur: ... AUTRE CAS: ... FIN` | `switch (expression) { case valeur: ...; default: ... }` |
| `RETOUR valeur` | `return valeur` |

## Chaînes de caractères

| WLangage | TypeScript |
|---|---|
| `Gauche(ch, n)` / `Droite(ch, n)` | `ch.slice(0, n)` / `ch.slice(-n)` |
| `Milieu(ch, début, longueur)` | `ch.substring(début - 1, début - 1 + longueur)` (attention à l'index 1-based WLangage) |
| `Majuscule(ch)` / `Minuscule(ch)` | `ch.toUpperCase()` / `ch.toLowerCase()` |
| `SansEspace(ch)` | `ch.trim()` |
| `Remplace(ch, recherche, remplacement)` | `ch.replaceAll(recherche, remplacement)` |
| `ChaîneVersEntier(ch)` / `ChaîneVersDécimal(ch)` | `parseInt(ch, 10)` / `parseFloat(ch)` ou `Number(ch)` |
| `EntierVersChaîne(n)` | `String(n)` ou `` `${n}` `` |
| Concaténation `ch1 + ch2` | identique, ou template literals `` `${a}${b}` `` |

## Dates

| WLangage | TypeScript |
|---|---|
| `DateVersChaîne(date, masque)` | `date.toLocaleDateString(...)` ou librairie `date-fns`/`dayjs` pour formats précis |
| `DateDuJour()` | `new Date()` |
| `AjouteJour(date, n)` | `date-fns`: `addDays(date, n)` |
| `DifférenceDate(date1, date2)` | `date-fns`: `differenceInDays(date1, date2)` |
| Format date HFSQL (`AAAAMMJJ` en chaîne) | Convertir en `Date` ISO dès la lecture (côté API/Prisma), ne pas propager le format chaîne côté front |

## Erreurs et exceptions

| WLangage | TypeScript |
|---|---|
| `SI ErreurDétectée ALORS ... FIN` après une fonction HFSQL | `try { ... } catch (error) { ... }` autour de l'appel Prisma/API |
| `ErreurInfo(errComplément)` | `error instanceof Error ? error.message : String(error)` |
| `Erreur("message")` (déclenche une erreur) | `throw new Error("message")` |

## Procédures et fonctions

| WLangage | TypeScript |
|---|---|
| Procédure globale (sans accès UI) | Fonction pure dans `lib/` (ex: `lib/pricing.ts`), exportée et testée unitairement |
| Procédure locale à une fenêtre, accédant aux données | Selon le rôle :<br>- lecture/écriture DB → Server Action ou Route Handler (`app/api/.../route.ts`)<br>- pure logique d'affichage → fonction dans le composant ou hook custom |
| Procédure déclenchée par un événement (clic, init fenêtre) | `onClick`/`useEffect` (Client Component) ou logique server-side (`page.tsx` Server Component pour l'init) |
| Paramètres optionnels (`PROCEDURE Truc(a, b = 10)`) | `function truc(a: string, b: number = 10)` |

## Collections / tableaux

| WLangage | TypeScript |
|---|---|
| `TableauAjoute(tab, élément)` | `tab.push(élément)` (ou `[...tab, élément]` en immuable) |
| `Trie(tab)` | `tab.sort((a, b) => ...)` |
| `Dimension(tab, n)` | Préférer un tableau dynamique (`[]`) plutôt qu'une taille fixe |
| `TableauOccurrence(tab, valeur)` | `tab.filter(x => x === valeur).length` |

## Notes générales

- WLangage est **1-indexé** (chaînes, tableaux) ; TypeScript/JS est **0-indexé** — vérifier systématiquement les bornes lors de la conversion de boucles et d'extractions de sous-chaînes.
- WLangage permet le typage implicite (`MaVariable = 5` sans déclaration) — toujours typer explicitement en TypeScript.
- Le code WLangage mélange souvent UI et logique métier dans le même événement ; la conversion doit **séparer** : la logique métier va en `lib/` ou en Server Action/Route Handler, l'UI reste dans le composant.
