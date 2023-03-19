#!/usr/bin/env python3

import sys
import fileinput
import re


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

#4. Juntar linhas da mesma frase
def frase(match):
    x = re.sub("\n", " ", match[0])
    return x + "\n"

print(text)