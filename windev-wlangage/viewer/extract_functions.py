# -*- coding: utf-8 -*-
"""Noms de fonctions WLangage intégrées (frontmatter type=Fonction, nom simple)
-> wlangage-viewer/functions.js : const FUNC_SET = new Set([...]) (minuscules)."""
import os, re, json
HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = os.path.join(HERE, "..", "pages")
OUTJS = os.path.join(HERE, "functions.js")
reTitle = re.compile(r'^title:\s*"(.*?)"', re.M)
reType  = re.compile(r'^type:\s*"(.*?)"', re.M)
names = set()
for f in os.listdir(PAGES):
    if not f.endswith('.md'): continue
    with open(os.path.join(PAGES,f), encoding='utf-8') as fh:
        head = fh.read(700)
    mt = reType.search(head); ti = reTitle.search(head)
    if not mt or not ti or mt.group(1) != 'Fonction': continue
    name = re.sub(r'\s*\(Fonction\)\s*$','', ti.group(1)).strip()
    # on ignore les syntaxes préfixées "<Variable ...>.Methode"
    if name.startswith('<') or '.' in name: continue
    if re.match(r'^[A-Za-zÀ-ÿ_][\wÀ-ÿ]*$', name):
        names.add(name.lower())
arr = sorted(names)
with open(OUTJS,'w',encoding='utf-8') as fh:
    fh.write("// Fonctions WLangage intégrées (doc officielle), en minuscules.\n")
    fh.write("const FUNC_SET = new Set(" + json.dumps(arr, ensure_ascii=False) + ");\n")
print("Fonctions extraites :", len(arr))
print("Test (intégrées):", [n for n in ('hexécuterequêtesql','tableautrie','chaînecompare','trace','chaîneconstruit') if n in names])
print("Taille functions.js :", round(os.path.getsize(OUTJS)/1024,1), "Ko")
