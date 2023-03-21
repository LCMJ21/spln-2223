#!/usr/bin/env python3
"""
Tihs is a tokenizador for books.
"""

__version__ = "0.1.0"

import sys
import fileinput
import re

def load_abrevs():
    abrevs_dict = {}
    file = open("TPC5/tokenizador/conf/abervs.txt", "r")
    ln_list = file.read().split("#")[1:]
    for ln in ln_list:
        lang, *abrevs = ln.split("\n")
        if len(abrevs) > 0:
            abrevs_dict[lang] = abrevs if abrevs[-1] else abrevs[:-1]
    return abrevs_dict

def load_trans():
    trans_dict = {}
    file = open("TPC5/tokenizador/conf/trans.txt", "r")
    pal_list = file.read().split("#")[1:]
    for pal in pal_list:
        en_pal, *trans_pals = pal.split("\n")
        trans_dict[en_pal] = {}
        for trans in trans_pals:
            lang_id, *lang_trans = trans.split(":")
            if len(lang_trans) == 1:
                trans_dict[en_pal][lang_id] = lang_trans[0]
    return trans_dict

print(load_trans())

def tokenizador():
    text = ""
    for line in fileinput.input():
        text += line

    #0. Quebra de paginas
    #1. Separar pontuação das palavras ✓
    #2. Marcar capitulos ✓
    #3. Separar paragrafos de linhas pequenas
    #4. Juntar linhas da mesma frase ✓
    #5. Uma frase por linha 

    regex_cap = r".*(CAP[IÍ]TULO \w+).*"
    text = re.sub(regex_cap, r"\n# \1", text)
    
    regex_nl = r"([a-z0-9,:])\n\n([a-z0-9])"
    text = re.sub(regex_nl, r"\1\n\2", text)

    list_poemas = {}
    def guarda_poema(poema):
        list_poemas.append(poema[1])
        return f">>{len(list_poemas)}<<"

    regex_poema = r'<poema>(.*)</poema>'
    text = re.sub(regex_poema, guarda_poema, text, flags=re.S)


    #1. Separar pontuação das palavras
    regex_pont = r"(\w)([.,?!;\-])+"
    text = re.sub(regex_pont, r"\1 \2", text)
