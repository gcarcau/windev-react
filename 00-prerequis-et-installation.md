# 00 — Prérequis & installation

Tout ce qu'il faut mettre en place **une seule fois**, avant le premier projet de migration WinDev → React.

## 1. Comptes

- **Compte Anthropic / Claude** : accès à Claude Cowork (interface web/desktop) et à Claude Code.
- **Compte Git** (Gitea/GitLab/GitHub auto-hébergé ou cloud) — il remplace le **GDS WinDev**.
- **Compte cloud** pour héberger l'API et le front (VPS, Azure/AWS/Scaleway, ou simple VM Linux).

## 2. Logiciels côté poste de pilotage

- **Node.js LTS** (≥ 20) + gestionnaire de paquets (`pnpm` recommandé, ou `npm`/`yarn`).
- **Git**.
- **VS Code** (ou éditeur équivalent) pour relecture rapide.
- **WinDev / WebDev 2026** (poste existant) : pour passer le projet en **format texte** et générer le script SQL de l'analyse.

## 3. Serveur Git

Un serveur Git auto-hébergé (Gitea léger conseillé) ou un compte sur une plateforme cloud. Il héberge :

- le dépôt du projet (`origine/`, `templates/`, code front `apps/web`, code API `apps/api`, `docs/`) ;
- les workflows CI (build front, build API, lint, tests).

## 4. VM Claude Code (« les mains »)

Une VM Linux (Ubuntu recommandé) avec :

- Node.js LTS, `pnpm`, Git ;
- accès au serveur Git (clé SSH déployée) ;
- selon le backend choisi à l'étape 2 : runtime supplémentaire (.NET, Python, etc.) ;
- Claude Code installé et configuré (`claude` CLI).

## 5. VM de test *(optionnelle mais recommandée)*

Une seconde VM, identique à la VM de dev, qui chaque nuit :

1. `git pull` ;
2. installe les dépendances (`pnpm install`) ;
3. lance `pnpm build` (front) et le build de l'API ;
4. exécute les tests unitaires + tests E2E (Playwright) ;
5. pousse un rapport horodaté dans `docs/runbooks/`.

## 6. Côté WinDev — préparer le terrain

- Passer le projet en **format de sauvegarde texte** (requis pour Git) : voir doc PC SOFT « Partagez vos projets via Git ».
- Générer le **script SQL** depuis l'analyse HFSQL.
- *(Optionnel, WinDev 2026)* Lancer `/init_projet` du Companion IA pour générer un fichier de contexte projet.

## Checklist de fin d'étape

- [ ] Compte Claude (Cowork + Code) opérationnel
- [ ] Serveur Git créé, dépôt projet initialisé
- [ ] VM Claude Code provisionnée, accès Git OK
- [ ] (Optionnel) VM de test provisionnée
- [ ] Projet WinDev exporté en texte + script SQL généré
