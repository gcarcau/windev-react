# 07 — Perspectives (annexe, optionnel)

Ce chapitre est **hors périmètre** du cœur du playbook : il aide à remplacer les dernières briques PC SOFT une fois l'application React/API fonctionnelle, si tu veux aller plus loin.

## Authentification

WinDev/WebDev gèrent souvent l'authentification via le moteur HFSQL ou un système de droits intégré. Équivalents côté React/API :

- **Auth maison** : table `users` + JWT (access/refresh tokens), hashing avec `argon2`/`bcrypt`.
- **Solutions managées** : Auth0, Clerk, Supabase Auth, Keycloak (auto-hébergé) — utile si SSO/2FA requis rapidement.
- Côté React : contexte d'authentification + routes protégées (`ProtectedRoute` / middleware Next.js).

## Gestion des droits / profils

Les notions WLangage de « groupes d'utilisateurs » se traduisent par un système de **rôles/permissions** côté API (middleware de vérification), avec affichage conditionnel des composants côté React selon le rôle.

## Télémétrie / monitoring

- **Frontend** : Sentry (erreurs JS), Plausible/Umami (analytics respectueux de la vie privée).
- **API** : logs structurés (pino/winston), métriques (Prometheus + Grafana) si volumétrie le justifie.

## Notifications

- Remplacement des notifications WinDev (popups, emails via WLangage) par :
  - emails transactionnels (Resend, Postmark, ou SMTP existant) ;
  - notifications in-app (toasts via le design system) ;
  - éventuellement websockets (Socket.IO, ou Server-Sent Events) pour du temps réel.

## Impression / export PDF

WinDev a un moteur d'état intégré ; côté web, équivalents courants :

- génération PDF côté API (ex: `pdf-lib`, Puppeteer pour rendu HTML→PDF) ;
- export Excel/CSV via librairies dédiées (`exceljs`, `papaparse`).

## Distribution / déploiement

- **Front** : build statique déployé (Vercel, Netlify, ou serveur Nginx) ; si Next.js SSR, déploiement Node.
- **API** : conteneur Docker, déployé sur VPS/cloud, derrière un reverse proxy (Nginx/Caddy) avec HTTPS automatique.
- **Mises à jour** : CI/CD (GitHub Actions/Gitea Actions) déclenché sur push vers `main`/`production`.

## Mobile

Si l'application avait des écrans **WinDev Mobile**, et qu'une version mobile reste nécessaire :

- **React Native (Expo)** permet de réutiliser une bonne part de la logique métier (hooks, types, appels API) déjà écrite pour le web ;
- ou **PWA** (le front React devient installable, accès offline limité) si les besoins mobiles sont modestes.

> Ces sujets sont **optionnels** et à traiter projet par projet, une fois le cœur fonctionnel migré et stable.
