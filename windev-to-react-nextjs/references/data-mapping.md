# HFSQL → Prisma / PostgreSQL (ou SQLite)

## Choix de la base cible

- **HFSQL Classic** (mono-poste, faible volumétrie) → **SQLite** (`provider = "sqlite"` dans `schema.prisma`).
- **HFSQL Client/Serveur** (multi-utilisateurs) → **PostgreSQL** (recommandé).

## Types de données

| HFSQL | Prisma |
|---|---|
| Texte / Chaîne (longueur fixe ou variable) | `String` |
| Texte long / Mémo | `String` (PostgreSQL: `@db.Text`) |
| Numérique entier | `Int` (ou `BigInt` si grand) |
| Numérique avec décimales (Monétaire) | `Decimal` (PostgreSQL) — éviter `Float` pour les montants |
| Date | `DateTime` (`@db.Date` si l'heure n'est pas pertinente) |
| Heure | `DateTime` (`@db.Time`) ou `String` si stocké séparément |
| DateHeure | `DateTime` |
| Booléen | `Boolean` |
| Identifiant auto-incrémenté (clé primaire HFSQL auto) | `Int @id @default(autoincrement())` |
| Lien (clé étrangère implicite HFSQL) | Relation Prisma explicite (`@relation`) avec champ `xxxId` + `@@index` |
| Champ "Composition" / sous-structure | À aplatir en colonnes séparées, ou `Json` si vraiment variable |
| Image / Document stocké en base | Ne pas stocker en base : champ `String` (URL/clé) pointant vers un stockage objet (S3-compatible) |

## Exemple de transformation

### Analyse HFSQL (simplifiée)

```
FICHIER Client
  IDClient   : Entier (clé primaire, auto-incrémenté)
  Nom        : Texte(100)
  Email      : Texte(150)
  DateCreation : DateHeure

FICHIER Commande
  IDCommande : Entier (clé primaire, auto-incrémenté)
  IDClient   : Entier (lien vers Client)
  DateCommande : Date
  Montant    : Monétaire
```

### `schema.prisma` équivalent

```prisma
model Client {
  id           Int        @id @default(autoincrement())
  nom          String     @db.VarChar(100)
  email        String?    @db.VarChar(150)
  dateCreation DateTime   @default(now())
  commandes    Commande[]

  @@map("clients")
}

model Commande {
  id            Int      @id @default(autoincrement())
  clientId      Int
  client        Client   @relation(fields: [clientId], references: [id])
  dateCommande  DateTime @db.Date
  montant       Decimal  @db.Decimal(10, 2)

  @@index([clientId])
  @@map("commandes")
}
```

> `@@map(...)` permet de garder les noms de tables HFSQL d'origine côté SQL tout en utilisant des noms idiomatiques (camelCase) côté TypeScript — pratique pendant la phase de migration des données.

## Requêtes HFSQL → Prisma

| HFSQL | Prisma |
|---|---|
| `HLitPremier(Client, IDClient)` puis boucle `HLitSuivant` | `prisma.client.findMany()` |
| `HLitRecherche(Client, IDClient, valeur)` | `prisma.client.findUnique({ where: { id: valeur } })` |
| `HFiltre(Client, "Nom", "Dupont")` | `prisma.client.findMany({ where: { nom: "Dupont" } })` |
| Filtre multi-critères (`SI ... HFiltre ...`) | `where: { AND: [...], OR: [...] }` |
| `HAjoute(Client)` | `prisma.client.create({ data: { ... } })` |
| `HModifie(Client)` | `prisma.client.update({ where: { id }, data: { ... } })` |
| `HSupprime(Client, id)` | `prisma.client.delete({ where: { id } })` |
| `HExecuteRequete` (requête SQL avec jointures complexes) | `prisma.$queryRaw\`SELECT ...\`` (typer le résultat) ou requête Prisma avec `include`/`select` |
| Tri (`HTrie`) | `orderBy: { champ: "asc" | "desc" }` |
| Pagination (`HRetour`, navigation page par page) | `skip` / `take` (ou curseur `cursor` pour grandes listes) |

### Exemple — jointure

HFSQL :
```
HLitRecherche(Commande, IDClient, idClientCourant)
TANT QUE HTrouve(Commande)
    // ... accès à Client via lien implicite ...
    HLitSuivant(Commande, IDClient)
FIN
```

Prisma :
```ts
const commandes = await prisma.commande.findMany({
  where: { clientId: idClientCourant },
  include: { client: true },
  orderBy: { dateCommande: "desc" },
});
```

## Procédures stockées / traitements batch WLangage

Les traitements WLangage qui manipulent plusieurs fichiers HFSQL dans une transaction (`HDébutTransaction` / `HValideTransaction` / `HAnnuleTransaction`) deviennent :

```ts
await prisma.$transaction(async (tx) => {
  const commande = await tx.commande.create({ data: { ... } });
  await tx.client.update({
    where: { id: commande.clientId },
    data: { totalCommandes: { increment: commande.montant } },
  });
});
```

## Migration des données réelles

1. Exporter chaque table HFSQL en CSV (`origine/data/<table>.csv`).
2. Générer le schéma Prisma (ci-dessus) et lancer `npx prisma migrate dev`.
3. Écrire un script de seed/migration (`prisma/seed.ts` ou `scripts/migrate-data.ts`) :
   - lire chaque CSV (`papaparse` ou `csv-parse`) ;
   - convertir les types (dates HFSQL souvent en `AAAAMMJJ` → `new Date(...)`) ;
   - insérer via `prisma.<model>.createMany` en respectant l'ordre des dépendances (tables référencées avant tables référençantes).
4. Valider par échantillonnage (comparer N enregistrements aléatoires entre export HFSQL et base cible).
