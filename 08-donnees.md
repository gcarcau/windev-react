# 08 — Données : alternatives à HFSQL

Le front React **n'accède jamais directement** à la base de données : il passe par l'API. Ce chapitre concerne donc surtout le choix de la base **derrière l'API**, et la stratégie de migration des données HFSQL.

## Choisir la base cible

| Type d'app HFSQL d'origine | Base cible recommandée | Pourquoi |
| --- | --- | --- |
| **HFSQL Classic** (mono-poste / petit volume) | **SQLite** | Simplicité, zéro serveur à gérer, suffisant pour petite/moyenne volumétrie, fichier facile à sauvegarder. |
| **HFSQL Client/Serveur** (multi-utilisateurs, volumétrie significative) | **PostgreSQL** (recommandé) ou **SQL Server** | Concurrence, intégrité, écosystème riche d'ORMs Node/TS (Prisma, Drizzle). SQL Server pertinent si l'écosystème existant (autres applis, DBA) est déjà SQL Server. |

## Ce qu'on retrouve nativement

- **Types** : HFSQL → types SQL standards (PostgreSQL/SQL Server) ou types SQLite (avec quelques approximations, ex: pas de type DATE natif strict).
- **Clés primaires/étrangères, index** : se transposent directement.
- **Contraintes simples** (unicité, NOT NULL) : directes.

## Ce qui est à recâbler

- **Fichiers liés / requêtes HFSQL spécifiques** (ex: `HLitRecherche`, requêtes multi-fichiers avec liaisons implicites) → à réécrire en SQL explicite (jointures) ou en requêtes ORM (Prisma/Drizzle).
- **Calculs/déclencheurs WLangage** (code exécuté avant/après enregistrement) → à porter en :
  - logique applicative côté API (la plupart des cas, recommandé pour rester testable) ;
  - ou triggers SQL si vraiment lié à l'intégrité des données.
- **Champs calculés / mémo / images stockées en base** → à migrer vers colonnes adaptées (texte long, ou stockage objet externe — S3-compatible — pour les fichiers/images, avec juste une référence en base).
- **Séquences / compteurs HFSQL** → équivalents natifs (`SERIAL`/`IDENTITY` en PostgreSQL/SQL Server, `AUTOINCREMENT` en SQLite).

## Outillage côté API (Node/TypeScript)

- **ORM** : Prisma (DX excellente, migrations versionnées) ou Drizzle (plus proche du SQL, léger).
- **Migrations** : versionnées dans `apps/api/prisma/migrations/` (ou équivalent Drizzle), exécutées en CI/CD.

## Stratégie de migration des données réelles

1. Exporter chaque table HFSQL en **CSV** (`origine/data/`).
2. Écrire un script de migration (`apps/api/scripts/migration/`) qui :
   - crée le schéma cible (via les migrations ORM) ;
   - lit les CSV, transforme (mapping de types, nettoyage) ;
   - insère dans la base cible, en respectant l'ordre des dépendances (FK).
3. Valider par échantillonnage : comparer des enregistrements aléatoires entre HFSQL et la base cible.
4. Exécuter sur la **VM de test** d'abord, puis en production lors du déploiement final.

## Accès depuis React

Toujours via l'API :

```
React (fetch / React Query) ──HTTP/JSON──> API (Node) ──SQL──> PostgreSQL/SQLite/SQL Server
```

Aucune connexion base de données, aucun identifiant DB, ne doivent figurer dans le code front ni être exposés au navigateur.
