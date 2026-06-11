# -*- coding: utf-8 -*-
"""Génère index/lookup.tsv : 1 ligne par rubrique pour une recherche en UN seul grep.
Colonnes (TAB) : id  type  nom_FR  nom_EN  module  signature(s)
La signature n'est présente que pour les fonctions (extraite de index/signatures.md)."""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = os.path.join(HERE, "..", "pages")
SIGS = os.path.join(HERE, "..", "index", "signatures.md")
OUT = os.path.join(HERE, "..", "index", "lookup.tsv")

reField = re.compile(r'^(\w+):\s*(.*)$')

def front(text):
    if not text.startswith('---'):
        return {}
    end = text.find('\n---', 3)
    if end < 0:
        return {}
    d = {}
    for line in text[3:end].split('\n'):
        m = reField.match(line)
        if not m:
            continue
        k, v = m.group(1), m.group(2).strip()
        if v.startswith('"') and v.endswith('"'):
            v = v[1:-1].replace('\\"', '"').replace('\\\\', '\\')
        d[k] = v
    return d

# --- signatures par id (depuis signatures.md) ---
sig_map = {}
cur = None
reHead = re.compile(r'^###\s+\[[^\]]*\]\(\.\./pages/(\d+)\.md\)')
reSig = re.compile(r'^`(.+)`\s*$')
with open(SIGS, encoding='utf-8') as fh:
    for line in fh:
        h = reHead.match(line)
        if h:
            cur = h.group(1)
            continue
        if cur:
            s = reSig.match(line.rstrip('\n'))
            if s:
                sig_map.setdefault(cur, []).append(s.group(1).strip())
            elif line.strip() == '' or line.startswith('#'):
                cur = None

def clean(s):
    return (s or '').replace('\t', ' ').replace('\n', ' ').strip()

rows = []
for f in os.listdir(PAGES):
    if not f.endswith('.md'):
        continue
    with open(os.path.join(PAGES, f), encoding='utf-8') as fh:
        fr = front(fh.read(800))
    if not fr:
        continue
    idp = fr.get('id', f[:-3])
    title = re.sub(r'\s*\([^()]*\)\s*$', '', fr.get('title', ''))  # nom sans le suffixe (Fonction)…
    sig = ' ⏐ '.join(sig_map.get(idp, []))
    rows.append((clean(title), idp, clean(fr.get('type', '')), clean(title),
                 clean(fr.get('english', '')), clean(fr.get('module', '')), clean(sig)))

rows.sort(key=lambda r: r[0].lower())
with open(OUT, 'w', encoding='utf-8') as fh:
    fh.write("# id\ttype\tnom_FR\tnom_EN\tmodule\tsignature\n")
    for _key, idp, typ, fr_, en, mod, sig in rows:
        fh.write("\t".join((idp, typ, fr_, en, mod, sig)) + "\n")

print("lookup.tsv :", len(rows), "rubriques,",
      round(os.path.getsize(OUT)/1024/1024, 2), "Mo")
