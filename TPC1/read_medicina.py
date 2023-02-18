# open medicina and apply regex
from dataclasses import dataclass
import json
import re
import os

# transform a pdf file to xml
def pdf_to_xml(pdf_file):
    os.system(f"pdftohtml {pdf_file} -f 20 -l 543 -xml")


def clean_text(text):
    # clean the text
    pattern = re.compile(r'^(.[^t\n][^e\n][^x\n].*|<text.*>[ ]+<\/text>|<text.*><(b|i)>[ ]+<\/(b|i)><\/text>)\n', re.MULTILINE)
    text = pattern.sub(r'', text)
    return text

def remove_header_fotter(text):
    # remove header
    text = re.sub(r'<text.*font="1">ocabulario.*<\/text>', r'###', text)
    text = re.sub(r'.*\n###\n.*\n', r'', text)
    return text

def mark_Complete(text):
    # mark complete entries
    text = re.sub(r'<text.*font="3"><b>[ ]*(\d+)[ ]*(.*)[ ]*<\/b><\/text>\n<text.*font="3"><b>[ ]*(.*)[ ]*(f|m|a)[ ]*<\/b><\/text>', r'#C# \1/\2\3/\4', text)
    text = re.sub(r'<text.*font="3"><b>[ ]*(\d+)[ ]*(.*)[ ]*(f|m|a)<\/b><\/text>', r'#C# \1/\2/\3', text)
    text = re.sub(r'<text.*font="3"><b>[ ]*(\d+)[ ]*(.*)[ ]*<\/b><\/text>', r'#C# \1/\2', text)
    text = re.sub(r'<text.*font="2">[ ]*(\d+)[ ]*<\/text>\n<text.*font="3"><b>(.*)(f|m|a)<\/b><\/text>', r'#C# \1/\2/\3', text)
    text = re.sub(r'<text.*font="2">[ ]*(\d+)[ ]*<\/text>\n<text.*font="3"><b>(.*)<\/b><\/text>', r'#C# \1/\2', text)
    return text

def mark_Remesive(text):
    # mark complete entries
    text = re.sub(r'<text.*font="3"><b>[ ]*(.{2,})<\/b><\/text>', r'#R# \1', text)
    return text

def mark_Language(text):
    # mark complete entries
    text = re.sub(r'<text.*font="0">[ ]*(es|en|pt|la)[ ]*<\/text>', r'@\1', text)
    return text

def remove_all(text):
    text = re.sub(r'<text.*>(([^<]+))(<\/b>)?(<\/i>)?<\/text>', r'\1', text)
    return text


# transform to pdf and read the file
#pdf_to_xml('Aula1/medicina.pdf')
real_text = open('Aula1/medicina.xml').read()

#process the text
real_text = clean_text(real_text)
real_text = remove_header_fotter(real_text)
real_text = mark_Complete(real_text)
real_text = mark_Remesive(real_text)
real_text = mark_Language(real_text)
real_text = remove_all(real_text)

@dataclass
class LanguageEntry:
    language: str
    term: str

@dataclass
class RemessiveEntry:
    title: str
    term: str

@dataclass
class CompleteEntry:
    id: int
    desciption: str
    gender: str
    other:str
    LanguageEntry: dict[str, LanguageEntry]
    RemessiveEntry: dict[str, RemessiveEntry]


def read_to_struct(text):
    entry_dict = {}
    # create a list of entries
    all_entries = text.split('#C# ')
    for entry in all_entries[1:]:

        # first line from entry = CompleteEntry
        separte_fisrt = entry.split('\n', 1)
        first_line = separte_fisrt[0].split('/')

        # remessive entries
        remessive_dict = {}
        remessive = separte_fisrt[1].split('#R# ')
        for remessive_entry in remessive[1:]:
            remessive_entry = remessive_entry.split('\n', 1)
            remessive_dict[remessive_entry[0]] = RemessiveEntry(remessive_entry[0], remessive_entry[1].replace('\n', ' '))

        # other info
        rest_of_entry = remessive[0].split('@')
        other = rest_of_entry[0].replace('\n', ' ') if rest_of_entry[0] else None

        # language entries
        language_dict = {}
        for languages in rest_of_entry[1:]:
            language = languages.split('\n', 1)
            language_dict[language[0]] = LanguageEntry(language[0], language[1].replace('\n', ' '))

        entry_dict[first_line[0]] = CompleteEntry(first_line[0], first_line[1], first_line[2] if len(first_line) == 3 else None, other, language_dict, remessive_dict)
    
    return entry_dict


def to_json(obj):
    return json.dumps(obj, indent= 4, default=lambda obj: obj.__dict__)

entry_dict = read_to_struct(real_text)
# write back on file
open('Aula1/medicina_prod.xml', 'w').write(real_text)
open('Aula1/medicina.json', 'w').write(to_json(entry_dict))
