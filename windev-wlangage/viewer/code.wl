//§ Déclarations globales de FEN_GoogleSheet
gsIDClasseur est une chaîne = "1AbCdEfGhIjKlMnOpQrStUvWxYz0123456789"
gsClientID est une chaîne = "votre_id.apps.googleusercontent.com"
gsClientSecret est une chaîne = "votre_secret"
gToken est un AuthToken

//§ Procédure locale ConnecterGoogle
PROCÉDURE LOCAL ConnecterGoogle()
oParams est un OAuth2Paramètres

oParams.ClientID = gsClientID
oParams.ClientSecret = gsClientSecret
oParams.URLAuth = "https://accounts.google.com/o/oauth2/v2/auth"
oParams.URLToken = "https://oauth2.googleapis.com/token"
oParams.Scope = "https://www.googleapis.com/auth/spreadsheets"
oParams.URLRedirection = "http://localhost:9876/"

gToken = AuthIdentifie(oParams)

//§ Procédure locale LirePlage
PROCÉDURE LOCAL LirePlage(sPlage est une chaîne)
req est un httpRequête
rép est un httpRéponse
vJSON est un Variant
sValeurs est une chaîne

req.URL = "https://sheets.googleapis.com/v4/spreadsheets/" + gsIDClasseur + "/values/" + sPlage
req.Méthode = httpGet
req.AuthToken = gToken

rép = HTTPEnvoie(req)
SI rép.CodeEtat <> 200 ALORS
	Erreur("Lecture impossible (code " + rép.CodeEtat + ").")
	RENVOYER ""
FIN

Désérialise(vJSON, rép.Contenu, psdJSON)
POUR TOUT uneLigne DE vJSON.values
	sValeurs += uneLigne[1] + RC
FIN
RENVOYER sValeurs

//§ Procédure locale EcrirePlage
PROCÉDURE LOCAL EcrirePlage(sPlage est une chaîne, sValeur est une chaîne)
req est un httpRequête
rép est un httpRéponse
vCorps est un Variant
sJSON est une chaîne

vCorps.range = sPlage
vCorps.majorDimension = "ROWS"
vCorps.values[1][1] = sValeur

Sérialise(vCorps, sJSON, psdJSON)

req.URL = "https://sheets.googleapis.com/v4/spreadsheets/" + gsIDClasseur + "/values/" + sPlage + "?valueInputOption=RAW"
req.Méthode = httpPut
req.AuthToken = gToken
req.ContentType = "application/json"
req.Contenu = sJSON

rép = HTTPEnvoie(req)
RENVOYER (rép.CodeEtat = 200)

//§ Clic de BTN_Synchroniser
ConnecterGoogle()
EDT_Resultat = LirePlage("Feuille1!A1:A10")
SI EcrirePlage("Feuille1!B1", "Mis à jour") ALORS
	Info("Cellule B1 mise à jour.")
FIN
