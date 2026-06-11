# Aide-mémoire — fonctions WLangage courantes

Signatures vérifiées (extraites de la doc). Pour le détail/paramètres : `pages/<id>.md` ou `index/lookup.tsv`.

## HFSQL — accès aux données

- `<Résultat> = HExécuteRequêteSQL(<Requête> [, <Mode>] , <Texte de la requête en SQL>)` — *HExecuteSQLQuery*
- `<Résultat> = HExécuteRequête(<Nom de la requête> [, <Mode> [, <Paramètre 1> [... [, <Paramètre N>]]]])` — *HExecuteQuery*
- `<Résultat> = HLitPremier([<Fichier de données> [, <Rubrique de parcours>] [, <Options>]])` — *HReadFirst*
- `<Résultat> = HLitDernier([<Fichier de données> [, <Rubrique de parcours>] [, <Options>]])` — *HReadLast*
- `<Résultat> = HLitSuivant([<Fichier de données> [, <Rubrique de parcours>] [, <Options>]])` — *HReadNext*
- `<Résultat> = HLitPrécédent([<Fichier de données> [, <Rubrique de parcours>] [, <Options>]])` — *HReadPrevious*
- `<Résultat> = HEnDehors([<Fichier de données>])` — *HOut*
- `<Résultat> = HLitRecherchePremier(<Fichier de données> , <Rubrique> , <Valeur recherchée> [, <Options>])` — *HReadSeekFirst*
- `<Résultat> = HLitRecherche(<Fichier de données> , <Rubrique> , <Valeur recherchée> [, <Options>])` — *HReadSeek*
- `<Résultat> = HAjoute([<Fichier de données> [, <Options>]])` — *HAdd*
- `<Résultat> = HModifie([<Fichier de données> [, <Numéro d'enregistrement> [, <Options>]]])` — *HModify*
- `<Résultat> = HSupprime([<Fichier de données> [, <Numéro d'enregistrement> [, <Options>]]])` — *HDelete*
- `<Résultat> = HRAZ([<Fichier de données> [, <Rubrique>]])` — *HReset*
- `<Résultat> = HNbEnr([<Fichier de données> [, <Options>]])` — *HNbRec*
- `<Résultat> = HTrouve([<Fichier de données>])` — *HFound*
- `<Résultat> = HFiltre(<Fichier de données> , <Clé de parcours> , <Borne minimale> [, <Borne maximale> [, <Condition de sélection>]])` — *HFilter*
- `<Résultat> = HAnnuleDéclaration([<Fichier de données>])` — *HCancelDeclaration*
- `<Résultat> = HErreurInfo([<Type d'information>])` — *HErrorInfo*
- `<Résultat> = HSauvePosition([<Fichier de données> [, <Rubrique>]] [, <Options>])` — *HSavePosition*
- `<Résultat> = HRetourPosition(<Position> [, <Option>])` — *HRestorePosition*

## Chaînes

- `<Résultat> = ChaîneConstruit(<Chaîne initiale> [, <Paramètre 1> [... [, <Paramètre N>]]])` — *StringBuild*
- `<Résultat> = ExtraitChaîne(<Chaîne initiale> , <Rang> [, <Séparateur> [, <Sens de parcours>]])` — *ExtractString*
- `<Résultat> = ExtraitChaîneEntre(<Chaîne initiale> , <Rang> , <Séparateur de début> [, <Séparateur de fin> [, <Options>]])` — *ExtractStringBetween*
- `<Résultat> = Remplace(<Chaîne initiale> , <Chaîne à remplacer> , <Nouvelle chaîne> [, <Option>])` — *Replace*
- `<Résultat> = Majuscule(<Chaîne de caractères à convertir>)` — *Upper*
- `<Résultat> = Minuscule(<Chaîne de caractères à convertir>)` — *Lower*
- `<Résultat> = Complète(<Chaîne à manipuler> , <Taille> [, <Caractère>])` — *Complete*
- `<Résultat> = Taille(<Chaîne initiale>)` — *Length*
- `<Résultat> = Position(<Chaîne initiale> , <Chaîne à rechercher> [, <Position de départ> [, <Option>]])` — *Position*
- `<Résultat> = PositionOccurrence(<Chaîne initiale> , <Chaîne à rechercher> , <Rang de l'occurrence recherchée> [, <Options de recherche>])` — *PositionOccurrence*
- `<Résultat> = ChaîneCommencePar(<Chaîne initiale> , <Chaîne recherchée> [, <Options de recherche>])` — *StringStartsWith*
- `<Résultat> = ChaîneFinitPar(<Chaîne initiale> , <Chaîne recherchée> [, <Options de recherche>])` — *StringEndsWith*
- `<Résultat> = Contient(<Chaîne à analyser> , <Sous-chaîne> [, <Options>])` — *Contains*
- `<Résultat> = Gauche(<Chaîne initiale> [, <Longueur>])` — *Left*
- `<Résultat> = Droite(<Chaîne initiale> [, <Longueur>])` — *Right*
- `<Résultat> = Milieu(<Chaîne initiale> , <Position de départ> [, <Longueur>])` — *Middle*
- `<Résultat> = SansEspace(<Chaîne initiale> [, <Position>])` — *NoSpace*
- `<Résultat> = NumériqueVersChaîne(<Nombre> [, <Format>])` — *NumToString*
- `<Résultat> = ChaîneVersNumérique(<Chaîne initiale> [, <Base utilisée>])` — *StringToNum*

## Date / Heure

- `<Résultat> = DateDuJour()` — *Today*
- `<Résultat> = DateVersChaîne(<Date> [, <Format>])` — *DateToString*
- `<Résultat> = ChaîneVersDate(<Date> [, <Format>])` — *StringToDate*
- `<Résultat> = DateValide(<Date>)` — *DateValid*
- `<Résultat> = DateHeureVersChaîne(<Donnée à convertir> [, <Format>])` — *DateTimeToString*

## Tableaux

- `<Résultat> = TableauAjoute(<Variable WLangage> [, <Valeur>])` — *ArrayAdd*
- `<Résultat> = Ajoute(<Variable WLangage> [, <Valeur>])` — *Add*
- `<Résultat> = TableauSupprime(<Tableau WLangage> , <Indice de l'élément>)` — *ArrayDelete*
- `TableauSupprimeTout(<Variable WLangage>)` — *ArrayDeleteAll*
- `<Résultat> = TableauCherche(<Tableau WLangage> , <Type de recherche> , <Valeur recherchée> [, <Indice de départ>])` — *ArraySeek*
- `TableauTrie(<Tableau WLangage> [, <Type de tri>])` — *ArraySort*
- `<Résultat> = TableauOccurrence(<Tableau WLangage>)` — *ArrayCount*
- `TableauInsère(<Tableau WLangage> , <Indice d'insertion> [, <Valeur de l'élément>])` — *ArrayInsert*

## Champ Table

- `<Résultat> = TableAjouteLigne(<Champ Table> [, <Élément colonne 1> [... [, <Élément colonne N>]]])` — *TableAddLine*
- `TableSupprimeTout(<Champ Table>)` — *TableDeleteAll*
- `TableAffiche(<Champ Table> [, <Position>])` — *TableDisplay*
- `<Résultat> = TableSelect(<Champ Table> [, <Rang> [, <Information à renvoyer>]])` — *TableSelect*
- `TableSelectMoins(<Champ Table> [, <Indice 1> [... [, <Indice N>]]])` — *TableSelectMinus*

## HTTP / REST

- `<Réponse REST> = RESTEnvoie(<Requête REST>)` — *RESTSend*
- `<Réponse HTTP> = HTTPEnvoie(<Requête HTTP>)` — *HTTPSend*
- `<Résultat> = HTTPRequête(<URL à contacter> [, <Agent utilisateur> [, <Entête HTTP supplémentaire> [, <Message à envoyer> [, <Type du message> [, <Nom User> [, <Mot de passe>]]]]]])` — *HTTPRequest*
- `<Résultat> = HTTPDonneRésultat([<Type d'information>])` — *HTTPGetResult*

## JSON / Sérialisation

- `Sérialise(<Variable> , <Buffer> , <Paramètres> [, <Nom de la racine>])` — *Serialize*
- `Désérialise(<Variable> , <Buffer> , <Paramètres>)` — *Deserialize*

## Authentification

- `AuthIdentifie(<Paramètres d'authentification> , <Procédure WLangage>)` — *AuthIdentify*

## E-mail

- `<Résultat> = EmailOuvreSessionSMTP(<Nom utilisateur> [, <Mot de passe>] , <Adresse serveur SMTP> [, <Numéro port SMTP> [, <Mode Asynchrone> [, <Option>]]])` — *EmailStartSMTPSession*
- `<Résultat> = EmailEnvoieMessage(<Session> [, <Email> [, <Options avancées>]])` — *EmailSendMessage*
- `<Résultat> = EmailLitMessage(<Session> [, <Email>] , <Numéro message>)` — *EmailReadMessage*
- `EmailFermeSession(<Session>)` — *EmailCloseSession*

## Sockets

- `<Résultat> = SocketCrée(<Nom du socket> , <Numéro de port> [, <Adresse>])` — *SocketCreate*
- **SocketConnecte** — *SocketConnect*
- `<Résultat> = SocketEcrit(<Nom du socket> , <Message>)` — *SocketWrite*
- `<Résultat> = SocketLit(<Nom du socket> [, <Attente indéfinie> [, <Attente maximale> [, <Nombre maximum d'octets> [, <Délai de réception des données>]]]])` — *SocketRead*
- `SocketFerme(<Nom du socket>)` — *SocketClose*
- `<Résultat> = SocketExiste(<Nom du socket>)` — *SocketExist*
- `<Résultat> = SocketAttendConnexion(<Nom du socket> [, <Durée maximale>])` — *SocketWaitForConnection*
- `<Résultat> = SocketAccepte(<Nom du socket>)` — *SocketAccept*

## Fichiers (fxxx)

- `<Résultat> = fSauveTexte(<Nom et chemin du fichier texte> , <Contenu>)` — *fSaveText*
- `<Résultat> = fChargeTexte(<Nom et chemin du fichier Texte> [, <Mode de chargement>])` — *fLoadText*
- `<Résultat> = fSélecteur(<Répertoire initial> , <Fichier sélectionné par défaut> , <Titre du sélecteur> , <Types de fichiers> , <Extension par défaut> [, <Mode de sélection>])` — *fSelect*
- `<Résultat> = fCopieFichier(<Fichier source> , <Fichier ou répertoire destination> [, <Indicateur de copie>])` — *fCopyFile*
- `<Résultat> = fSupprime(<Nom du fichier> [, <Option>])` — *fDelete*
- `<Résultat> = fRenomme(<Chemin du fichier à renommer> , <Nouveau chemin du fichier>)` — *fRename*
- `<Résultat> = fConstruitChemin(<Chemin> , <Nom court> [, <Extension>])` — *fBuildPath*

## Dialogue / UI

- `Info(<Texte> [, <Ligne 2> [... [, <Ligne n>]]])` — *Info*
- `Erreur(<Texte> [, <Ligne 2> [... [, <Ligne n>]]])` — *Error*
- `Avertissement(<Texte> [, <Ligne 2> [... [, <Ligne n>]]])` — *Warning*
- **OuiNon** — *YesNo*
- **Confirmer** — *Confirm*
- `<Résultat> = Dialogue(<Identifiant du message> [, <Paramètre 1> [, <Paramètre N>]])` — *Dialog*
- `ToastAffiche(<Message> [, <Durée d'affichage> [, <Cadrage Vertical> [, <Cadrage Horizontal> [, <Couleur de fond>]]]])` — *ToastDisplay*
- `Trace(<Informations> [, <Informations complémentaires 1> [... [, <Informations complémentaires N>]]])` — *Trace*

## Divers

- `<Résultat> = ErreurInfo([<Type information>])` — *ErrorInfo*
- `<Résultat> = ExceptionInfo([<Type information>])` — *ExceptionInfo*
- `<Résultat> = RéseauUtilisateur()` — *NetworkUser*
- `<Résultat> = Arrondi(<Valeur numérique> [, <Nombre de décimales>])` — *Round*
- `ChronoDébut([<Numéro du chronomètre>])` — *ChronoStart*
- `<Résultat> = ChronoFin([<Numéro du chronomètre>])` — *ChronoEnd*

## Constantes courantes par famille

**Comparaison de chaînes (ChaîneCompare, ChaîneFormate…)** : `ccNormal`, `ccSansCasse`, `ccSansAccent`, `ccSansEspace`, `ccSansEspaceIntérieur`, `ccSansPonctuationNiEspace`

**Toast — durée / cadrage** : `toastCourt`, `toastLong`, `cvBas`, `cvHaut`, `cvMilieu`, `chCentre`, `chDroite`, `chGauche`

**Méthodes HTTP** : `httpGet`, `httpPost`, `httpPut`, `httpDelete`, `httpPatch`, `httpHead`

**HFSQL — options de requête** : `hRequêteDéfaut`, `hRequêteSansCorrection`

**Sérialisation (Sérialise / Désérialise)** : `psdJSON`, `psdXML`

**Tri de tableau (TableauTrie)** : `ttCroissant`, `ttDécroissant`, `ttFonction`, `ttColonne`

**Affichage Table (TableAffiche)** : `taDébut`

**Couleurs prédéfinies** : `Blanc`, `Noir`, `Argent`, `Transparent`, `GrisClair`, `GrisFoncé`, `RougeClair`, `RougeFoncé`, `VertClair`, `VertFoncé`, `BleuClair`, `BleuFoncé`, `JauneClair`, `JauneFoncé`, `CyanClair`, `CyanFoncé`, `MagentaClair`, `MagentaFoncé`

**Booléens / valeurs spéciales** : `Vrai`, `Faux`, `Null`
