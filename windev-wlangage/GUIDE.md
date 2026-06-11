# Guide de génération de code WLangage

Règles et patterns pour produire du code WLangage **correct, idiomatique et
homogène**. Vérifier tout identifiant dans `index/lookup.tsv` avant emploi.

## 1. Charte de nommage

| Élément | Préfixe / forme | Exemples |
|---|---|---|
| Variable **globale** | `g` + type | `gnCompteur`, `gsNom`, `gbActif`, `gtabLignes` |
| **Membre** de classe/fenêtre | `m_` | `m_bAdmin`, `m_nID` |
| Variable **locale** (hongrois) | type en préfixe | `n` entier, `s` chaîne, `b` booléen, `d` date, `r` réel, `dh` dateheure, `tab` tableau, `st` structure, `o`/`cl` objet |
| **Champs** | TYPE_ en majuscules | `BTN_`, `EDT_`, `TABLE_`, `COMBO_`, `LIB_`, `IMG_`, `SEL_`, `ONG_`, `COL_` |
| **Procédure** / **Structure** | PascalCase (struct préfixe `ST`) | `CalculeTotal`, `STClient` |

## 2. Formatage (obligatoire)

- **Déclarer toutes les variables en tête** de procédure/événement, avant les instructions.
- **Corps de procédure en colonne 0** ; seules les structures de contrôle (`SI`, `POUR`, `POUR TOUT`, `TANTQUE`, `BOUCLE`, `SELON`, `QUAND EXCEPTION`) indentent d'**une tabulation** par niveau.
- **Aligner** les déclarations sur `est` et les affectations consécutives sur `=`.
- En-tête de procédure : `PROCÉDURE LOCAL <Nom>()` / `PROCÉDURE GLOBAL <Nom>()` / `PROCÉDURE INTERNE <Nom>()`.
- `SI … ALORS <instruction>` mono-ligne **sans** `FIN` ; multi-ligne **avec** `FIN`. Pas de continuation `...`.

## 3. Bonnes pratiques

- **Requêtes SQL paramétrées** (anti-injection) : ne jamais concaténer une saisie utilisateur dans le SQL (voir pattern §4).
- **Gestion d'erreurs HFSQL** : tester le retour des fonctions `Hxxx` et lire `HErreurInfo()`.
- **Exceptions** : `QUAND EXCEPTION DANS … FAIRE … FIN` + `ExceptionInfo()`.
- **Libérer les ressources** (sockets, fichiers, connexions) après usage.

## 4. Patterns vérifiés

### Parcours HFSQL
```wlangage
HLitPremier(Client, Nom)
TANTQUE PAS HEnDehors(Client)
	Trace(Client.Nom)
	HLitSuivant(Client, Nom)
FIN
```

### Requête SQL paramétrée (anti-injection)
```wlangage
reqClients est une Requête SQL =
[
SELECT nom, ville FROM Client WHERE ville = {pVille}
]
reqClients.pVille = EDT_Ville
HExécuteRequête(reqClients)
POUR TOUT reqClients
	TableAjouteLigne(TABLE_Res, reqClients.nom)
FIN
```

### CRUD HFSQL
```wlangage
HRAZ(Client)
SI HLitRecherchePremier(Client, ID, nID) ALORS
	Client.Nom = sNom
	RENVOYER HModifie(Client)
FIN
Client.Nom = sNom
RENVOYER HAjoute(Client)
```

### REST POST JSON
```wlangage
req est un restRequête
rép est un restRéponse
sJSON est une chaîne
vCorps est un Variant

vCorps.nom = "Test"
Sérialise(vCorps, sJSON, psdJSON)
req.URL = "https://api.exemple.com/v1/clients"
req.Méthode = httpPost
req.ContentType = "application/json"
req.Contenu = sJSON
rép = RESTEnvoie(req)
SI rép.CodeEtat <> 200 ALORS Erreur(ErreurInfo())
```

### Lecture JSON
```wlangage
vRacine est un Variant
Désérialise(vRacine, rép.Contenu, psdJSON)
POUR TOUT vElem DE vRacine.items
	Trace(vElem.nom)
FIN
```

### Chaîne multiligne
```wlangage
sModèle est une chaîne = [
Bonjour %1,
Votre commande %2 est prête.
]
sModèle = ChaîneConstruit(sModèle, sClient, nNumCmd)
```

### SELON
```wlangage
SELON nStatut
	CAS 0 : sLib = "Brouillon"
	CAS 1, 2 : sLib = "En cours"
	AUTRE CAS : sLib = "Inconnu"
FIN
```

### Procédure interne (callback)
```wlangage
TableauTrie(tabClients, ttFonction, CompareNom)

PROCÉDURE INTERNE CompareNom(c1 est un STClient, c2 est un STClient)
RENVOYER ChaîneCompare(c1.nom, c2.nom, ccSansCasse)
FIN
```

### E-mail (SMTP)
```wlangage
EmailOuvreSessionSMTP("user", "mdp", "smtp.exemple.com")
unMessage est un Email
unMessage.Destinataire = "client@exemple.com"
unMessage.Sujet = "Bonjour"
unMessage.Message = "Texte"
SI PAS EmailEnvoieMessage("user", unMessage) ALORS Erreur(ErreurInfo())
```

### Socket client
```wlangage
SI SocketConnecte("Sck", 8000, "192.168.1.10") ALORS
	SocketEcrit("Sck", sCommande + RC)
	sRép = SocketLit("Sck", Faux, 5000)
	SocketFerme("Sck")
FIN
```

> Pour visualiser un code coloré : déposer le code dans `viewer/code.wl` puis ouvrir le viewer.
