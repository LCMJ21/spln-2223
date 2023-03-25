#!/usr/bin/env python3
"""
Tokenizador for books.
"""

__version__ = "0.1.0"

import re
from utils import *

list_poemas = []

def page_break(text):
    regex_nl = r'([a-z.0-9,;\-–?!\(\)])(\n\n)+([a-zA-Z.0-9,;\-–?!\(\)])'
    return re.sub(regex_nl,r'\1\n\3',text)

def punctuation(text):
    regex_punc = r'([.!,?;:' + r'\"\-\”\–\`()\[\]])?(\w+)([.!,?;:' + r'\"\-\”\–\`()\[\]])'
    return re.sub(regex_punc,r'\1 \2 \3',text)

def chapters(text):
    regex_cap = r'.*(CAPÍTULO +(\w+|\d+)).*\n((.+\n)*)'
    return re.sub(regex_cap,r'#\1\n[\3]\n',text)

def paragraphs(text):
    regex_par = r'([.!?;])\n(([^.!?;]|[\u00C0-\u017F]))'
    return re.sub(regex_par,r'\1\n/PAR/ \2',text)

def sentences_single_line(text):
    regex_sen = r'([^.!?])\n+([^.!?])'
    return re.sub(regex_sen,r'\1 \2',text)

def sentences_per_line(text):
    regex_sen = r'([^.!?][.?!])(\s|[^.])'
    text = re.sub(regex_sen,r'\1\2\n',text)
    regex_abrv = r'((Sr)|(Sra))\.(\s*)\n'
    return re.sub(regex_abrv,r'\1.\4',text)

def save_poems(poema):
    list_poemas.append(poema[1])
    return f">>{len(list_poemas)}<<"

def poems(text):
    if options['poems']:
        regex_poema = r'<poem>(.*?)</poem>'
        text = re.sub(regex_poema,save_poems,text,flags=re.S)
        print(list_poemas)
    return text

def tokenizer():
    text = input()

    # 0. Quebra de pagina
    text = page_break(text)
    # 1. Separar pontuação das palavras
    text = punctuation(text)
    # 2. Marcar capitulos
    text = chapters(text)
    # 3. Separar paragrafos de linhas pequenas
    text = paragraphs(text)
    # 4. Juntar linhas da mesma frase
    text = sentences_single_line(text)
    # 5. Uma frase por linha
    text = sentences_per_line(text)
    # 6. Tratar Poemas (tagged)
    text = poems(text)

    output(text)

if __name__ == "__main__":
    print(f'Tokenizer version={__version__}')
    options = read_args()
    tokenizer()