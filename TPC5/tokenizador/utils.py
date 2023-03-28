import sys
import argparse

def get_keywords(lang):
    abrevs = load_abrevs()
    trans = load_trans()
    keywords = {}
    keywords['abrevs'] = abrevs[lang]
    for pal in trans:
        if lang != 'en':
            keywords[pal] = trans[pal][lang]
        else:
            keywords[pal] = pal
    return keywords


def load_abrevs():
    abrevs_dict = {}
    file = open("tokenizador/conf/abervs.txt", "r")
    ln_list = file.read().split("#")[1:]
    for ln in ln_list:
        lang, *abrevs = ln.split("\n")
        if len(abrevs) > 0:
            abrevs_dict[lang] = abrevs if abrevs[-1] else abrevs[:-1]
    return abrevs_dict

def load_trans():
    trans_dict = {}
    file = open("tokenizador/conf/trans.txt", "r")
    pal_list = file.read().split("#")[1:]
    for pal in pal_list:
        en_pal, *trans_pals = pal.split("\n")
        trans_dict[en_pal] = {}
        for trans in trans_pals:
            lang_id, *lang_trans = trans.split(":")
            if len(lang_trans) == 1:
                trans_dict[en_pal][lang_id] = lang_trans[0].upper()
    return trans_dict

def input(input='stdin'):
    text = ""
    if input == 'stdin':
        for line in sys.stdin:
            text+=line
    else:
        input = open(input,'r')
        text = input.read()
    return text

def output(text, output='stdout'):
    if output == 'stdout':
        sys.stdout.write(text)
    else:
        file = open(output,'w')
        file.write(text)

def read_args():
    parser = argparse.ArgumentParser(description='Procces tokenizar options.')
    parser.add_argument('-p', '--poems',action='store_true')
    parser.add_argument("-l", '--language', default='en', choices=['en', 'pt', 'fr'])
    return parser.parse_args()