# -*- coding: utf-8 -*-
"""Extrait les noms de types de variables WLangage (frontmatter type=Type de variable)
-> wlangage-viewer/types.js : const TYPE_SET = new Set([...]) (en minuscules)."""
import os, re, json
HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = os.path.join(HERE, "..", "pages")
OUTJS = os.path.join(HERE, "types.js")
reTitle = re.compile(r'^title:\s*"(.*?)"', re.M)
reType  = re.compile(r'^type:\s*"(.*?)"', re.M)
names = set()
for f in os.listdir(PAGES):
    if not f.endswith('.md'): continue
    with open(os.path.join(PAGES,f), encoding='utf-8') as fh:
        head = fh.read(700)
    mt = reType.search(head); ti = reTitle.search(head)
    if not mt or not ti: continue
    if mt.group(1) != 'Type de variable': continue
    name = re.sub(r'\s*\(Type de variable\)\s*$','', ti.group(1)).strip()
    # on ne garde que les noms d'un seul token (utilisables dans le tokenizer)
    if re.match(r'^[A-Za-zÀ-ÿ_][\wÀ-ÿ]*$', name):
        names.add(name.lower())
# types de base usuels
for t in ('chaîne','entier','réel','booléen','monétaire','date','heure','durée',
          'dateheure','tableau','buffer','variant','numérique','caractère','octet',
          'structure','objet','enregistrement'):
    names.add(t)
arr = sorted(names)
with open(OUTJS,'w',encoding='utf-8') as fh:
    fh.write("// Types de variables WLangage (doc officielle), en minuscules.\n")
    fh.write("const TYPE_SET = new Set(" + json.dumps(arr, ensure_ascii=False) + ");\n")
print("Types extraits :", len(arr))
print("Présents restrequête/restréponse/toast/json :",
      [t for t in arr if t in ('restrequête','restréponse','toast','json','restrequete','restreponse')])
print("Exemples :", ", ".join(arr[:25]))
