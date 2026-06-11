# -*- coding: utf-8 -*-
"""Génère index/cheatsheet.md : fonctions courantes par famille, avec signature
(extraites de index/lookup.tsv). Seules les fonctions réellement présentes sont émises."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
LOOKUP = os.path.join(HERE, "..", "index", "lookup.tsv")
OUT = os.path.join(HERE, "..", "index", "cheatsheet.md")

# name_FR(lower) -> (nom_FR, nom_EN, signature)  (fonctions uniquement)
idx = {}
with open(LOOKUP, encoding='utf-8') as fh:
    for line in fh:
        if line.startswith('#'):
            continue
        p = line.rstrip('\n').split('\t')
        if len(p) < 6:
            continue
        _id, typ, fr, en, mod, sig = p[0], p[1], p[2], p[3], p[4], p[5]
        if typ == 'Fonction':
            idx.setdefault(fr.lower(), (fr, en, sig))

FAMILLES = [
 ("HFSQL — accès aux données", ["HExécuteRequêteSQL","HExécuteRequête","HLitPremier","HLitDernier","HLitSuivant","HLitPrécédent","HEnDehors","HLitRecherchePremier","HLitRecherche","HAjoute","HModifie","HSupprime","HRAZ","HNbEnr","HTrouve","HFiltre","HAnnuleDéclaration","HErreurInfo","HSauvePosition","HRetourPosition"]),
 ("Chaînes", ["ChaîneConstruit","ExtraitChaîne","ExtraitChaîneEntre","Remplace","Majuscule","Minuscule","Complète","Taille","Position","PositionOccurrence","ChaîneCommencePar","ChaîneFinitPar","Contient","Gauche","Droite","Milieu","SansEspace","NumériqueVersChaîne","ChaîneVersNumérique"]),
 ("Date / Heure", ["DateDuJour","DateSystème","DateVersChaîne","ChaîneVersDate","DateValide","HeureSystème","DateHeureVersChaîne"]),
 ("Tableaux", ["TableauAjoute","Ajoute","TableauSupprime","TableauSupprimeTout","TableauCherche","TableauTrie","TableauOccurrence","TableauInsère"]),
 ("Champ Table", ["TableAjouteLigne","TableSupprimeLigne","TableSupprimeTout","TableAffiche","TableSelect","TableSelectMoins","TableRecherche"]),
 ("HTTP / REST", ["RESTEnvoie","HTTPEnvoie","HTTPRequête","HTTPDonneRésultat"]),
 ("JSON / Sérialisation", ["Sérialise","Désérialise"]),
 ("Authentification", ["AuthIdentifie"]),
 ("E-mail", ["EmailOuvreSessionSMTP","EmailEnvoieMessage","EmailLitMessage","EmailFermeSession"]),
 ("Sockets", ["SocketCrée","SocketConnecte","SocketEcrit","SocketLit","SocketFerme","SocketExiste","SocketAttendConnexion","SocketAccepte"]),
 ("Fichiers (fxxx)", ["fSauveTexte","fChargeTexte","fSélecteur","fCopieFichier","fSupprime","fRenomme","fRépertoireSélecteur","fConstruitChemin"]),
 ("Dialogue / UI", ["Info","Erreur","Avertissement","OuiNon","Confirmer","Dialogue","ToastAffiche","Trace"]),
 ("Divers", ["ErreurInfo","ExceptionInfo","RéseauUtilisateur","Arrondi","ChronoDébut","ChronoFin"]),
]

lines = ["# Aide-mémoire — fonctions WLangage courantes", "",
         "Signatures vérifiées (extraites de la doc). Pour le détail/paramètres : `pages/<id>.md` ou `index/lookup.tsv`.", ""]
missing = []
for titre, noms in FAMILLES:
    lines.append("## " + titre)
    lines.append("")
    for nom in noms:
        e = idx.get(nom.lower())
        if not e:
            missing.append(nom); continue
        fr, en, sig = e
        enpart = " — *{}*".format(en) if en else ""
        if sig:
            first = sig.split(" ⏐ ")[0]
            lines.append("- `{}`{}".format(first, enpart))
        else:
            lines.append("- **{}**{}".format(fr, enpart))
    lines.append("")
# --- constantes courantes par famille (toutes vérifiées dans la doc) ---
FAM_CONST = [
 ("Comparaison de chaînes (ChaîneCompare, ChaîneFormate…)",
  ["ccNormal","ccSansCasse","ccSansAccent","ccSansEspace","ccSansEspaceIntérieur","ccSansPonctuationNiEspace"]),
 ("Toast — durée / cadrage",
  ["toastCourt","toastLong","cvBas","cvHaut","cvMilieu","chCentre","chDroite","chGauche"]),
 ("Méthodes HTTP",
  ["httpGet","httpPost","httpPut","httpDelete","httpPatch","httpHead"]),
 ("HFSQL — options de requête",
  ["hRequêteDéfaut","hRequêteSansCorrection"]),
 ("Sérialisation (Sérialise / Désérialise)",
  ["psdJSON","psdXML"]),
 ("Tri de tableau (TableauTrie)",
  ["ttCroissant","ttDécroissant","ttFonction","ttColonne"]),
 ("Affichage Table (TableAffiche)",
  ["taDébut"]),
 ("Couleurs prédéfinies",
  ["Blanc","Noir","Argent","Transparent","GrisClair","GrisFoncé","RougeClair","RougeFoncé",
   "VertClair","VertFoncé","BleuClair","BleuFoncé","JauneClair","JauneFoncé",
   "CyanClair","CyanFoncé","MagentaClair","MagentaFoncé"]),
 ("Booléens / valeurs spéciales",
  ["Vrai","Faux","Null"]),
]
lines.append("## Constantes courantes par famille")
lines.append("")
for titre, noms in FAM_CONST:
    lines.append("**{}** : {}".format(titre, ", ".join("`"+n+"`" for n in noms)))
    lines.append("")

with open(OUT, "w", encoding="utf-8") as fh:
    fh.write("\n".join(lines))
print("cheatsheet.md généré.")
print("Fonctions non trouvées (ignorées) :", ", ".join(missing) if missing else "(aucune)")
