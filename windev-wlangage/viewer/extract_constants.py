# -*- coding: utf-8 -*-
"""
Extrait la liste des constantes WLangage depuis le corpus de doc.
Repère les paramètres typés "Constante ... de type ..." puis collecte les
noms de constantes dans la 1re colonne des tableaux qui suivent.
Produit wlangage-viewer/constants.js : const CONST_SET = new Set([...]).
"""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = os.path.join(HERE, "..", "pages")
OUTJS = os.path.join(HERE, "constants.js")

# marqueur de type "Constante ... de type" (sur la ligne du paramètre)
reTypeConst = re.compile(r'\*[^*]*[Cc]onstante[^*]*\*')
# cellule italique en début de ligne de tableau : | *NomConstante* ... | ... |
reCell = re.compile(r'^\s*>?\s*\|\s*\*([A-Za-zÀ-ÿ_][\wÀ-ÿ]*)\*')
# un identifiant de constante plausible
reIdent = re.compile(r'^[A-Za-zÀ-ÿ_][\wÀ-ÿ]*$')

consts = {}   # nom -> nb d'occurrences

def add(name):
    if reIdent.match(name) and len(name) >= 2:
        consts[name] = consts.get(name, 0) + 1

for f in os.listdir(PAGES):
    if not f.endswith('.md'):
        continue
    with open(os.path.join(PAGES, f), encoding='utf-8') as fh:
        lines = fh.read().split('\n')
    for ln in lines:
        # toute 1re cellule de tableau en italique = définition de constante
        m = reCell.match(ln)
        if m:
            # on ignore l'entête de séparation et les cellules vides
            add(m.group(1))

# Vrai/Faux/Null + quelques incontournables
for c in ('Vrai','Faux','Null','True','False'):
    consts.setdefault(c, 1)

names = sorted(consts.keys(), key=str.lower)
js = "// Constantes WLangage extraites de la documentation officielle.\n"
js += "const CONST_SET = new Set(" + json.dumps(names, ensure_ascii=False) + ");\n"
with open(OUTJS, 'w', encoding='utf-8') as fh:
    fh.write(js)

print("Constantes extraites :", len(names))
print("Exemples :", ", ".join(names[:30]))
print("Toast/cadrage présents :", [n for n in names if n in
      ('toastCourt','toastLong','cvBas','cvHaut','cvMilieu','chCentre','chDroite','chGauche','ccNormal','ccSansCasse')])
print("Taille constants.js :", round(os.path.getsize(OUTJS)/1024,1), "Ko")
